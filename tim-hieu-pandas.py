import numpy as np
import pandas as pd

#Khởi tạo 1 sery
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

#Tao bang du lieu 6 hang va 4 cot
df = pd.DataFrame(np.random.randn(6, 4), columns=list("ABCD"))
print(df)

dates = pd.date_range("20130101", periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)