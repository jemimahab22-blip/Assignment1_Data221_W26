import pandas as pd
#I am creating a DataFrame from provided data
data = {
    "A": [1,2,2,1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150,400,210]
}

dataframe_of_my_data= pd.DataFrame(data)
#I am adding a new column derived form the existing columns

dataframe_of_my_data['Addition']= (dataframe_of_my_data["A"]+ dataframe_of_my_data["B"])
#i am printing out the final DataFrame
print(dataframe_of_my_data)