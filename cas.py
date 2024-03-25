import pandas as pd

df = pd.read_csv('test.csv')
df = df.drop(columns=['Suppressed', 'Series_reference', 'STATUS', 'UNITS', 'Magnitude','Subject', 'Group', 'Series_title_1', 'Series_title_3', 'Series_title_4', 'Series_title_5'])
df.to_csv('test.csv', index=False)