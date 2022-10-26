from gwdatafind import *
from gwdatafind.utils import *

#find latest data file from the server

filename = find_latest('H', 'H1_GWOSC_O2_4KHZ_R1', urltype='file', host='datafind.gw-openscience.org')
print(filsename)

print("segment: \n")
print(file_segment(filename[0]))
print("metadata: \n")
print(filename_metadata(filename[0]))







