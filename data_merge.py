import pandas as pd
import os

# Define the folder path where your 16 spreadsheets are located
folder_path = 'C:/Users/natha/OneDrive/Desktop/Advanced Business Analytics/Railroad_Accidents/csv'

# Create an empty list to store DataFrames
data_frames = []

# Loop through each file in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):  # Ensure you're reading only CSV files
        file_path = os.path.join(folder_path, file_name)
        # Read the current CSV file and append the DataFrame to the list
        df = pd.read_csv(file_path)
        data_frames.append(df)

# Concatenate all DataFrames into one
combined_df = pd.concat(data_frames, ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('RR_Accident_Weather_Data.csv', index=False)

print("All files have been successfully combined into 'RR_Accident_Weather_Data.csv'")