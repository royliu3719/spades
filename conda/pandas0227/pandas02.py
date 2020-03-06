# --- Pandas DataFrame 建立與附加 page.55
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.rand(6, 4), columns=list('A B C D'))   # 0 到 1 之間
print(df1)
print('')

df2 = pd.DataFrame(np.random.randn(6, 4), columns=list('A B C D'))   # 常態分配
print(df2)
print('')

df1 = df1.append(df2, ignore_index=True)   # 附加 df2
df1 = df1.drop(list(range(2, 8)))   # drop row
df1 = df1.drop(columns=['A', 'D'])   # drop column
df1 = df1.drop(11)   # drop row index=11
print(df1)
print('')

