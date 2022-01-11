import os
import sys
from collections import Counter
from zipfile import ZipFile
import pandas as pd
from keras.callbacks import EarlyStopping
from tabulate import tabulate
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras import backend as K
from sklearn.model_selection import train_test_split
import numpy as np


def file_to_str(file):
    _str = ""
    with open(file, 'r', encoding='utf-8') as f:
        _str = f.readlines()
        _str = "".join(_str)
    return _str


def print_README_table(docs):
    print()
    print('\n| file | similarity |\n| ------------- | ------------- |')
    for doc in docs:
        doc_name = doc[0].split('\\')[2]
        doc_dis = doc[1]
        print('| [', doc_name, '](docs/Clean_Punctuation/',
              doc_name.replace("root", "").replace("prefsuf", ""), ')|', doc_dis, '|', sep="")
    print()


def clean(_str):
    return ''.join(e for e in _str if e.isalnum() and not e.isdigit())


def read_file(file):
    words = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            words += line.split()
    words = [clean(w) for w in words]
    return words


def read_files(docs_locations):
    """
    :param docs_locations: list of lications of the files.
    :return: dictionary of file_location to list of words.
    """
    docs = {}
    for doc in tqdm(docs_locations):
        docs[doc] = read_file(doc)
    return docs


def get_bow(docs, max_size, min_word_count=100):
    """
    :param docs: dictionary of file_location to list of words.
    :param max_size: max bow size, The function will delete the least common words.
    :param min_word_count: The function will delete the words that are less common than 'min_word_count'.
    :return: bag of words.
    """
    stop_words = get_stop_words()
    bow = []
    for doc in docs.values():
        bow += list(doc)
    bow = Counter(bow).most_common()
    bow = [word for word, count in bow if count > min_word_count and len(word) >= 2 and word not in stop_words][
          :max_size]
    return bow


def my_unzip(docs_list):
    index = 0
    with ZipFile('Clean_Punctuation.zip', 'r') as zipObj:
        listOfFileNames = ["Clean_Punctuation/" + str(n) + ".txt" for n in docs_list]
        for fileName in listOfFileNames:
            zipObj.extract(fileName, 'docs')
            index += 1


def my_csv(symbol=None):
    df = pd.read_csv('data.csv', names=["doc", "type"])

    if symbol is not None:
        df = df[df['type'] == symbol]

    my_docs = df["doc"].tolist()
    my_docs.sort()
    return my_docs


def get_file_name(file):
    return os.path.basename(file).replace('prefsuf', '').replace('root', '').replace('.txt', '')


def kmeans(df, real_symbols, title):
    print("[LOG] Ploting", title)
    _scalar = StandardScaler()
    _scalar.fit(df)
    print("starting k-means")
    kmeans_scale = KMeans(n_clusters=2).fit(df)
    labels_scale = kmeans_scale.labels_
    mapping = {0: 'A', 1: 'B', 2: 'C'}
    predict = [mapping[i] for i in labels_scale]
    pca_features = PCA(n_components=2).fit(df).transform(df)
    fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, figsize=(20, 10))
    fig.suptitle(title, fontsize=16)
    sns.scatterplot(pca_features[:, 0], pca_features[:, 1], palette='Set1', hue=predict, s=100, alpha=0.2,
                    ax=ax1).set_title('KMeans', fontsize=15)
    plt.legend()
    ax1.set_xlabel("PC1")
    ax1.set_ylabel("PC2")
    sns.scatterplot(pca_features[:, 0], pca_features[:, 1], palette='Set1', hue=real_symbols, s=100, alpha=0.2,
                    ax=ax2).set_title('Real', fontsize=15)
    plt.legend()
    ax2.set_xlabel("PC1")
    ax2.set_ylabel("PC2")
    plt.savefig('plots\\' + title + '.png')

    accuracy = str(accuracy_score(real_symbols, predict))
    f1 = str(f1_score(real_symbols, predict, average='macro'))
    precision = str(precision_score(real_symbols, predict, average='macro'))
    recall = str(recall_score(real_symbols, predict, average='macro'))
    print()
    print('\n|', title, '|  |\n| ------------- | ------------- |')
    for v in [["Accuracy", accuracy], ["F1", f1], ["Precision", precision], ["Recall", recall]]:
        print(v[0], '|', v[1], '|')
    print()
    with open('plots\\results.txt', 'a') as file:
        file.writelines(title + ' kmeans' "\n")
        file.writelines("Recall:" + recall + "\n")
        file.writelines("F1:" + f1 + "\n")
        file.writelines("Precision:" + precision + "\n")
        file.writelines("Accuracy:" + accuracy + "\n")
        file.writelines("\n")


def get_stop_words():
    words = []
    with open('heb_stopwords.txt', 'r', encoding='utf-8') as f:
        for line in f:
            words += line.split()
    return words


def recall_m(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall


def precision_m(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision


def f1_m(y_true, y_pred):
    precision = precision_m(y_true, y_pred)
    recall = recall_m(y_true, y_pred)
    return 2 * ((precision * recall) / (precision + recall + K.epsilon()))


def batch_generator(x_data, y_data, batch_size=128, title=''):
    mapping = {'A': 0, 'B': 1, 'C': 2}
    y_data = [mapping[i] for i in y_data]

    model = Sequential()
    model.add(Dense(10, activation='relu'))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(7, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc', f1_m, precision_m, recall_m])

    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, train_size=0.8, random_state=1000)
    x_train = np.asarray(x_train)
    y_train = np.asarray(y_train)
    x_test = np.asarray(x_test)
    y_test = np.asarray(y_test)

    model.fit(x_train, y_train, batch_size=batch_size, epochs=15, validation_split=0.1)
    loss, accuracy, f1, precision, recall = model.evaluate(x_test, y_test, verbose=0)
    print()
    print('\n|', title, '|  |\n| ------------- | ------------- |')
    for v in [["Accuracy", accuracy], ["F1", f1], ["Precision", precision], ["Recall", recall]]:
        print(v[0], '|', v[1], '|')
    print()
    with open('plots\\results.txt', 'a') as file:
        file.writelines(title + ' ann' "\n")
        file.writelines("Recall:" + str(recall) + "\n")
        file.writelines("F1:" + str(f1) + "\n")
        file.writelines("Precision:" + str(precision) + "\n")
        file.writelines("Accuracy:" + str(accuracy) + "\n")
        file.writelines("\n")
