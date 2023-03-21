def transform(df):
    """
    Transform data
    Aggregate and prepare datatypes
    """
    dfti = df.copy()
    dfti.dropna()
    # aggregate by gender
    agg1 = dfti.groupby('gender', as_index=False)\
        .agg({"id": "count"})\
        .rename(columns={'id': 'count'})
    agg1['gender'] = agg1['gender'].astype(str)
    agg1['count'] = agg1['count'].astype(int)
    agg1.info()
    return agg1