import pandas as pd

# Read the Market Trend CSV file
market_trend_df = pd.read_csv(r'C:\BTEC\ASM\Market_Trend.csv')

# Kiểm tra định dạng ngày tháng
market_trend_df['trend_start_date'] = pd.to_datetime(market_trend_df['trend_start_date'], errors='coerce')
