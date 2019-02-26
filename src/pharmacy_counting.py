#import pandas as pd 
#df1 = pd.read_csv("de_cc_data.txt")
#df2 = df1.groupby('drug_name').agg({'drug_cost' : [pd.Series.nunique,'sum']})
#df2.sort_values(by=[('drug_cost','sum'),'drug_name'], ascending = [False, True]).to_csv('top_cost_drug.txt')

import csv
import sys
import os

inputPath = str(sys.argv[1])
outputPath = str(sys.argv[2])

import pandas as pd 
df1 = pd.read_csv(inputPath)
df2 = df1.groupby('drug_name').agg({'drug_cost' : [pd.Series.nunique,'sum']})
df3 = df2.sort_values(by=[('drug_cost','sum'),'drug_name'], ascending = [False, True])
df3 = df3['drug_cost'].reset_index()
df3.columns = ['drug_name','num_prescriber','total_cost'] 
df3.to_csv(outputPath, index = False)
