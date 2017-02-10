"""
Method:         Heatmap
Data Variables: 2 type variables:
Columns - type list
Labels - type list(legend of chart)
Author:         Rodionova Anastasia
"""

import numpy as np
import seaborn as sns
import pandas as pd


def plot_heatmap(df, pivot):
    if size(pivot) == 3 & set(pivot) <= set(df.columns.values):
        df = df.pivot(pivot[0], pivot[1], pivot[2])
        ax = sns.heatmap(df, annot=True, fmt="d")


flights = sns.load_dataset("flights")
pivot = ["month", "year", "passengers"]

plot_heatmap(flights, pivot)
