import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
import numpy as np
from statsmodels.tsa.stattools import adfuller

cn = pd.read_csv("data/cryptonews.csv")
bp = pd.read_csv("data/btc.csv")

cn["date"] = pd.to_datetime(cn["date"], format='mixed', errors='coerce').dt.date
bp["Date"] = pd.to_datetime(bp["Date"]).dt.date

start_date = cn["date"].min()
end_date = cn["date"].max()

bp_filtered = bp[(bp["Date"] >= start_date) & (bp["Date"] <= end_date)]
test = np.array(bp_filtered["Open"].reset_index()["Open"])
gaus = np.array(gaussian_filter1d(test, 5))
test = test - gaus
print("p-value ", adfuller(test)[1])

fig, ax1 = plt.subplots(figsize=(10, 6))

# ax1.hist(cn["date"], bins=26, alpha=0.6,)
# ax1.set_xlabel('Date')
# ax1.set_ylabel("Amount of News Articles")

ax2 = ax1.twinx()
ax2.plot(bp_filtered["Date"], bp_filtered["Open"], label="BTC Price")
ax2.plot(bp_filtered["Date"], gaus, label="Gaussian_filtered BTC Price")
ax2.plot(bp_filtered["Date"], test, label="Trend Removed")
ax2.legend()
ax2.set_ylabel("BTC Price")

fig.tight_layout()

plt.show()
