# --- Pandas DataFrame 切片 page.56
import pandas as pd

data = [{'A': 1, 'B': 2},
        {'A': 5, 'B': 10, 'C': 20},
        {'B': 10, 'C': 5, 'D': 22}]

df = pd.DataFrame(data, columns=list('A B C D'), index=['r0', 'r1', 'r2'])
print(df)
print('')

print(df.loc['r0'])   # row slice
print('')

print(df.iloc[1])
print('')

print(df['B'])   # column slice
print('')

print(df.loc['r1':'r2', 'C':'D'])   # row and column slice
print('')

print(df.shape)

