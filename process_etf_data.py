import sys
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import os

def process_html_file(file_path):
    try:
        print("Starting to process HTML file...")
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        print("File read successfully.")
        
        # Split content into lines
        lines = content.split('\n')
        print(f"Content split into {len(lines)} lines.")
        
        # Find the header line
        try:
            header_index = next(i for i, line in enumerate(lines) if 'Date |' in line)
            headers = [h.strip() for h in lines[header_index].split('|')]
            print(f"Headers found: {headers}")
        except StopIteration:
            raise ValueError("Could not find the header line containing 'Date |'")
        
        # Process data lines
        print("Processing data lines...")
        data = []
        total_index = None
        for i, line in enumerate(lines[header_index + 1:], start=header_index + 1):
            if line.strip().startswith('Total |'):
                total_index = i
                break
            if any(month in line for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']):
                cells = line.split('|')
                if len(cells) != len(headers):
                    print(f"Warning: Line {i} has {len(cells)} cells, expected {len(headers)}. Line content: {line}")
                    continue
                data.append([cell.strip() for cell in cells])
        
        print(f"Processed {len(data)} data lines.")
        
        # Create first dataframe
        try:
            df1 = pd.DataFrame(data, columns=headers)
            print("First DataFrame created successfully.")
        except ValueError as ve:
            print(f"Error creating DataFrame: {ve}")
            print(f"Data shape: {len(data)} rows, {len(headers)} columns")
            print(f"First few rows of data: {data[:5]}")
            raise
        
        # Process second dataframe if 'Total' line exists
        df2 = None
        if total_index:
            print("Processing second part of the data...")
            data2 = []
            for line in lines[total_index + 1:]:
                if any(month in line for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']):
                    cells = line.split('|')
                    if len(cells) != len(headers):
                        print(f"Warning: Line has {len(cells)} cells, expected {len(headers)}. Line content: {line}")
                        continue
                    data2.append([cell.strip() for cell in cells])
            df2 = pd.DataFrame(data2, columns=headers)
            print(f"Second DataFrame created with {len(df2)} rows.")
        
        # Combine dataframes
        df_full = pd.concat([df1, df2]) if df2 is not None else df1
        print(f"Full DataFrame created with {len(df_full)} rows.")
        
        # Convert Date column to datetime
        print("Converting Date column to datetime...")
        df_full['Date'] = pd.to_datetime(df_full['Date'], format='%d %b %Y', errors='coerce')
        if df_full['Date'].isnull().all():
            raise ValueError("Failed to parse any dates. Check the date format in the HTML file.")
        
        # Convert numeric columns to float
        print("Converting numeric columns to float...")
        numeric_columns = headers[1:]
        for col in numeric_columns:
            df_full[col] = pd.to_numeric(df_full[col].replace('-', '0'), errors='coerce')
        
        # Sort by date in descending order
        df_full = df_full.sort_values('Date', ascending=False)
        print("DataFrame sorted by date.")
        
        # Create latest data DataFrame
        df_latest = df_full[df_full['Date'] == df_full['Date'].max()].copy()
        
        if df_latest.empty:
            raise ValueError("No latest data available. Check if the dates are parsed correctly.")
        
        print("Processing completed successfully.")
        return df_full, df_latest
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path}' is empty.")
        sys.exit(1)
    except ValueError as ve:
        print(f"Error processing data: {str(ve)}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)

def save_dataframes(df_full, df_latest):
    try:
        current_date = datetime.now().strftime('%d%b%Y').upper()
        
        full_data_filename = f'FULL_DATA_{current_date}.parquet'
        latest_data_filename = f'LATEST_DATA_{current_date}.parquet'
        
        df_full.to_parquet(full_data_filename, index=False)
        df_latest.to_parquet(latest_data_filename, index=False)
        
        print(f"Full data saved as: {full_data_filename}")
        print(f"Latest data saved as: {latest_data_filename}")
    except Exception as e:
        print(f"Error saving DataFrames: {str(e)}")

if __name__ == '__main__':
    html_file_path = './scraped_content.html'
    
    if not os.path.exists(html_file_path):
        print(f"Error: The file '{html_file_path}' was not found.")
        sys.exit(1)
    
    try:
        print(f"Processing file: {html_file_path}")
        df_full, df_latest = process_html_file(html_file_path)
        
        print("Preview of full data:")
        print(df_full.head())
        print("\nPreview of latest data:")
        print(df_latest)
        
        user_input = input("Do you want to save the DataFrames as .parquet files? (y/n): ").lower()
        if user_input == 'y':
            save_dataframes(df_full, df_latest)
        else:
            print("DataFrames were not saved.")
    
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred in the main execution: {str(e)}")
        sys.exit(1)
