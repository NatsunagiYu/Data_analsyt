import pandas as pd

def calculate_topn(df_product : pd.DataFrame, n: int = 50) :

    df = df_product.copy()
    df = df.sort_values("net_gmv", ascending = False)

    df['rank'] = range(1,len(df)+1)
    df_topn = df[df['rank'] <= n]

    total_gmv = df_product['net_gmv'].sum()
    total_topn_gmv = df_topn['ne_gmv'].sum()

    coverage_ratio = total_topn_gmv/ total_gmv *100

    return {
        "topn_table" : df_topn,
        "topn_ratio" : coverage_ratio,
        "total_gmv"  : total_gmv,
        "total_topn_gmv" : total_topn_gmv
    } 