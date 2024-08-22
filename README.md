# RNA editing Off-Target Analysis
Custom scripts for identifying off-target RNA editing events from RNA-seq data. These tools help detect, quantify, and analyze off-target editing sites, offering a streamlined pipeline for researchers in RNA editing. Optimized for high-throughput data processing and adaptable for various downstream analyses.

# Pre-processing
First, analyze the aligned BAM files with [JACUSA2](https://github.com/dieterich-lab/JACUSA2) with the *call-2* option.
$ java -jar jacusa2.jar call-2 results_call2.out Sample#.bam
   - **Flags**: -R `reference2.fasta` -r `Sample#_call2-FS.vcf` -P `RF-FIRSTSTRAND`

# INSTRUCTIONS
1) Run the [JACUSA2](https://github.com/dieterich-lab/JACUSA2) output `.CSV` files through the `Analysis_JACUSA2.Rmd` script. This will generate `.csv` tables for downstream analyses.
2) Run the `merge_samples.py` script to merge together control files.
   - **Usage**: `python merge_samples.py <Sample1_path> <Sample2_path> <output_path>`
3) Run the `remove_common.py` script to remove events found in common between controls and samples.
   - **Usage**: `python remove_common.py <input1_path> <input2_path> <output_path>`
4) Extract the `.fasta` lists using the `extractRNAfasta_byDir.py` script for downstream analyses with [PPRmatcher](https://github.com/ian-small/PPRmatcher).
   - **Usage**: `python extractRNAfasta_byDir.py <path_to_input_dir> <path_to_output_dir>`
