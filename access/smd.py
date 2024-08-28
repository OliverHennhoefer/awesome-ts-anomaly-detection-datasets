"""
Server Machine Dataset (SMD)
"""

import pandas as pd
import matplotlib.pyplot as plt

train_machine_1_1 = 'https://github.com/NetManAIOps/OmniAnomaly/blob/master/ServerMachineDataset/train/machine-1-1.txt?raw=true'

df = pd.read_csv(train_machine_1_1, header=0, sep=',')

df.plot(kind='line', figsize=(10, 6))
plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Line Plot of DataFrame Columns')
plt.grid(True)
plt.show()