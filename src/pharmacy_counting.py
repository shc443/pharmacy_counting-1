import csv
import sys
import os
#import pandas as pd 

inputPath = str(sys.argv[1])
outputPath = str(sys.argv[2])

#df1 = pd.read_csv(inputPath)
#df2 = df1.groupby('drug_name').agg({'drug_cost' : [pd.Series.nunique,'sum']})
#df3 = df2.sort_values(by=[('drug_cost','sum'),'drug_name'], ascending = [False, True])
#df3 = df3['drug_cost'].reset_index()
#df3.columns = ['drug_name','num_prescriber','total_cost'] 
#df3.to_csv(outputPath, index = False)

#Data Import
txt = txt = open(inputPath);
dat = txt.read()
dat = dat.split('\n');

#Data Calc
pre = {}
df = {}
new = []
for line in dat:
    new.append(line.split(','))
for line in new[1:]:
    try:
        if line[0] not in pre[line[3]]:
            pre[line[3]].append(line[0])
    except:
        try:
            pre[line[3]] = [line[0]]
        except:
            print("")
    try:
        df[line[3]] = [len(pre[line[3]]),df[line[3]][1]+eval(line[4])]
    except:
        try:
            df[line[3]] = [len(pre[line[3]]),eval(line[4])]
        except:
            print("")

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


