import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print("Current working directory:", os.getcwd())

df_2 = pd.read_csv("data/archive_1/SP500.csv")
df_2['date'] = pd.to_datetime(df_2['observation_date'])
df_2.rename(columns={'SP500': 'sp500'}, inplace=True)

df_mutual = pd.read_csv("data/mutual/MutualFundsData.csv")
df_mutual['Date'] = pd.to_datetime(df_mutual['Date'])

plt.style.use('fivethirtyeight')

fig, ax = plt.subplots(figsize=(14, 7))
ax.plot(df_2['date'], df_2['sp500'], label='S&P 500', color='steelblue', linewidth=2)

ax.set_xlabel('Date', fontsize=14, labelpad=10)
ax.set_ylabel('Price (USD)', fontsize=14, labelpad=10)
ax.set_title('S&P 500 Price Over Time', fontsize=18, weight='bold', pad=15)
ax.tick_params(axis='both', which='major', labelsize=12)
fig.autofmt_xdate()
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(fontsize=12, loc='upper left')

plt.tight_layout()
plt.show()

df_2 = df_2.set_index('date')
df_mutual = df_mutual.set_index('Date')

common_start = max(df_2.index.min(), df_mutual.index.min())
common_end = min(df_2.index.max(), df_mutual.index.max())

df_2 = df_2.loc[common_start:common_end]
df_mutual = df_mutual.loc[common_start:common_end]

df_2['sp500_norm'] = (1 + df_2['sp500'].pct_change().fillna(0)).cumprod()
df_mutual['mutual_norm'] = (1 + df_mutual['Return'].fillna(0)).cumprod()

plt.style.use('fivethirtyeight')

fig, ax = plt.subplots(figsize=(14, 7))
ax.plot(df_2.index, df_2['sp500_norm'], label='S&P 500 (Normalized)', color='steelblue', linewidth=2)
ax.plot(df_mutual.index, df_mutual['mutual_norm'], label='Mutual Fund (Normalized)', color='darkorange', linewidth=2)

ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Normalized Growth', fontsize=14)
ax.set_title('Performance Comparison: Mutual Fund vs S&P 500', fontsize=18, weight='bold')
ax.tick_params(axis='both', which='major', labelsize=12)
fig.autofmt_xdate()
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(fontsize=12, loc='upper left')

plt.tight_layout()
plt.show()


# Load CSVs
import pandas as pd
import matplotlib.pyplot as plt

# Load CSVs from correct path
nasdaq = pd.read_csv("data/archive_4/NASDAQ_100.csv", parse_dates=['date'])
qqq = pd.read_csv("data/archive_4/QQQ_split_adj.csv", parse_dates=['date'])
spy = pd.read_csv("data/archive_4/SPY.csv", parse_dates=['date'])
sp500 = pd.read_csv("data/archive_4/SP500.csv", parse_dates=['date'])

# Set index to 'date'
nasdaq.set_index('date', inplace=True)
qqq.set_index('date', inplace=True)
spy.set_index('date', inplace=True)
sp500.set_index('date', inplace=True)

# Drop rows with missing 'close' values
nasdaq = nasdaq[['close']].dropna()
qqq = qqq[['close']].dropna()
spy = spy[['close']].dropna()
sp500 = sp500[['close']].dropna()

# Align all by common date range
start_date = max(df.index.min() for df in [nasdaq, qqq, spy, sp500])
end_date = min(df.index.max() for df in [nasdaq, qqq, spy, sp500])

nasdaq = nasdaq.loc[start_date:end_date]
qqq = qqq.loc[start_date:end_date]
spy = spy.loc[start_date:end_date]
sp500 = sp500.loc[start_date:end_date]

# Compute return ratios
nasdaq['return'] = nasdaq['close'] / nasdaq['close'].iloc[0]
qqq['return'] = qqq['close'] / qqq['close'].iloc[0]
spy['return'] = spy['close'] / spy['close'].iloc[0]
sp500['return'] = sp500['close'] / sp500['close'].iloc[0]

# Plot return ratios
plt.style.use('fivethirtyeight')
plt.figure(figsize=(14, 7))

plt.plot(nasdaq.index, nasdaq['return'], label='NASDAQ 100', linewidth=1)
plt.plot(qqq.index, qqq['return'], label='QQQ', linewidth=1)
plt.plot(spy.index, spy['return'], label='SPY', linewidth=1)
plt.plot(sp500.index, sp500['return'], label='S&P 500', linewidth=1)

plt.title('Return Ratio (Relative to First Day)', fontsize=18, weight='bold')
plt.xlabel('Date', fontsize=14)
plt.ylabel('Return Ratio', fontsize=14)
plt.legend(fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

