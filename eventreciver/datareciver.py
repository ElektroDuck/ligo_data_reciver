from gwdatafind import *
from gwdatafind.utils import *

#find latest data file from the server

filename = find_latest('H', 'H1_GWOSC_O2_4KHZ_R1', urltype='file', host='datafind.gw-openscience.org')

#filename = find_latest('H', 'H1_R', urltype='file', host='https://datafind.gw-openscience.org')

print(filename)

print("segment: \n")
print(file_segment(filename[0]))
print("metadata: \n")
print(filename_metadata(filename[0]))

print(find_observatories(host="datafind.gw-openscience.org"))

print(type(file_segment(filename[0])))

var = type(file_segment(filename[0]))




