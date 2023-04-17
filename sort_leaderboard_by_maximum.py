import pandas as pd #pandas is too good for csv files
  
# making data frame from csv file
data = pd.read_csv("bullet.csv")
data.sort_values("Maximum Rating", axis=0, ascending=False,
                 inplace=True, na_position='first')
print(data)
data.to_csv('bullet_sorted_by_max_rating.csv', index=False)