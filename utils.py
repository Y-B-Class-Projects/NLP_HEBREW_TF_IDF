import os
import shutil
from collections import Counter
from zipfile import ZipFile

import matplotlib
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from keras.models import Sequential
from keras.layers import Dense
from keras import backend as K
from sklearn.model_selection import train_test_split
import numpy as np
import dataframe_image as dfi


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


def plot_results(pca_features, predict, real_symbols, title):
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


def kmeans(df, real_symbols, title):
    print("[LOG] Ploting", title)
    symbols_names = list(set(real_symbols))
    _scalar = StandardScaler()
    _scalar.fit(df)
    print("[LOG] starting k-means")
    kmeans_scale = KMeans(n_clusters=2).fit(df)
    labels_scale = kmeans_scale.labels_
    mapping_option_01 = {0: symbols_names[0], 1: symbols_names[-1]}
    mapping_option_02 = {0: symbols_names[-1], 1: symbols_names[0]}
    predict_option_01 = [mapping_option_01[i] for i in labels_scale]
    predict_option_02 = [mapping_option_02[i] for i in labels_scale]
    pca_features = PCA(n_components=2).fit(df).transform(df)

    accuracy_option_01 = str(accuracy_score(real_symbols, predict_option_01))
    accuracy_option_02 = str(accuracy_score(real_symbols, predict_option_02))

    if accuracy_option_01 >= accuracy_option_02:
        accuracy = accuracy_option_01
        predict = predict_option_01
    else:
        accuracy = accuracy_option_02
        predict = predict_option_02

    f1_option_01 = str(f1_score(real_symbols, predict, pos_label=symbols_names[0]))
    f1_option_02 = str(f1_score(real_symbols, predict, pos_label=symbols_names[-1]))

    if f1_option_01 >= f1_option_02:
        f1 = f1_option_01
        pos_label = symbols_names[0]
    else:
        f1 = f1_option_02
        pos_label = symbols_names[-1]

    precision = str(precision_score(real_symbols, predict, pos_label=pos_label))
    recall = str(recall_score(real_symbols, predict, pos_label=pos_label))

    plot_results(pca_features, predict, real_symbols, title)
    return [accuracy, f1, precision, recall]


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


def split_data(x_data, y_data):
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, train_size=0.8, random_state=1000)
    return np.asarray(x_train), np.asarray(y_train), np.asarray(x_test), np.asarray(y_test)


def ann(x_data, y_data, batch_size=128, title=''):
    mapping = {'A': 0, 'B': 1, 'C': 2}
    y_data = [mapping[i] for i in y_data]

    x_train, y_train, x_test, y_test = split_data(x_data, y_data)
    ann_model = Sequential()
    ann_model.add(Dense(10, activation='relu'))
    ann_model.add(Dense(10, activation='relu'))
    ann_model.add(Dense(7, activation='relu'))
    ann_model.add(Dense(1, activation='sigmoid'))
    ann_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc', f1_m, precision_m, recall_m])
    ann_model.fit(x_train, y_train, batch_size=batch_size, epochs=15, validation_split=0.1)
    loss, accuracy, f1, precision, recall = ann_model.evaluate(x_test, y_test)

    return [accuracy, f1, precision, recall]


def symbols_docs_to_folders(folders):
    for folder in folders:
        for symbol in ['A', 'B', 'C']:
            dst_folder = folder.replace('docs', 'symboled_docs') + symbol
            os.makedirs(dst_folder, exist_ok=True)
            for doc in tqdm(my_csv(symbol)):
                add_str = ''
                if folder == 'docs\\prefSufWord\\':
                    add_str = 'prefsuf'
                elif folder == 'docs\\rootWord\\':
                    add_str = 'root'
                doc_str = str(doc) + add_str + ".txt"
                src = folder + doc_str
                dst = dst_folder + "\\" + doc_str
                if not os.path.exists(dst):
                    shutil.copyfile(src, dst)
        print()


def print_results_table(title, k_means_res, ann_res):
    with open('plots\\results.txt', 'a') as file:
        print()
        file.writelines("\n")
        first_line = '\n| ' + title + ' | k-means | ANN |\n| ------------- | ------------- | ------------- | '
        print(first_line)
        file.writelines(first_line)
        for table_line in [["Accuracy", k_means_res[0], ann_res[0]], ["F1", k_means_res[1], ann_res[1]],
                           ["Precision", k_means_res[2], ann_res[2]], ["Recall", k_means_res[3], ann_res[3]]]:
            line = '\n' + str(table_line[0]) + ' | ' + str(table_line[1]) + ' | ' + str(table_line[2]) + ' | '
            print(line)
            file.writelines(line)
        print()
        file.writelines("\n")

    k_means_res = ["{:.2%}".format(float(num)) for num in k_means_res]
    ann_res = ["{:.2%}".format(float(num)) for num in ann_res]

    df = pd.DataFrame({'k-means': k_means_res, 'ANN': ann_res})
    df.index = ['Accuracy', 'F1', 'Precision', 'Recall']
    df.columns.name = title
    dfi.export(df, 'plots\\' + title + '_table.jpeg', fontsize=20, table_conversion=matplotlib)
