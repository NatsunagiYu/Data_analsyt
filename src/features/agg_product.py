import pandas as pd

def product_feature (df : pd.DataFrame ) -> pd.DataFrame :

    df = df.copy()

    df_pro = df[df['type'] == "PRODUCT"]

    agg = df_pro.groupby("StockCode").agg(
        net_gmv = ("net_gmv" , "sum"),
        solds_unit = ("Quantity" , "sum"),
        orders = ("InvoiceNo", "nunique"),
        avg_price = ("UnitPrice", "mean")
    ).reset_index()


    df_return = df[df["is_return"] == True]

    return_form = df_return.groupby("StockCode").agg(
        return_unit = ("abs_quantity", "sum")
    ).reset_index()

    agg = agg.merge(return_form, on="StockCode", how="left")
    agg["return_unit"] = agg["return_unit"].fillna(0)

    agg["return_rate"] = agg["return_unit"] * 100 / agg["solds_unit"]
    return agg