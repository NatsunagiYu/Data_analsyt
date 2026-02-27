import pandas as pd

def get_n_days (df : pd.DataFrame, days : int) -> pd.DataFrame :

    df = df.copy()

    max_date = df['InvoiceDate'].max()
    cut = max_date - pd.Timedelta(days=days)

    df = df[df['InvoiceDate'] >= cut]

    return df