import pandas as pd

def classify_transaction (row) :

    invoice = str(row['InvoiceNo']).upper()
    des   = str(row.get("Description","")).upper()

    if invoice.startswith("C"):
        return "RETURN"
    
    if "MANUAL" in des:
        return "MANUAL"
    
    if "POSTAGE" in des:
        return "POSTAGE"
    
    if "DISCOUNT" in des:
        return "DISCOUNT"
    
    if "SAMPLES" in des:
        return "SAMPLES"
    
    return "PRODUCT"

def clean_data(df : pd.DataFrame) -> pd.DataFrame :

    df = df.copy()

    #raise message to inform elt, drop for testing
    df = df.dropna(subset = ['InvoiceNo', 'StockCode', 'UnitPrice', 'Quantity'])
    df = df[df['UnitPrice'] > 0]

    df['type'] = df.apply(classify_transaction, axis=1)
    df['is_return'] = (df['type'] == "RETURN"| df['Quantity'] < 0)


    df['line_gmv'] = df['UnitPrice'] * df['Quantity']
    df['net_gmv'] = df['line_gmv'].where((df['type'] == "PRODUCT") & (df['Quantity'] > 0),0)
    df['return_value'] = df['line_gmv'].where(df['is_return'],0)

    df['order_date'] = df['InvoiceDate'].dt.date
    df['month'] = df['InvoiceDate'].dt.to_period("M")

    df['abs_quantity'] = df["Quantity"].abs()
    
    return df