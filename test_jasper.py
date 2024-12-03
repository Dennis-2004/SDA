import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


# https://en.wikipedia.org/wiki/Spearman's_rank_correlation_coefficient
def spearman_correlation(rank1, rank2):
    n = len(rank1)

    sum_d_squared = sum([(rank1[i] - rank2[i])**2 for i in range(n)])
    correlation = 1 - ((6 * sum_d_squared) / (n * (n**2 - 1)))
    return correlation


# Read data
cn = pd.read_csv("data/cryptonews.csv")
bp = pd.read_csv("data/btc.csv")

# Convert the date to the datetime format
cn['date'] = pd.to_datetime(cn['date'], format='%Y-%m-%d %H:%M:%S')
bp['date'] = pd.to_datetime(bp['Date'], format='%Y-%m-%d')

# Only keep the year and months of the date
cn['year_month'] = cn['date'].dt.to_period('M')
bp['year_month'] = bp['date'].dt.to_period('M')

# Group data by the months
cn_monthly_count = cn.groupby('year_month').size().reset_index(name='Count')
bp_monthly_mean = bp.groupby('year_month')[['Open']].mean().reset_index()

# Calculate ranks
cn_rank = list(cn_monthly_count['Count'].rank())
bp_rank = list(bp_monthly_mean['Open'].rank())

correlation = spearman_correlation(cn_rank, bp_rank)
print(f"Spearman Correlation: {correlation:.3f}")
