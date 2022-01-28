import math
from scipy.spatial import distance
from utils import *
import numpy as np


def calculateTF(doc, bow, avg_doc_length):
    """
    :param doc: vector of words from some document.
    :param bow: bag of words, vector of all words in the language.
    :param avg_doc_length: avg doc length (used for the normalization).
    :return: dictionary of normalized word-frequency = for each word in the 'bow' how many times it appears in 'doc'.
    """
    b = 0.75
    normalize_val = (1 - b + b * len(doc) / avg_doc_length)
    tf = dict.fromkeys(bow, 0)
    _counter = dict(Counter(doc))
    for w in bow:
        if w in _counter:
            tf[w] = _counter[w] / normalize_val
    return tf


def calculateDF(docs, bow):
    """
    :param docs: dictionary of documents - {doc_location: doc_words}.
    :param bow: bag of words, vector of all words in the language.
    :return: dictionary of doc-frequency = for each word the total number of docs containing this word.
    """
    print("[LOG] (Calculating DF)")
    return {word: sum([1 for doc in docs if word in doc]) for word in tqdm(bow)}


def calculate_IDF(docs, bow):
    """
    :param docs: list of documents, each document is a vector of words.
    :param bow: bag of words, vector of all words in the language.
    :return: dictionary of normalized IDF vector for etch word in 'bow'.
    """
    print("[LOG] (Calculating IDF)")
    N = len(docs)
    df = calculateDF(docs, bow)
    idf = dict.fromkeys(bow, 0)
    for w in tqdm(bow):
        idf[w] = math.log((1 + N) / (1 + df[w])) + 1
    return idf


def calculate_doc_TF_IDF(doc_tf, idf, bow):
    """
    :param doc_tf: tf-vector of the doc.
    :param idf: idf vector of all the docs.
    :param bow: bag of words, vector of all words in the language.
    :return: tf-idf vector of single document.
    """
    tf_idf = dict.fromkeys(bow, 0)
    for w in bow:
        tf_idf[w] = doc_tf[w] * idf[w]
    return tf_idf


def TF_IFD(docs, is_matrix_mode=True, query='', max_bow_size=100):
    """
    :param docs: dictionary of documents - {doc_location: doc_words}.
    :param is_matrix_mode: if True the function will return tf-idf-matrix, otherwise the function will return the cosine
    distance matrix of all documents to the 'query'.
    :param query: needed only for 'is_matrix_mode' = False.
    :param max_bow_size: max bag-of-words size.
    :return:
    """
    print("[LOG] Calculating TF-IDF")
    if not is_matrix_mode:
        docs['query'] = query.split()
    bow = get_bow(docs, max_bow_size)
    if not is_matrix_mode:
        bow += query.split()
        bow = list(set(bow))    # remove duplicates.
    avg_doc_length = np.average([len(words) for words in docs.values()])
    idf = calculate_IDF(docs.values(), bow)
    TF_IFD_matrix = pd.DataFrame()
    cosine_similarity = []

    if not is_matrix_mode:
        query_tf = calculateTF(docs['query'], bow, avg_doc_length)
        query_tf_idf = calculate_doc_TF_IDF(query_tf, idf, bow)

    for doc_name, doc_words in tqdm(docs.items()):
        doc_tf = calculateTF(doc_words, bow, avg_doc_length)
        doc_tf_idf = calculate_doc_TF_IDF(doc_tf, idf, bow)
        if is_matrix_mode:
            doc_tf_idf['doc_name'] = doc_name
            TF_IFD_matrix = TF_IFD_matrix.append(doc_tf_idf, ignore_index=True)
        else:
            cosine_similarity.append([doc_name, 1 - distance.cosine(pd.Series(query_tf_idf), pd.Series(doc_tf_idf))])

    if is_matrix_mode:
        return TF_IFD_matrix
    else:
        cosine_similarity = sorted(cosine_similarity, key=lambda x: x[1], reverse=True)
        cosine_similarity = [it for it in cosine_similarity if it[1] != 1]
        return cosine_similarity