import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def load_data(file_path):
    return pd.read_parquet(file_path)

def plot_cumulative_sum(data, features):
    plt.figure(figsize=(12, 6))
    for feature in features:
        cumulative_sum = data[feature].cumsum()
        sns.lineplot(x=data['Date'], y=cumulative_sum, label=feature)
    
    plt.title('Cumulative Sum of ETF Features')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Sum')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    # List all .parquet files in the current directory
    parquet_files = [f for f in os.listdir() if f.endswith('.parquet')]
    
    if not parquet_files:
        print("No .parquet files found in the current directory.")
        return

    print("Available .parquet files:")
    for i, file in enumerate(parquet_files):
        print(f"{i}: {file}")

    # Get user input for file selection
    while True:
        try:
            file_index = int(input("\nEnter the index of the file you want to visualize: "))
            if 0 <= file_index < len(parquet_files):
                selected_file = parquet_files[file_index]
                break
            else:
                print("Invalid index. Please enter a valid index.")
        except ValueError:
            print("Please enter a valid integer index.")

    # Load the ETF data
    try:
        etf_data = load_data(selected_file)
    except Exception as e:
        print(f"Error loading the file: {e}")
        return

    # Display available features
    print("\nAvailable features:")
    for i, feature in enumerate(etf_data.columns):
        if feature != 'Date':
            print(f"{i}: {feature}")

    # Get user input for feature selection
    user_input = input("\nEnter feature indices separated by commas, or 'all' for all features: ")

    if user_input.lower() == 'all':
        selected_features = [col for col in etf_data.columns if col != 'Date']
    else:
        feature_indices = [int(idx.strip()) for idx in user_input.split(',')]
        selected_features = [etf_data.columns[idx] for idx in feature_indices if idx < len(etf_data.columns)]

    # Plot the cumulative sum of selected features
    plot_cumulative_sum(etf_data, selected_features)

if __name__ == "__main__":
    main()
