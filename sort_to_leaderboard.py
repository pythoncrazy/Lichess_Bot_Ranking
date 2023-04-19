import pandas as pd #pandas is too good for csv files
  

variants = ["bullet","blitz","rapid"]

def sort_to_csv(variant):
    # making data frame from csv file
    data = pd.read_csv(variant+"/"+variant+".csv")
    data.sort_values("Maximum Rating", axis=0, ascending=False,
                    inplace=True, na_position='first')
    print(data)
    data.to_csv(variant+"/"+variant+'_sorted_by_max_rating.csv', index=False)

    data = pd.read_csv(variant+"/"+variant+".csv")
    data.sort_values("Current Rating", axis=0, ascending=False,
                    inplace=True, na_position='first')
    print(data)
    data.to_csv(variant+"/"+variant+'_sorted_by_current_rating.csv', index=False)

for variant in variants:
    sort_to_csv(variant)
