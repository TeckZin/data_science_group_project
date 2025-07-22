import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# print("hello world")

# x = np.random.randn(50)
# y = np.random.randn(50)
#
# plt.figure(figsize=(8, 6))
# plt.scatter(x, y, alpha=0.6)
# plt.xlabel('X values')
# plt.ylabel('Y values')
# plt.title('Scatter Plot')
# plt.show()
#


# Read CSV

print("Current working directory:", os.getcwd())


df = pd.read_csv("data/archive/all_stocks_5yr.csv")
# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])
#
# print(sorted(df['Name'].unique()))
#
# # (Optional) Filter for a specific stock if the CSV contains multiple tickers
# # df = df[df['Name'] == 'AAPL']  # Uncomment and change 'AAPL' to your stock symbol
#
# # Plot
# plt.figure(figsize=(12, 6))
# plt.plot(df['date'], df['close'], label='Close Price')
# plt.xlabel('Date')
# plt.ylabel('Price ($)')
# plt.title('Stock Close Price Over Time')
# plt.grid(True)
# plt.legend()
# plt.tight_layout()
# plt.show()


# Group by date and compute the average closing price across all companies
# sp500_daily_avg = df.groupby('date')['close'].mean().reset_index()
#
# # Plot
# plt.figure(figsize=(12, 6))
# plt.plot(sp500_daily_avg['date'], sp500_daily_avg['close'], label='Synthetic S&P 500')
# plt.xlabel('Date')
# plt.ylabel('Average Close Price ($)')
# plt.title('Synthetic S&P 500 Index (Equal-Weighted Average)')
# plt.grid(True)
# plt.legend()
# plt.tight_layout()
# plt.show()
#

df_2 = pd.read_csv("data/archive_1/SP500.csv")
# Convert 'date' column to datetime format
df_2['date'] = pd.to_datetime(df_2['observation_date'])



plt.style.use('ggplot')  # Try other styles too: 'ggplot', 'fivethirtyeight', 'bmh', etc.

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(df_2['date'], df_2['SP500'], label='S&P 500', color='steelblue', linewidth=2)

# Beautify labels and title
ax.set_xlabel('Date', fontsize=14, labelpad=10)
ax.set_ylabel('Price (USD)', fontsize=14, labelpad=10)
ax.set_title('S&P 500 Price Over Time', fontsize=18, weight='bold', pad=15)

# Improve tick formatting
ax.tick_params(axis='both', which='major', labelsize=12)
fig.autofmt_xdate()  # Auto-rotate date labels

# Add subtle grid and legend
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(fontsize=12, loc='upper left')

plt.tight_layout()
plt.show()
