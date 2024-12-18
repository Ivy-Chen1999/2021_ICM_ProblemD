import csv
import numpy as np
import networkx as nx 


for line in csv_reader:
    if head:
        head = False
        continue
    cnt += 1
    for i in range(len(line)-1):
        if i == 5:
            continue
        if i > 6:
            continue
        val = float(line[i+1])
        feature_average[i] += val
        # print(i)
        feature_max[i] = max(feature_max[i], val)
        feature_min[i] = min(feature_min[i], val)

feature_average = np.array(feature_average) / cnt
