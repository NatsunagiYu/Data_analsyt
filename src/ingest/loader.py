import pandas as pd

def load_csv(path : str) -> pd.DataFrame :
    df = pd.read_csv (
        path,
        parse_dates=["InvoiceDate"],
        dtype = {
            "InvoiceNo" : "string",
            "StockCode" : "string",
            "Country"   : "string"
        }
    )
    return df