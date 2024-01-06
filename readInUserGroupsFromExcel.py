# Import modules
import openpyxl as op
import pandas as pd


# Read the Excel file into a DataFrame
df = pd.read_excel("Book1.xlsx")

print(df)

# Loop through the group-name column values and output them using print()
for name, values in df["group-name"].items():
    print(values)