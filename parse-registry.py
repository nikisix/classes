import itertools as it
import ConfigParser as cp
import sys

#read through the registry and populate geolist and tablemap
#tablemap = { geo : table }
geolist = []
geo_table_map = {}
parser = cp.ConfigParser()
parser.add_section('config')
for geo_table in file('registry.csv').readlines():
    geo, table = geo_table.strip().split(',')
#    if not parser.has_section(geo):
#        parser.add_section(geo)
#    parser.set(geo,table)
    if geo_table_map.has_key(geo):   geo_table_map[geo].append(table)
    else:   geo_table_map[geo] = [table]
    geolist.append(geo)

for k,v in geo_table_map.iteritems():
    parser.set('config', k ,v)
#    print k,v
parser.write(file('config.out','w'))
print geolist
print
print geo_table_map
