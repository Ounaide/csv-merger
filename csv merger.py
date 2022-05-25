from pandas import *
import os

dataframes = [read_csv(name,delimiter=" ") for name in os.listdir() if name.split(".")[0]!="combined" and name.split(".")[-1]=="csv"]

df = concat(dataframes,ignore_index=True)

df.to_csv("combined.csv",sep=" ",index=0)