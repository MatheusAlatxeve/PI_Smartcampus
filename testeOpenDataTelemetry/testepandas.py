# WaterTankLevel: data_distance (millimeters from the water);
# Hydrometer: data_counter (accumulated liters);
# ArtesianWell: data_filter_inlet_pressure (bar), data_filter_outlet_pressure (bar);
# Timestamp: Unix Timestamp milliseconds (13 digits).

# pandas
# seaborn
# statsmodels
# spicy

import pandas as pd
import matplotlib.pyplot as plt

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

print("print do DataFrame")

myvar = pd.DataFrame(mydataset)

print(myvar)

print("print do Series")

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 
print("print do loc[0]")
print(df.loc[0])

#load a file
import pandas as pd

df = pd.read_csv('data.csv')

# print(df) 
# print(df.to_string()) 
# use to_string() to print the entire DataFrame.
# You can check your system's maximum rows with the pd.options.display.max_rows statement.
# pd.options.display.max_rows = 9999

# load a json file
# import pandas as pd

# df = pd.read_json('data.json')

# print(df.to_string()) 

# Get a quick overview by printing the first 10 rows of the DataFrame:
# print(df.head(10))
# if the number of rows is not specified, the head() method will return the top 5 rows.
# Print the last 5 rows of the DataFrame:
# print(df.tail()) 

print(df.info()) 

# will drop all the empty cells
# new_df = df.dropna()
# If you want to change the original DataFrame, use the inplace = True argument:
# df.dropna(inplace = True) 
# Replace NULL values with the number 130
# df.fillna(130, inplace = True)
# Replace NULL values in the "Calories" columns with the number 130:
# df["Calories"].fillna(130, inplace = True)
# x = df["Calories"].mean()

# df["Calories"].fillna(x, inplace = True)
# x = df["Calories"].median()
# x = df["Calories"].mode()[0]

# Let's try to convert all cells in the 'Date' column into dates.

# Pandas has a to_datetime() method for this:
# df['Date'] = pd.to_datetime(df['Date'])

# Set "Duration" = 45 in row 7:

# df.loc[7, 'Duration'] = 45

# Loop through all values in the "Duration" column.

# If the value is higher than 120, set it to 120:

# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.loc[x, "Duration"] = 120

# Delete rows where "Duration" is higher than 120:

# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.drop(x, inplace = True)

# print(df.duplicated())
# df.drop_duplicates(inplace = True)

# Pandas - Data Correlations

# The Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.

# The number varies from -1 to 1.

# 1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column, the other one went up as well.

# 0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.

# -0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.

# 0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.

# What is a good correlation? It depends on the use, but I think it is safe to say you have to have at least 0.6 (or -0.6) to call it a good correlation.

#Pandas uses the plot() method to create diagrams.

# df = pd.read_csv('data.csv')

# df.plot()

# plt.show()

# df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

# Histogram

# df["Duration"].plot(kind = 'hist')

