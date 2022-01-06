import os
from collections import Counter
from zipfile import ZipFile
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


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
    bow = [word for word, count in bow if count > min_word_count and len(word) >= 2 and word not in stop_words][:max_size]
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


def plot_kmeans(df, real_symbols, title):
    print("[LOG] Ploting", title)
    _scalar = StandardScaler()
    _scalar.fit(df)
    print("starting k-means")
    kmeans_scale = KMeans(n_clusters=2).fit(df)
    labels_scale = kmeans_scale.labels_
    pca_features = PCA(n_components=2).fit(df).transform(df)

    plt.figure(figsize=(10, 10))
    sns.scatterplot(pca_features[:, 0], pca_features[:, 1],
                    palette='Set1',
                    hue=labels_scale,
                    s=100, alpha=0.2).set_title(title, fontsize=15)
    plt.legend()
    plt.ylabel('PC2')
    plt.xlabel('PC1')
    plt.savefig('plots\\' + title + '.png')

    title += ' real'
    plt.figure(figsize=(10, 10))
    sns.scatterplot(pca_features[:, 0], pca_features[:, 1],
                    palette='Set1',
                    hue=real_symbols,
                    s=100, alpha=0.2).set_title(title, fontsize=15)
    plt.legend()
    plt.ylabel('PC2')
    plt.xlabel('PC1')
    plt.savefig('plots\\' + title + '.png')


def get_stop_words():
    words = []
    with open('heb_stopwords.txt', 'r', encoding='utf-8') as f:
        for line in f:
            words += line.split()
    return words

