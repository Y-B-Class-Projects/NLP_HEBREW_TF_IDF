import copy
from sentence_transformers import SentenceTransformer
import pandas as pd


def BERT(docs):
    print("[LOG] Calculating BERT")
    docs = copy.deepcopy(docs)
    docs = {loc: words for loc, words in docs.items() if len(words) >= 1}
    BERT_model = SentenceTransformer('bert-base-nli-mean-tokens')
    BERT_vectors = BERT_model.encode(list(docs.values()), show_progress_bar=True)
    return pd.DataFrame(BERT_vectors), docs.keys()
