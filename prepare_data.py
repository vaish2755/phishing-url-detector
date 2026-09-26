import pandas as pd

from src.feature_extraction import extract_features


# Load the dataset
df = pd.read_csv("data/phishing_urls.csv")

print("Dataset loaded.")
print("Number of URLs:", len(df))


# Extract features from every URL
print("\nExtracting URL features...")

features = df["url"].apply(extract_features)

# Convert list of dictionaries into a DataFrame
X = pd.DataFrame(features.tolist())

# Convert labels into numerical values
y = df["type"].map({
    "legitimate": 0,
    "phishing": 1
})


# Combine features and target
processed_df = X.copy()
processed_df["label"] = y


print("\nFeature extraction completed.")

print("\nFeature columns:")
print(X.columns.tolist())

print("\nProcessed dataset shape:")
print(processed_df.shape)

print("\nFirst 5 rows:")
print(processed_df.head())


# Save processed dataset
processed_df.to_csv("data/processed_data.csv", index=False)

print("\nProcessed dataset saved to:")
print("data/processed_data.csv")