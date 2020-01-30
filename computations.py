import pandas as pd
import pyspark
from pyspark import SparkContext

sc=SparkContext("spark://ip-172-31-47-76.eu-west-1.compute.internal:7077", "Test")

data_filepath = '/home/ubuntu/server/wine.csv'

data = pd.read_csv(data_filepath)
# data.info()

n_records = data.quality.count()
n_unique_qualities = data.quality.unique()

records_str = f'Number of records: {n_records}'
qualities_str = f'Number of unique qualities: {n_unique_qualities}'

print(records_str)
print(qualities_str)

with open('statistics.txt', 'w') as file:
    for string in (records_str, qualities_str):
        file.write(string + '\n')
sc.stop()
