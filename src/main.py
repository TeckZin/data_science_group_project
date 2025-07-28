import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print("Current working directory:", os.getcwd())

df_2 = pd.read_csv("data/archive_1/SP500.csv")
df_2['date'] = pd.to_datetime(df_2['observation_date'])
df_2.rename(columns={'SP500': 'sp500'}, inplace=True)

df_mutual = pd.read_csv("data/Mutual/MutualFundsData.csv")
df_mutual['Date'] = pd.to_datetime(df_mutual['Date'])

plt.style.use('ggplot')

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

