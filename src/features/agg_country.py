import pandas as pd
from src.features.agg_product import product_feature

def country_feature ( df : pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    df_pro = df[df['type']== 'PRODUCT']

    agg = df_pro.groupby(['Country','StockCode']).agg(
        net_gmv = ('net_gmv','sum'),
        solds_unit = ('Quantity','sum'),
        orders = ('InvoiceNo','nunique')
    ).reset_index()

    return agg