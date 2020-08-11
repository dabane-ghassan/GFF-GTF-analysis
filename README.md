# GFF-GTF-analysis




```python
import GeneralFormat as gf 

file_path = "hg38_5k.gtf"
gtf = gf.GeneralFormat(file_path)

gtf.nb_nr_tx() # Number of non-redondant trascripts in the file
gtf.ex_per_tx() # Number of exons per trascript 
gtf.cdna_per_tx() # Length (in bp) of the circular dna for each transcript
gtf.tx_coverage() # Genome coverage (exons+introns) for every transcript
```
