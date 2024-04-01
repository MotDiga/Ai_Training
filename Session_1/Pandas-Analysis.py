import pandas as pd
import os


# Get a list of all CSV files in Sales_Data
data_files = [("Sales_Data/" + file) for file in os.listdir("Sales_Data")]

# Create an empty list to hold dataframes
dfs = []

# Loop over the list of CSV files
for file in data_files:
    # Read each file into a pandas DataFrame and append it to the list
    dfs.append(pd.read_csv(file))

# Concatenate all dataframes in the list
the_df = pd.concat(dfs, ignore_index=True)

# Data Cleaning
the_df = the_df.drop_duplicates()
the_df = the_df.dropna()
the_df = the_df[the_df["Price Each"] != "Price Each"]
the_df.head()

# Write the Concatenated dataframes in a single CSV file
the_df.to_csv("Sales_Data/Sales_2019.csv")

# Add Mount and Sales columns to help us determin the best month for sales
the_df["Month"] = the_df["Order Date"].str[0:2]
the_df["Month"] = the_df["Month"].astype("int32")
the_df["Sales"] = the_df["Quantity Ordered"].astype("float64") * the_df["Price Each"].astype("float64")

mth_earns = the_df.groupby("Month").sum()
print(mth_earns["Sales"])
# The best mount is December with 4608295.5$ of sales

import matplotlib.pyplot as plt

mths = range(1, 13)
plt.bar(mths, mth_earns["Sales"])
plt.xticks(mths)
plt.xlabel("Mounts")
plt.ylabel("Sales in USD ($)")
plt.show()
# Add City column to help us determin the city with highest number of sales

def get_city(adress):
    splt_ad = adress.split(",")
    return splt_ad[1] + " (" + splt_ad[2].split(" ")[1] + ")"
    
the_df["City"] = the_df["Purchase Address"].apply(lambda x: get_city(x))#x.split(",")[1] + "," + x.split(",")[2])
the_df.head()
the_df["Quantity Ordered"] = the_df["Quantity Ordered"].astype("int32")

city_prchs = the_df.groupby("City").sum()
print(city_prchs["Quantity Ordered"])
# The best city is San Francisco, CA with 50169 purcheses

citys = [city for city, df in the_df.groupby("City")]
#citys = the_df["City"].unique()
#citys = range(1, len(city_prchs)+1)
plt.bar(citys, city_prchs["Quantity Ordered"])
plt.xticks(citys, rotation="vertical")
plt.xlabel("City")
plt.ylabel("Nember of Sales")
plt.show()

the_df["Order Date"] = pd.to_datetime(the_df["Order Date"])
the_df["Hour"] = the_df["Order Date"].dt.hour
the_df["Minute"] = the_df["Order Date"].dt.minute

hours = [hour for hour, df in the_df.groupby("Hour")]

plt.plot(hours, the_df.groupby("Hour").count())
plt.xticks(hours)
plt.grid()
plt.xlabel("Hour")
plt.ylabel("Nember of Sales")
plt.show()
# The best time for selling is in the 2 intervals [11h -> 13h], [18h -> 20h]

# Write the Modified version of our dataframes in a CSV file
the_df.to_csv("Sales_Data/Sales_2019(Mod).csv")
for hour, df in the_df.groupby("Hour"):
    products = [product for product, df in the_df[the_df["Hour"] == hour].groupby("Product")]
    plt.plot(products, the_df[the_df["Product"]].count())
