import sys
import pandas as pd

def remove_matches(file1_path, file2_path, output_file):
    # Load the CSV files into pandas dataframes
    file1_df = pd.read_csv(file1_path)
    file2_df = pd.read_csv(file2_path)
    
    # Identify common columns to compare on
    common_cols = ['contig', 'start', 'end', 'strand']
    
    # Find common rows
    common_rows = pd.merge(file1_df[common_cols], file2_df[common_cols], on=common_cols, how='inner')
    
    # Remove matched rows from file2
    file2_filtered_df = file2_df[~file2_df[common_cols].apply(tuple, axis=1).isin(common_rows.apply(tuple, axis=1))]
    
    # Save the filtered dataframe to a new CSV file
    file2_filtered_df.to_csv(output_file, index=False)
    print(f"Filtered file saved as {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python remove_common.py <input1_path> <input2_path> <output_path>")
        sys.exit(1)
    
    input1, input2, output = sys.argv[1], sys.argv[2], sys.argv[3]
    remove_matches(input1, input2, output)
