import pandas as pd

# data = {
#     "Name": ["Alice", "Bob", "Charlie"],
#     "Age": [25, 30, 35],
#     "Salary": [50000, 60000, 70000]
# }
# df = pd.DataFrame(data)

# # print(df)

# df.set_index("Name", inplace=True)  # set index to Name by this the shape of the data frame will be (3, 2)
# print(df)
# print(df.shape)
# print(df.columns)

# data = [["A", 90], ["B", 95], ["C", 85]]
# df = pd.DataFrame(data, columns=["Name", "Marks"])
# print(df)

# df["NewColumn"] = df["Marks"] * 2
# df.set_index([pd.Index(["A", "B", "C"])], inplace=True)
# print(df)
# print(df.loc["A"])      # loc is used to access the data by the index
# print(df.iloc[1])       # iloc is used to access the data by the row number

#USE OF GROUPBY
data = {
    "Name": ["Alice", "Bob", "Charlie", "Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35, 25, 30, 35],
    "Salary": [50000, 60000, 70000, 80000, 90000, 100000]
}

df = pd.DataFrame(data)

grouped = df.groupby("Name")["Salary"]  #remember this creates an object
print(grouped.mean())