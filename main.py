import collections
import datetime
from zipfile import ZipFile
from tabulate import tabulate
import os
from collections import Counter
import numpy as np
from tqdm import tqdm
import pickle
import pandas as pd
from scipy.spatial import distance


def make_dictionary(file):
    words = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            words += line.split()
    return words


def calculateTF(wordset, bow, avdl):
    b = 0.75
    termfreq_diz = dict.fromkeys(wordset, 0)
    counter1 = dict(collections.Counter(bow))
    for w in bow:
        termfreq_diz[w] = counter1[w] / ((1 - b) + b * len(bow) / avdl)
    return termfreq_diz


def calculate_IDF(wordset, bow):
    d_bow = {'bow_{}'.format(i): list(set(b)) for i, b in enumerate(bow)}
    N = len(d_bow.keys())
    l_bow = []
    for b in d_bow.values():
        l_bow += b
    counter = dict(collections.Counter(l_bow))
    idf_diz = dict.fromkeys(wordset, 0)
    for w in wordset:
        idf_diz[w] = np.log((1 + N) / (1 + counter[w])) + 1
    return idf_diz


def calculate_TF_IDF(wordset, tf_diz, idf_diz):
    tf_idf_diz = dict.fromkeys(wordset, 0)
    for w in wordset:
        tf_idf_diz[w] = tf_diz[w] * idf_diz[w]
    tdidf_values = list(tf_idf_diz.values())
    return tdidf_values


def jaccard_similarity(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(set(list1)) + len(set(list2))) - intersection
    return float(intersection) / union


def create_cosine_distances_matrix(query_str, docs_files):
    files_words = {}
    all_words = query_str.split()
    for file in tqdm(docs_files):
        files_words[file] = make_dictionary(file)
        all_words += make_dictionary(file)
    files_words["Query"] = query_str.split()
    all_words = Counter(all_words).most_common()

    all_words_temp = []
    for word in tqdm(all_words):
        if word[1] > 100 and len(word[0]) > 1:
            all_words_temp += [word[0]]
    all_words = all_words_temp

    avdl = np.average([len(bow) for bow in list(files_words.values())])
    IDF = calculate_IDF(all_words, list(files_words.values()))

    cosine_distances = []
    query_TF_IDF = calculate_TF_IDF(all_words, calculateTF(all_words, list(files_words.get("Query")), avdl), IDF)
    for file in tqdm(files_words):
        if file != "Query":
            doc_TF_IDF = calculate_TF_IDF(all_words, calculateTF(all_words, files_words[file], avdl), IDF)
            cosine_distances.append([file, distance.cosine(query_TF_IDF, doc_TF_IDF)])

    cosine_distances = sorted(cosine_distances, key=lambda x: x[1])
    cosine_distances = [it for it in cosine_distances if it[1] != 0]

    print(tabulate(cosine_distances[:10], headers=['file', 'cosine distances'], tablefmt='fancy_grid'))

    print('\n| file | cosine distances |\n| ------------- | ------------- |')
    for doc in cosine_distances[:10]:
        print('| [', doc[0].split('\\')[2], '](docs/Clean_Punctuation/', doc[0].split('\\')[2].replace("root", "").replace("prefsuf", ""), ')|', doc[1], '|',
              sep="")
    return cosine_distances


def my_unzip(docs_list):
    index = 0
    with ZipFile('Clean_Punctuation.zip', 'r') as zipObj:
        listOfFileNames = ["Clean_Punctuation/" + str(n) + ".txt" for n in docs_list]
        for fileName in listOfFileNames:
            zipObj.extract(fileName, 'docs')
            index += 1


def my_csv():
    pd.options.display.max_rows = 102
    df = pd.read_csv('data.csv', names=["doc", "type"])
    my_docs = df["doc"].tolist()
    my_docs.sort()
    return my_docs


def main():
    folders = ['docs\\Clean_Punctuation\\', 'docs\\prefSufWord\\', 'docs\\rootWord\\']
    query_str = "חמאס מלחמה עזה טיל טילים פלסטינים"

    cosine_distances_matrixs = []

    for folder in folders:
        docs_files = [folder + file for file in os.listdir(folder) if file.endswith(".txt")]
        _matrix = create_cosine_distances_matrix(query_str, docs_files)
        cosine_distances_matrixs.append(["TF-IDF, " + folder, _matrix])

    print()


if __name__ == '__main__':
    # my_unzip(my_csv())
    tic = datetime.datetime.now()
    main()
    toc = datetime.datetime.now()
    print('\n' + str((toc - tic)))
