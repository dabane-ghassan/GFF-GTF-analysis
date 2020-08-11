# GFF-GTF-analysis

General Feature Format files consist of one line per feature, each containing 9 columns of data. for more information about this file format and its different columns please refer to https://www.ensembl.org/info/website/upload/gff.html.

## Importing the script and initializing the file
```python
import GeneralFormat as gf 
file_path = "hg38_5k.gtf"
gtf = gf.GeneralFormat(file_path)
```

## Getting the number of non-redondant transcripts in the file
```python
gtf.nb_nr_tx() 
```
## Getting the number of exons per transcript
```python
gtf.ex_per_tx() 
```

## Sending back the length (in bp) of the circular dna for each transcript (exons)
```python
gtf.cdna_per_tx() # Length (in bp) of the circular dna for each transcript
```

## Getting the genome coverage (exons+introns) for every transcript in the file
```python
gtf.tx_coverage() # Genome coverage (exons+introns) for every transcript
```

- In each of the cases above, the output will be a dictionary that maps from the transcript to the wished output.
