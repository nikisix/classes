import pandas as pd
d1 = pd.read_csv('jan15.csv')
d2 = pd.read_csv('extract_pandas.csv')

d1.drop_duplicates(subset=['Date'], inplace=True)
d2.drop_duplicates(subset=['Date'], inplace=True)

print d1.shape
print d2.shape

dm = pd.merge(left=d1, right=d2, how='outer',\
        left_on=d1.Date, right_on=d2.Date,\
        suffixes=('_l','_r'))

print dm.shape
