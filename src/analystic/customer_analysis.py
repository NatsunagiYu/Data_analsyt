import pandas as pd

def customer_concentration (df : pd.DataFrame):

    df = df.copy()

    df = df.sort_values('total_gmv', ascending = False)

    total_revenue = df['total_gmv'].sum()

    df['rank'] = range(1, len(df) + 1)

    top10_ratio = df[df['rank'] <= 10]['total_gmv'].sum()/ total_revenue
    top20_ratio = df[df['rank'] <= 20]['total_gmv'].sum()/ total_revenue
    return {
        "top10_ratio" : top10_ratio,
        "top20_ratio" : top20_ratio,
        "total_revenue" : total_revenue
    }


def repeat_pruchase (df : pd.DataFrame) :

    total_customer = len(df)
    total_repeat = len(df[df['orders'] >=2 ])

    return total_repeat/total_customer * 100