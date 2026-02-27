import pandas as pd

def clean_data(df : pd.DataFrame) -> pd.DataFrame :

    df = df.copy()

    #raise message to inform elt, drop for testing
    df = df.dropna(subset = ['InvoiceNo', 'StockCode', 'UnitPrice', 'Quantity'])

    df = df[df['UnitPrice'] > 0]

    df['is_return'] = (df['StockCode'].str.upper().str.startswith("C", na=False) | df['Quantity'] < 0)

    df['line_gmv'] = df['UnitPrice'] * df['Quantity']

    df['net_gmv'] = df['line_gmv'].where(~df['is_return'],0)

    return df