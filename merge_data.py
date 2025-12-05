import pandas as pd

# 4개의 데이터 병합.
def merge_economic_data(oil, cpi, rate, unemployment):

    merged = pd.merge(oil, cpi, on="date", how="inner")
    merged = pd.merge(merged, rate, on="date", how="inner")
    merged = pd.merge(merged, unemployment, on="date", how="inner")

    merged = merged.sort_values("date").reset_index(drop=True)

    return merged