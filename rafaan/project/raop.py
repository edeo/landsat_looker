import json
from pprint import pprint
import pandas as pd

#reading in training data to pandas dataframe
df = pd.read_json('data/train.json')

#descriptive statistics
df.describe()
df.info()

