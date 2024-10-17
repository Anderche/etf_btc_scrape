import os
import pandas as pd
import glob
import re
from datetime import datetime

def list_parquet_files(directory):
    parquet_files = [f for f in os.listdir(directory) if f.endswith('.parquet')]
    return parquet_files

def convert_parquet_to_csv(input_file, output_file):
    df = pd.read_parquet(input_file)
    df.to_csv(output_file, index=False)
    print(f"\nConverted {input_file} to {output_file}")

def delete_older_file(file_pattern):
    matching_files = glob.glob(file_pattern)
    if len(matching_files) > 1:
        # Sort files by modification time (newest first)
        sorted_files = sorted(matching_files, key=os.path.getmtime, reverse=True)
        for old_file in sorted_files[1:]:
            os.remove(old_file)
            print(f"Deleted older file: {old_file}")

def save_parquet_file(df, file_name, directory='.'):
    # Construct the full file path
    full_path = os.path.join(directory, file_name)
    
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    
    # Save the DataFrame as a Parquet file
    df.to_parquet(full_path, index=False)
    print(f"Saved Parquet file: {full_path}")

def main():
    directory = '.'  # Current directory, change this if needed
    output_directory = './artifacts_csv'  # New output directory for CSV files
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)
    
    parquet_files = list_parquet_files(directory)
    
    if not parquet_files:
        print("No .parquet files found in the current directory.")
        return
    
    print("\nFound the following .parquet files:")
    for idx, file in enumerate(parquet_files):
        print(f"{idx + 1}. {file}")
    
    while True:
        try:
            choice = int(input("\nEnter the number of the file you want to convert (or 0 to exit): "))
            if choice == 0:
                print("Exiting the program.")
                return
            if 1 <= choice <= len(parquet_files):
                selected_file = parquet_files[choice - 1]
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    input_file = os.path.join(directory, selected_file)
    output_file = os.path.join(output_directory, os.path.splitext(selected_file)[0] + '.csv')
    
    # Read the parquet file
    df = pd.read_parquet(input_file)
    
    # Save the new parquet file (this will ask about deleting older files)
    save_parquet_file(df, selected_file, directory)
    
    # Convert to CSV
    convert_parquet_to_csv(input_file, output_file)

if __name__ == "__main__":
    main()
