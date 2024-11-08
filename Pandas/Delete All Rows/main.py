import pandas as pd

#Load the CSV file


df = pd.read_csv('performed.csv')

#Remove all rows by assigning empty data frame
df =  df[0:0]

#Save the empty data frame back to csv file

df.to_csv('performed.csv', index=False)