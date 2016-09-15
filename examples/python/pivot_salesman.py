# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import datetime as dt
import xlsxwriter
import matplotlib as plt

df = pd.DataFrame.from_csv('salesman.csv', index_col = 'Created Date')
# del df['Unnamed: 4']
df['opp_count'] = np.ones(len(df))
groups = df.groupby(by = ['Created By', pd.TimeGrouper(freq='M')])
df_out = pd.DataFrame(groups.sum())
print df_out.head()
print
# writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
# df_out.transpose().to_excel(writer,'Sheet1')
# writer.save()


# In[114]:

df = pd.DataFrame.from_csv('salesman.csv', index_col = None)
# del df['Unnamed: 4']
df['Created Date'] = pd.to_datetime(df['Created Date'], format = '%m/%d/%Y')
df['opp_count'] = np.ones(len(df))
groups = df.groupby(by = ['Created By', pd.TimeGrouper(freq='M', key='Created Date')])
df_out = pd.DataFrame(groups.sum())
print df_out.transpose().head()
print


# In[155]:
print 'crosstab'
print pd.crosstab(index = df['Created By'],
            columns = df['Created Date'],
            values = df['Amount'],
            aggfunc = np.sum ).head()
print
#pd.DataFrame(df, columns = ['opp_count', 'Amount'])


# In[3]:

#second approach
from pylab import rcParams
rcParams['figure.figsize'] = 15, 10

months = { i : dt.datetime(2000,i,1).strftime("%B") for i in range(1, 13)}
# df["month_number"] = df["month_name"].map(months)
months
df = pd.DataFrame.from_csv('salesman.csv',
                           index_col = 'Created Date')
# del df['Unnamed: 4']
df['opp_count'] = np.ones(len(df))
# df.index = [months[i] for i in df.index.month] #remove this at year's end
df = df[df['Created By']=='Ross Gratopp']
groups = df.groupby(by = ['Created By', pd.TimeGrouper('M')])
df_out = pd.DataFrame(groups.sum())
df_out.transpose().boxplot()
plt.show()

# In[ ]:

#df.index > dt.datetime.strptime('2014-1-9', '%Y-%m-%d')
# pd.groupby(df,by=[pd.to_datetime(df['Created Date']).month,df['Created Date'].year])
# dates = pd.to_datetime(df['Created Date'], format = '%Y-%m-%d')
# df.groupby(pd.TimeGrouper(freq='M'))

# d_new = pd.DataFrame(piv.groupby(by = piv.index.month, axis =0 , as_index = True).sum())
# d_new.index = [months[i] for i in d_new.index]
# d_new


# In[156]:

#df.pivot_table(values = 'Amount', index = 'Created By', aggfunc = sum, columns = 'Created Date')
df = pd.DataFrame.from_csv('salesman.csv', index_col = None)
# del df['Unnamed: 4']
df['opp_count'] = np.ones(len(df))
df['Created Date'] = pd.to_datetime(df['Created Date'], format = '%m/%d/%Y')
df_ross = df[df['Created By'] == 'Ross Gratopp']


# In[157]:

piv = df_ross.pivot_table(columns = pd.TimeGrouper('M', key = 'Created Date'),
                          index = 'Created By',
                          values = ['opp_count', 'Amount'],
                          aggfunc = np.sum)
piv


# In[158]:

piv = pd.pivot_table(df_ross, 
               index = [pd.TimeGrouper('M', key = 'Created Date'), 'Created By'], 
               aggfunc = np.sum,
               values = ['opp_count', 'Amount']
               )
piv.stack().unstack('Created Date')


# In[3]:

import pandas as pd
import numpy as np
import xlsxwriter

df = pd.DataFrame.from_csv('salesman.csv', index_col = None)
# del df['Unnamed: 4']
df['opp_count'] = np.ones(len(df))
df['Created Date'] = pd.to_datetime(df['Created Date'], format = '%m/%d/%Y')
melted = pd.melt(df, id_vars = ['Created Date', 'Created By'], value_vars = ['Amount', 'opp_count'])
final = melted.pivot_table(
               index = 'Created By',
               columns = [pd.TimeGrouper('M', key = 'Created Date'), 'variable'],
               aggfunc = np.sum,
               values = 'value'
        )
# writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
# final.to_excel(writer, 'Sheet1')
# writer.save()

