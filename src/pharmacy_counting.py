#import pandas as pd 
#df1 = pd.read_csv("de_cc_data.txt")
#df2 = df1.groupby('drug_name').agg({'drug_cost' : [pd.Series.nunique,'sum']})
#df2.sort_values(by=[('drug_cost','sum'),'drug_name'], ascending = [False, True]).to_csv('top_cost_drug.txt')

import csv
import sys
import os

inputPath = str(sys.argv[1])
outputPath = str(sys.argv[2])

#Data Import
txt = open(inputPath);
dat = txt.read()
dat = dat.split('\n');

#Data Calc
pre = {}
df = {}
for line in dat:
    new.append(line.split(','))
for line in new[1:]:
    try:
        if line[0] not in pre[line[3]]:
            pre[line[3]].append(line[0])
    except:
        pre[line[3]] = [line[0]]
    try:
        df[line[3]] = [len(pre[line[3]]),df[line[3]][1]+eval(line[4])]
    except:
        df[line[3]] = [len(pre[line[3]]),eval(line[4])]
        
#Sorting
LI = []
for i in df.items():
    LI.append([i[0],i[1][0],i[1][1]])
LI.sort(key = lambda x : (-x[2], x[0]))
LI.insert(0,['drug_name','num_prescriber','total_cost'])

#Saving
with open(outputPath, "w") as f:
    writer = csv.writer(f)
    writer.writerows(LI)
