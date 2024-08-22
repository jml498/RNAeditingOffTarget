import sys
import pandas as pd

def merge_files(file1_path, file2_path, output_file):
    # Load the CSV files into pandas dataframes
    file1_df = pd.read_csv(file1_path)
    file2_df = pd.read_csv(file2_path)
    
    # Add a new column to indicate the source of each row
    file1_df['source'] = '1'
    file2_df['source'] = '2'
    
    # Identify common columns to merge on
    common_cols = ['contig', 'start', 'end', 'strand']
    
    # Find common rows
    common_rows = pd.merge(file1_df[common_cols], file2_df[common_cols], on=common_cols, how='inner')
    
    # Tag common rows in file1 as 'B1' and in file2 as 'B2'
    file1_df.loc[file1_df[common_cols].apply(tuple, axis=1).isin(common_rows.apply(tuple, axis=1)), 'source'] = 'B1'
    file2_df.loc[file2_df[common_cols].apply(tuple, axis=1).isin(common_rows.apply(tuple, axis=1)), 'source'] = 'B2'
    
    # Concatenate the dataframes to get the union without dropping duplicates
    union_df = pd.concat([file1_df, file2_df])

    # Sort the final dataset by 'end' value
    union_df = union_df.sort_values(by='end')
    
    # Save the union dataframe to a new CSV file
    union_df.to_csv(output_file, index=False)
    print(f"Union file saved as {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python merge_samples.py <Sample1_path> <Sample2_path> <output_path>")
        sys.exit(1)
    
    file1, file2, output = sys.argv[1], sys.argv[2], sys.argv[3]
    merge_files(file1, file2, output)
