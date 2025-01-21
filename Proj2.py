import pandas as pd
import numpy as np

ds = pd.read_csv("sample_dataset.csv")
print(ds)

print("MISSIGN VALUES IN EACH COLUMN : ")
print(ds.isnull().sum())

print("TOTAL NUMBER OF MISSING VALUES : ")
print(ds.isnull().sum().sum())


print(ds[ds.isnull().any(axis=1)])

Q1 = ds["Math_Score"].quantile(0.25)
Q3 = ds["Math_Score"].quantile(0.75)
IQR = Q3 - Q1

lbound = Q1 - 1.5 * IQR
ubound = Q3 + 1.5 * IQR

outliers = ds[(ds["Math_Score"] < lbound) | (ds["Math_Score"] > ubound)]
print("OUTLIERS : ",outliers)

import numpy as np

ds['Log_Maths'] = np.log(ds['Math_Score']+1)
print("DATASET WITH TRANSFORMED ATTENDANCE : ")
ds['Math_Score'] = ds['Math_Score'].fillna(ds['Math_Score'].median())
ds['Log_Maths'] = ds['Log_Maths'].fillna(ds["Log_Maths"].median())
print(ds[['Name' , 'Math_Score' , 'Log_Maths']])
