import pandas as pd

# step 1: read the csv file from the url
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv'
baby_data = pd.DataFrame(pd.read_csv(url))

# step 2: delete the unnamed columns, in this scenario it is the first column and print the columns
baby_data = baby_data.loc[:, ~baby_data.columns.str.contains('^Unnamed')]

# step 3: top 5 most preferred names
print("top 5 most preferred names")
grouped_data_by_name = baby_data.groupby(by='Name', as_index=False).agg({"Count": "sum"}).sort_values(
                            by='Count',
                            ascending=False
                        )
print(grouped_data_by_name.head(5))
