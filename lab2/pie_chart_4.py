"""
Method:         Pie chart
Data Variables: quantitative and nominal
Author:         Adayev Marat
"""

import pandas as pd
import matplotlib.pyplot as pl


def get_data():
    data = pd.read_csv('user_bq_data.csv')
    gender_list = data.gender.values.tolist()
    male = 0
    female = 0
    for w in gender_list:
        if (w == 'male'):
            male += 1;
        if (w == 'female'):
            female += 1;

    return [male, female]


def pie_chart(values):
    gender = 'Male', 'Female'
    proportion = values
    explode = [0, 0]
    pl.pie(proportion, explode=explode, labels=gender, autopct='%1.1f%%',
           shadow=True, startangle=90)
    pl.axis('equal')
    pl.title('Male/Female')


pie_chart(get_data())
pl.show()
