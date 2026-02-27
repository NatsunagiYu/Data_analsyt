import pandas as pd

def customer_feature (df : pd.DataFrame) -> pd.DataFrame :
    df = df.copy()

    df_pro = df[df['type'] == 'PRODUCT']

    agg = df_pro.groupby('CustomerId').agg(
        total_gmv = ('net_gmv', 'sum'),
        total_unit = ('Quantity', 'sum'),
        last_purchase = ('InvoiceDate', 'Max'),
        orders = ('InvoiceNo', 'nunqiue')
    ).reset_index()
    
    return agg