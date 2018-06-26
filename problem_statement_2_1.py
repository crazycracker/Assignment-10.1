import pandas as pd

# step 1: read the csv file from the url
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv'
baby_data = pd.DataFrame(pd.read_csv(url))

# step 2: delete the unnamed columns, in this scenario it is the first column and print the columns
baby_data = baby_data.loc[:, ~baby_data.columns.str.contains('^Unnamed')]
print(baby_data.columns.tolist())
