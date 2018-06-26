import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# step 1: read the csv file from the url
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv'
baby_data = pd.DataFrame(pd.read_csv(url))

# step 2: delete the unnamed columns, in this scenario it is the first column
baby_data = baby_data.loc[:, ~baby_data.columns.str.contains('^Unnamed')]
#print(baby_data.columns.tolist())

# step 3: male and female born count by states

grouped_data_by_states = baby_data.groupby(by=['State', 'Gender'], as_index=False).agg({"Count": "sum"}).sort_values(
    by='State',
    ascending=False
)
states = baby_data['State'].unique()
print(states)

i = 0
j = 0

'''
    Grouping the plots into one single plot wasn't seemingly attractive, so i have plotted every states plot one by one
'''
for state in states:
    temp_data = grouped_data_by_states[grouped_data_by_states.State == state]
    sns.set(style='darkgrid')
    sns.barplot(x='Gender', y='Count', data=temp_data)
    plt.title('State: %s' % state)
    plt.show()
    j = j + 1
    if j == 7:
        i = i + 1
        j = 0
