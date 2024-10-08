
# RNA Editing Off-Target Analysis
This repository contains custom scripts for identifying off-target RNA editing events from RNA-seq data. The tools provided here enable the detection, quantification, and analysis of off-target editing sites, offering a streamlined pipeline optimized for high-throughput data processing. The pipeline is adaptable for various downstream analyses, making it a valuable resource for researchers in the field of RNA editing.

## Pre-processing
Before running the custom scripts, you must analyze the aligned BAM files using [JACUSA2](https://github.com/dieterich-lab/JACUSA2) with the `call-2` option:

```bash
$ java -jar jacusa2.jar call-2 results_call2.out Sample#.bam
```

### Recommended Flags:
- `-R reference2.fasta`
- `-r Sample#_call2-FS.vcf`
- `-P RF-FIRSTSTRAND`

## Instructions

### 1. Analyze JACUSA2 Output
Run the output `.CSV` files generated by [JACUSA2](https://github.com/dieterich-lab/JACUSA2) through the `Analysis_JACUSA2.Rmd` script. This script will process the data and generate `.csv` tables for downstream analyses.

### 2. Merge Control Files
Use the `merge_samples.py` script to merge control files together.

**Usage**:
```bash
python merge_samples.py <Sample1_path> <Sample2_path> <output_path>
```

### 3. Remove Common Events
Use the `remove_common.py` script to remove events found in both control and sample files.

**Usage**:
```bash
python remove_common.py <input1_path> <input2_path> <output_path>
```

### 4. Extract FASTA Lists
Use the `extractRNAfasta_byDir.py` script to extract `.fasta` sequences for downstream analyses with [PPRmatcher](https://github.com/ian-small/PPRmatcher).

**Usage**:
```bash
python extractRNAfasta_byDir.py <path_to_input_dir> <path_to_output_dir>
```

### 5. PPRmatcher Per-Repeat Analysis
The `PPRmatcher_perRepeat.jl` script is a modified version of the [PPRmatcher](https://github.com/ian-small/PPRmatcher) tool. It returns PPRmatcher scores per PPR repeat, per sequence.

**Usage**:
```bash
julia PPRmatcher_perRepeat.jl -r ../targetDNA.FASTA -e 16 -o ../dir_to_outputfile.csv ../dir_to_dsn3PLS.motifs.txt ../dir_to_Sample_Input.fasta ../dir_to_Kobayashi.tsv
```

**Notes**:
- Use the `dsn3PLS.motifs.txt` and the `Kobayashi.tsv` files directly from the [PPRmatcher](https://github.com/ian-small/PPRmatcher) repository.
