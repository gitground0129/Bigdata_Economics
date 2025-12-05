import pandas as pd

from preprocess import (preprocess_oil, preprocess_cpi, preprocess_rate, preprocess_unemployment)
from merge_data import merge_economic_data
from visualize import (plot_all_trends, plot_correlation_heatmap, plot_rate_vs_unemployment, plot_unemployment_scatter, save_all_plots)

# 한국은행 경제통계시스템 (ECOS) ( 유가 / 소비자물가지수 / 금리 / 실업률 )
oil_path = "data/국제상품가격_27151753.csv"
cpi_path = "data/소비자물가지수_27192439.csv"
rate_path = "data/한국은행 기준금리 및 여수신금리_27153917.csv"
unemployment_path = "data/경제활동인구_27192338.csv"

oil_df = pd.read_csv(oil_path, encoding='utf-8')
cpi_df = pd.read_csv(cpi_path, encoding='utf-8')
rate_df = pd.read_csv(rate_path, encoding='utf-8')
unemployment_df = pd.read_csv(unemployment_path, encoding='utf-8')

# 전처리 처리 (전처리 과정은 preproces.py 참고)
oil = preprocess_oil(oil_df)
cpi = preprocess_cpi(cpi_df)
rate = preprocess_rate(rate_df)
unemployment = preprocess_unemployment(unemployment_df)


print("=== OIL 전처리 결과 ===")
print(oil.head())
print(oil.info(), "\n")

print("=== CPI 전처리 결과 ===")
print(cpi.head())
print(cpi.info(), "\n")

print("=== RATE 전처리 결과 ===")
print(rate.head())
print(rate.info(), "\n")

print("=== UNEMPLOYMENT 전처리 결과 ===")
print(unemployment.head())
print(unemployment.info(), "\n")


merged = merge_economic_data(oil, cpi, rate, unemployment)

# 시각화
plot_all_trends(merged)
plot_correlation_heatmap(merged)
plot_rate_vs_unemployment(merged)
plot_unemployment_scatter(merged)


save_all_plots(merged)