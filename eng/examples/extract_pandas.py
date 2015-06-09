"""
Take mean of BlockRange values (separated by a dash)
Merge three fields into an Address field:
Address = BlockRange + StreetName + Type"""

import pandas as pd
import numpy as np

d = pd.read_csv('jan15.csv')
#filterint out UNK values for blockranges, Double check with GIS
d = d[d.BlockRange!='UNK']
d.BlockRange = d.BlockRange.map(
    lambda x: int(
        np.mean(
            [int(i) for i in x.split('-')]
        )
    )
)

d['Address'] = pd.DataFrame([' '.join([str(i[0]),i[1],i[2]]) for i in zip(d.BlockRange, d.StreetName, d.Type)], index=d.index)
del d['BlockRange']
del d['StreetName']
del d['Type']
d.to_csv('out.csv')
