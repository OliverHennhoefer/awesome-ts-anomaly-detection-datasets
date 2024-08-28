"""
Tennessee Eastman Process (TEP)
"""

import pyarrow
import pandas as pd
import matplotlib.pyplot as plt

tpe_sample = './local/tpe_sample.parquet'  # fault-free training file
df = pd.read_parquet(tpe_sample, dtype_backend='pyarrow')

df.plot(kind='line', figsize=(10, 6))
plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Line Plot of DataFrame Columns')
plt.grid(True)
plt.show()