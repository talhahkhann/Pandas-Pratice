import pandas as pd


#Load Data File

df = pd.read_csv('data.csv')

#Take input from the User

value_to_search = int(input('Enter Value'))

#Set the Data Frame
result = df[df['Duration'] == value_to_search]

#Print the data
print(result)
