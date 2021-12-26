import collections
import datetime

import util
from tabulate import tabulate
import os
from collections import Counter
import numpy as np
from scipy import spatial
from tqdm import tqdm
import textwrap
import pickle


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


def main():
    query_str = "קרונה COVID חיסונים מחלימים חיסון שלישי בוסטר מתחסנים הקורונה מחלה בדיקות סגר חולים"
    docs_files = ['data\\' + file for file in os.listdir('data') if file.endswith(".txt")]
    all_files = docs_files

    files_words = {}
    all_words = query_str.split()
    for file in tqdm(all_files):
        files_words[file] = make_dictionary(file)
        all_words += make_dictionary(file)
    files_words["Query"] = query_str.split()
    all_words = Counter(all_words).most_common()

    with open('1.pkl', 'wb') as f:
        pickle.dump(query_str, f)
        pickle.dump(all_files, f)
        pickle.dump(files_words, f)
        pickle.dump(all_words, f)

    all_words_temp = []
    for word in tqdm(all_words):
        if word[1] > 111 and len(word[0]) > 1 and word[0] not in util.get_stop_words():
            all_words_temp += [word[0]]
    all_words = all_words_temp

    with open('2.pkl', 'wb') as f:
        pickle.dump(all_words_temp, f)

    avdl = np.average([len(bow) for bow in list(files_words.values())])
    IDF = calculate_IDF(all_words, list(files_words.values()))

    with open('3.pkl', 'wb') as f:
        pickle.dump(avdl, f)
        pickle.dump(IDF, f)

    cosine_distances = []
    euclidean_distances = []
    jaccard_distances = []
    query_TF_IDF = calculate_TF_IDF(all_words, calculateTF(all_words, list(files_words.get("Query")), avdl), IDF)
    for file in tqdm(files_words):
        if file != "Query":
            doc_TF_IDF = calculate_TF_IDF(all_words, calculateTF(all_words, files_words[file], avdl), IDF)
            cosine_distances.append([file, spatial.distance.cosine(query_TF_IDF, doc_TF_IDF)])
            euclidean_distances.append([file, spatial.distance.euclidean(query_TF_IDF, doc_TF_IDF)])
            jaccard_distances.append([file, jaccard_similarity(query_TF_IDF, doc_TF_IDF)])

    cosine_distances = sorted(cosine_distances, key=lambda x: x[1])
    cosine_distances = [it for it in cosine_distances if it[1] != 0]
    euclidean_distances = sorted(euclidean_distances, key=lambda x: x[1])
    euclidean_distances = [it for it in euclidean_distances if it[1] != 0]
    jaccard_distances = sorted(jaccard_distances, key=lambda x: x[1])
    jaccard_distances = [it for it in jaccard_distances if it[1] != 0]

    with open('4.pkl', 'wb') as f:
        pickle.dump(cosine_distances, f)
        pickle.dump(euclidean_distances, f)
        pickle.dump(jaccard_distances, f)

    print(tabulate(cosine_distances[:10], headers=['file', 'cosine distances'], tablefmt='fancy_grid'))
    print(tabulate(euclidean_distances[:10], headers=['file', 'euclidean distances'], tablefmt='fancy_grid'))
    print(tabulate(jaccard_distances[:10], headers=['file', 'euclidean distances'], tablefmt='fancy_grid'))


if __name__ == '__main__':
    tic = datetime.datetime.now()
    main()
    toc = datetime.datetime.now()
    print('\n' + str((toc - tic)))
