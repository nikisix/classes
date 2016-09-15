import pandas as pd
d = pd.read_csv('head-wa.txt', sep='\t', header=None)
d.columns=['countycode','state_voterid','election_date','unique_county_code']
print d
