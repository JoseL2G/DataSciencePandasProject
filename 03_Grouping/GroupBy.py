import pandas as pd

drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv')
drinks.head()

drinks.groupby('continent').beer_servings.mean()