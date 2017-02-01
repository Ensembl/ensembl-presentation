#!/bin/bash

crispr_file_location=/home/ensembl/data/Crispr/wge_crisprs_grch38.bb

bigBedToBed -chrom=chr13 -start=32315474 -end=32400266 $crispr_file_location deleteme.bed

number_of_crispr_sites_found=`wc -l deleteme.bed | cut -f 1 -d " "`

echo $number_of_crispr_sites_found crispr sites were found at the specified location.
