import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

cn = pd.read_csv("data/cryptonews.csv")
bp = pd.read_csv("data/btc.csv")
# print(bp["date"][])
data = []

for x in [cn["date"][0], cn["date"][1]]:
    data.append(int(datetime.strptime(x.split()[0], "%Y-%m-%d").timestamp()))

print(data)

# figure=plt.figure(figsize=(8,8))
# height, _, _ = plt.hist(data, 25, density=True)
# plt.show()