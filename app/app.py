import pandas as pd
import numpy as np

data= pd.read_csv('vgsales.csv')

data = pd.DataFrame(data)
print(data.describe())
print(data.columns)

