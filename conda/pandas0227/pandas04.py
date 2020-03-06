# --- Pandas DataFrame 資料擷取與篩選 page.56
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 100, 24).reshape(6, 4), columns=list('ABCD'))
print(df)
print('')

print(df[3:5])
print('')

print(df[['A', 'B', 'D']])
print('')

print(df.loc[3, 'B'])   # (3,B)元素
print('')

print(df.iloc[3, 1])   # (3,1)元素
print('')

print(df.iloc[2:5, 0:2])   # 範圍擷取
print('')

print(df[df > 18])   # 篩選條件
# df[df > 18] = 18
print(df)
print('')

print(df[df.C > 50])   # 篩選條件
print('')


