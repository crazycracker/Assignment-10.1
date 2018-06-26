import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# step 1: read the csv file from the url
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv'
baby_data = pd.DataFrame(pd.read_csv(url))

# step 2: delete the unnamed columns, in this scenario it is the first column and print the columns
baby_data = baby_data.loc[:, ~baby_data.columns.str.contains('^Unnamed')]
# step 3: distribution of male and female

male_baby = baby_data.loc[baby_data['Gender'] == 'M']
female_baby = baby_data.loc[baby_data['Gender'] == 'F']

print('Male probability %f' %(male_baby.shape[0]/baby_data.shape[0]))
print('Female probability %f' %(female_baby.shape[0]/baby_data.shape[0]))
sns.set(style='darkgrid')
ax = sns.countplot(x='Gender',data=baby_data)
plt.show()
