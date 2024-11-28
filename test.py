import pandas as pd
import matplotlib.pyplot as plt

cn = pd.read_csv("data/cryptonews.csv")
bp = pd.read_csv("data/btc.csv")

cn["date"] = pd.to_datetime(cn["date"], format='mixed', errors='coerce').dt.date

bp["Date"] = pd.to_datetime(bp["Date"]).dt.date

start_date = cn["date"].min()
end_date = cn["date"].max()

bp_filtered = bp[(bp["Date"] >= start_date) & (bp["Date"] <= end_date)]


fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.hist(cn["date"], bins=26, alpha=0.6,)
ax1.set_xlabel('Date')
ax1.set_ylabel("Amount of News Articles")

ax2 = ax1.twinx()
ax2.plot(bp_filtered["Date"], bp_filtered["Open"], color="orange")
ax2.set_ylabel("BTC Price")

fig.tight_layout()

plt.show()
