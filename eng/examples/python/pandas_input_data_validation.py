import pandas as pd
import numpy as np
import sys


#if all data in a frame isn't numeric, it this will catch the error, then iterate through all columns
def validate_data(df):
    try:
        all(np.isfinite(df))
    except TypeError:
        for c in df.columns:    
            try:
                    print c
                    print all(np.isfinite(df[c]))
            except TypeError:
                print 'Error with column: '+c+'\nIt must be composed of all numbers.'
        sys.exit(2)

d = pd.DataFrame(np.random.rand(10,4), columns=['col1','col2','col3','col4'])
print all(np.isfinite(d))
print d
d.loc[1,'col1'] = 'a'
d.loc[1,'col3'] = 'b'
print d
# print all(np.isfinite(d)) #blows up
validate_data(d)
