import os
import pandas as pd

def list_parquet_files(directory):
    parquet_files = [f for f in os.listdir(directory) if f.endswith('.parquet')]
    return parquet_files

def convert_parquet_to_csv(input_file, output_file):
    df = pd.read_parquet(input_file)
    df.to_csv(output_file, index=False)
    print(f"Converted {input_file} to {output_file}")

def main():
    directory = '.'  # Current directory, change this if needed
    output_directory = './artifacts_csv'  # New output directory
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)
    
    parquet_files = list_parquet_files(directory)
    
    if not parquet_files:
        print("No .parquet files found in the current directory.")
        return
    
    print("Found the following .parquet files:")
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
    
    convert_parquet_to_csv(input_file, output_file)

if __name__ == "__main__":
    main()
