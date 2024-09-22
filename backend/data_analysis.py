import pandas as pd

# Load the Netflix dataset
data_path = './data/netflix_data.csv'
df = pd.read_csv(data_path)

# Display the first few rows of the dataset
print(df.head())
