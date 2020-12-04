import pandas as pd
import numpy as np

vehicles = pd.read_csv('vehicles.csv')
vehicles.groupby(['Transmission'])

#Some standard aggregation functions are: mean, sum, count, median, min, max, std.
#We can also use the agg function to apply multiple aggregations at once to all columns specified.
#After aggregating, we can subset the data to only apply the aggregation to the columns that we choose.Some standard aggregation functions are: mean, sum, count, median, min, max, std.
#We can also use the agg function to apply multiple aggregations at once to all columns specified.
#After aggregating, we can subset the data to only apply the aggregation to the columns that we choose.

print(vehicles.groupby(['Transmission'])['Highway MPG', 'City MPG', 'Combined MPG'].mean())
