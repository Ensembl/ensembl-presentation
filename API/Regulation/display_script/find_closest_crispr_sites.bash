#!/bin/bash

crispr_file_location=/home/ensembl/data/Crispr/wge_crisprs_grch38.bb

bigBedToBed -chrom=chr4 -start=121819383 -end=121819583 $crispr_file_location crispr_sites_200bp.bed

printf "%s\t%d\t%d\t%s\t%d\t%s" chr4 121819482 121819483 "random position" 0 - > genomic_position_of_interest.bed

bedtools closest -d -wb -a genomic_position_of_interest.bed -b crispr_sites_200bp.bed
