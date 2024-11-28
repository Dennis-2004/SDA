import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv("data/cryptonews.csv")
data = []

for x in df["date"]:
    data.append(int(datetime.strptime(x.split()[0], "%Y-%m-%d").timestamp()))

figure=plt.figure(figsize=(8,8))
height, _, _ = plt.hist(data, 25, density=True)
plt.show()

