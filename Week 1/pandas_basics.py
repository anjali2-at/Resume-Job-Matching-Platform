import pandas as pd

# Load the dataset
df = pd.read_csv("sample_dataset.csv")

print("===== Original Dataset =====")
print(df)

# Display basic information
print("\n===== Dataset Information =====")
print(df.info())

# Check missing values
print("\n===== Missing Values =====")
print(df.isnull().sum())

# Clean missing values
df["Skills"] = df["Skills"].fillna("Not Provided")
df["Experience"] = df["Experience"].fillna(df["Experience"].mean())

print("\n===== Cleaned Dataset =====")
print(df)

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

# Features (Input)
features = df[["Skills", "Experience", "Education"]]

# Label (Output)
labels = df["JobRole"]

print("\n===== Features =====")
print(features)

print("\n===== Labels =====")
print(labels)