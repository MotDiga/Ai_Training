import pandas as pd
import os

# Get a list of all CSV files in Sales_Data
data_files = [("Sales_Data/" + file) for file in os.listdir("./Sales_Data")]

# Create an empty list to hold dataframes
dfs = []

# Loop over the list of CSV files
for file in data_files:
    # Read each file into a pandas DataFrame and append it to the list
    dfs.append(pd.read_csv(file))

# Concatenate all dataframes in the list
the_df = pd.concat(dfs, ignore_index=True)
