import pandas as pd
import numpy as np

d = pd.read_csv('head-wa.txt', sep='\t')
d.columns = ['state','code','date','id']
d.set_index('id',inplace=True)
print 'before transform'
print d.head()
d.date = d.date.map(
        lambda x: '-'.join([
            '-'.join(x.split('/')[0:2]), 
            str( int( x.split('/')[-1]) +1 )
            ])
        )
print 'after transform'
print d.head()
