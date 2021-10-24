import pandas as pd

df = pd.read_csv(r'csv-sample.csv', header=None)
row_count = len(df.index)
print("The total number of rows is", row_count)