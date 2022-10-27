from gwosc import datasets
from gwosc import timeline

set = datasets.find_datasets()

for i in set:
    print(i)

timeline.get_segments

