import pandas as pd

#Load Data File
df = pd.read_csv('data.csv')
# Take Input from the user
value_to_deleted = float(input("Enter the Value"))
# Set the Data Frame According to Input
df = df[df['Calories'] != value_to_deleted ]

# Rewrite the File
df.to_csv('data.csv', index=False)

