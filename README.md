# RNAeditingOffTarget
Custom scripts for identifying off-target RNA editing events from RNA-seq data. These tools help detect, quantify, and analyze off-target editing sites, offering a streamlined pipeline for researchers in RNA editing. Optimized for high-throughput data processing and adaptable for various downstream analyses.

# INSTRUCTIONS
1) Run the JACUSA2 csv files with the Analysis_JACUSA2.Rmd script. This will generate .csv tables for downstream analyses
2) Run the merge_samples.py script to merge toguether control files.
   USAGE: python merge_samples.py <Sample1_path> <Sample2_path> <output_path>
3) Run remove_common.py script to remove events found in common between controls and samples.
   USAGE: python remove_common.py <input1_path> <input2_path> <output_path>
4) Extract the .fasta lists with extractRNAfasta_byDir.py for downstream analyses with PPRmatcher.
   USAGE: python extractRNAfasta_byDir.py <path_to_input_dir> <path_to_output_dir>
