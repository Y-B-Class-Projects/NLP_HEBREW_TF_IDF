import datetime
import copy
import nltk

from BERT import BERT
from utils import *
from tfidf import TF_IFD
from doc2vec import doc2vec
import os


def vectors_classification(x_vectors, y, title):
    k_means_res = kmeans(x_vectors, y, title)
    ann_res = ann(x_vectors, y)
    print_results_table(title, k_means_res, ann_res)


def EX_3_2_code():
    folders = ['docs\\Clean_Punctuation\\', 'docs\\prefSufWord\\', 'docs\\rootWord\\']
    query_str = "חמאס מלחמה עזה טיל טילים פלסטינים"

    for folder in folders:
        docs_files = [folder + file for file in os.listdir(folder) if file.endswith(".txt")]
        docs = read_files(docs_files)
        # We used these lines to print and copy the results to README.
        print_README_table(TF_IFD(copy.deepcopy(docs), False, query_str)[:10])
        print_README_table(doc2vec(copy.deepcopy(docs), query_str, n_top_docs=10, is_matrix_mode=False))


def EX_4_code():
    open('plots\\results.txt', 'w+').close()
    folders = ['docs\\Clean_Punctuation\\', 'docs\\prefSufWord\\', 'docs\\rootWord\\']
    groups = [['A', 'B'], ['A', 'C'], ['C', 'B']]
    max_vector_size = 1000

    for group in groups:
        groups_docs = {}
        for symbol in group:
            groups_docs = {**groups_docs, **{str(doc): symbol for doc in my_csv(symbol)}}

        for folder in folders:
            title = ', '.join(group) + ' ' + folder.split('\\')[1]
            print(title)
            docs_locations = [folder + file for file in os.listdir(folder) if get_file_name(file) in groups_docs.keys()]
            docs = read_files(docs_locations)

            # TF_IFD classification
            TF_IFD_vectors, doc_locations = TF_IFD(docs, max_bow_size=max_vector_size)
            real_symbols = [groups_docs[get_file_name(doc)] for doc in doc_locations]
            vectors_classification(TF_IFD_vectors, real_symbols, title + ' TF-IDF')

            # doc2vec classification
            doc2vec_vector, doc_locations = doc2vec(docs)
            real_symbols = [groups_docs[get_file_name(doc)] for doc in doc_locations]
            vectors_classification(doc2vec_vector, real_symbols, title + ' doc2vec')

            # BERT classification
            BERT_vector, doc_locations = BERT(docs)
            real_symbols = [groups_docs[get_file_name(doc)] for doc in doc_locations]
            vectors_classification(BERT_vector, real_symbols, title + ' BERT')


def main():
    """
    Since this exercise is an exercise that is divided into several sub-exercises, we built a separate function for
    each sub-exercise.
    """
    # EX_3_2_code()
    EX_4_code()


if __name__ == '__main__':
    nltk.download('punkt')
    # my_unzip(my_csv())    # for the first time you need to unzip all docs.
    tic = datetime.datetime.now()
    main()
    toc = datetime.datetime.now()
    print('\n' + str((toc - tic)))
