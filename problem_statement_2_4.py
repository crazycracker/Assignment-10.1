import pandas as pd

# step 1: read the csv file from the url
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv'
baby_data = pd.DataFrame(pd.read_csv(url))

# step 2: delete the unnamed columns, in this scenario it is the first column
baby_data = baby_data.loc[:, ~baby_data.columns.str.contains('^Unnamed')]
#print(baby_data.columns.tolist())

# step 3: Grouping the baby names with their count sum
grouped_data_by_name = baby_data.groupby(by='Name', as_index=False).agg({"Count": "sum"}).sort_values(
                            by='Count',
                            ascending=False
                        )

# step 4: median name occurence
median_count_value = grouped_data_by_name['Count'].median()
print('Median Name Occurence')
print(grouped_data_by_name[grouped_data_by_name['Count'] == median_count_value])
