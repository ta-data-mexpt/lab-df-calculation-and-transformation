import pandas as pd
import numpy as np

animals = pd.read_csv('animals.csv')

#We create a new column converting body wieghts
animals['dobywt kgs'] = animals['bodywt'] * 0.45359237

#we can compute the ratio of body weight to brain weight for all animals in our data and assign this value to a new column.

animals['wtratio'] = animals['bodywt']/animals['brainwt']

#we can introduce a condition in our assignment. If the brain weight is zero then the ratio will be zero, otherwise, store the ratio in the new column. We can create conditional functions using the where function in numpy. We pass 3 arguments to the function. The first argument is the condition, the second is the value in case the condition is true, and the third is the value in case the condition is false.

animals['wtratio-zero-check'] = np.where(animals['brainwt'] != 0, animals['bodywt']/animals['brainwt'], 0)
#print(animals.head())
#Let's say we want to take a sum of all numeric columns in the animals DataFrame. We can do this by using the sum function and passing axis=1 as an argument to the function.
animals['sum'] = animals.sum(axis = 1)
print(animals.head())

