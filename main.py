import pandas as pd
from pathlib import Path

# Path to your data folder
data_folder = Path("data")

# Read all three CSVs
csv_files = list(data_folder.glob("*.csv"))
dfs = [pd.read_csv(f) for f in csv_files]

# Combine into one DataFrame
data = pd.concat(dfs, ignore_index=True)

# Keep only rows for 'Pink Morsel'
data = data[data["product"] == "pink morsel"]

# Create the 'sales' column
data["sales"] = data["quantity"] * data["price"]

# Select only required fields
final = data[["sales", "date", "region"]]

# Save to a new CSV file
output_path = data_folder / "cleaned_data.csv"
final.to_csv(output_path, index=False)

print(f" Cleaned data saved to: {output_path}")
print(final.head())
