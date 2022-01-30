import copy
from sentence_transformers import SentenceTransformer
import pandas as pd


def BERT(docs):
    docs = copy.deepcopy(docs)
    BERT_model = SentenceTransformer('bert-base-nli-mean-tokens')
    return pd.DataFrame(BERT_model.encode(list(docs.values()))), docs.keys()

