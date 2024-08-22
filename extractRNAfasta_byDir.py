import sys
import os
import pandas as pd

def process_sequences(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Open the output file
    with open(output_file, 'w') as fasta_file:
        for index, row in df.iterrows():
            contig = row['contig']
            end = row['end']
            sequence = row['sequence']
            
            # Extract bases from 6 to 21 (1-based index in description, 0-based in Python)
            sub_sequence = sequence[5:21]
            
            # Convert DNA to RNA (replace T with U)
            rna_sequence = sub_sequence.replace('T', 'U')
            
            # Write to the fasta file
            fasta_file.write(f">{contig} ({end})\n")
            fasta_file.write(f"{rna_sequence}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extractRNAfasta_byDir.py /path_to_input/ /path_to_output/")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Process each CSV file in the input directory
    for input_file in os.listdir(input_dir):
        if input_file.endswith(".csv"):
            input_file_path = os.path.join(input_dir, input_file)
            output_file_path = os.path.join(output_dir, os.path.splitext(input_file)[0] + '.fasta')
            process_sequences(input_file_path, output_file_path)
