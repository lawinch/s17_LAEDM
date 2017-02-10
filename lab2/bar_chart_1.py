"""
Method:         Bar chart
Data Variables: 2 type variables:
DataFrame, 
Pivot - list of 3 columns name in data frame
Author:         Rodionova Anastasia
"""

import numpy as np
import seaborn as sns 
import pandas as pd

def plot_heatmap(df, pivot):
   if size(pivot)==3:
       df = df.pivot(pivot[0], pivot[1], pivot[2])
       ax = sns.heatmap(df, annot=True, fmt="d")

flights = sns.load_dataset("flights")
pivot = ["month", "year", "passengers"]
   
plot_heatmap(flights, pivot)