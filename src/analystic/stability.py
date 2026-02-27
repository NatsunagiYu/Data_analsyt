import pandas as pd
from src.features.time_window import get_n_days
from src.analystic.topn import calculate_topn
from src.features.agg_product import product_feature

def jacc(setA , setB) :

    intersection = len(setA & setB)
    union = len(setA | setB)

    if union == 0:
        return  0
    
    return intersection / union * 100

def calculate_stability (df, n=50) :

    df30 = get_n_days(df,30)
    df60 = get_n_days(df,60)
    df90 = get_n_days(df,90)

    top30 = product_feature(calculate_topn(df30), n)['topn_table']
    top60 = product_feature(calculate_topn(df60), n)['topn_table']
    top90 = product_feature(calculate_topn(df90), n)['topn_table']

    set30 = set(top30['StockCode'])
    set60 = set(top60['StockCode'])
    set90 = set(top90['StockCode'])

    j_30_60 = jacc(set30, set60)
    j_60_90 = jacc(set60, set90)
    j_30_90 = jacc(set30, set90)
    return {
        "jaccard_30_60" : j_30_60,
        "jaccard_60_90" : j_60_90,
        "jaccard_30_90" : j_30_90,
        "top30" : top30,
        "top60" : top60,
        "top90" : top90
    }