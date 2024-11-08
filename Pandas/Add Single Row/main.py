import pandas as pd

#Load the Data File

df = pd.read_csv('data.csv')

#Take user input

row_to_Add  =  pd.DataFrame({'Duration': [80], 'Date': ['2021/03/18'], 'Pulse': [115] , 'Maxpulse':[135] , 'Calories':[149]})

# Set the Data Frame

df = pd.concat([df , row_to_Add] , ignore_index=True)

# Set the Data File

df.to_csv('data.csv', index=False)

print(df)