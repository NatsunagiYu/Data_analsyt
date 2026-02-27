import pandas as pd

def country_topn (df : pd.DataFrame, n = 50):

    country_result ={}

    countries = df['Country'].unique()

    for country in countries:
        
        df_country = df[df['Country'] == country]

        if len(country) == 0:
            continue

        df_country = df_country.sort_values('net_gmv', ascending = False)
        df_country['rank'] = range(1, len(df_country)+1)

        topn = df_country[df_country['rank'] <= n]

        total_gmv = df_country['net_gmv'].sum()
        total_top = topn['net_gmv'].sum()

        if total_gmv > 0:    
            coverage = total_top/total_gmv * 100
        else :
            coverage = 0

        country_result[country] = {
            "topn_table" : topn,
            "coverage" : coverage,
            "total_gmv" : total_gmv
        }

    return country_result