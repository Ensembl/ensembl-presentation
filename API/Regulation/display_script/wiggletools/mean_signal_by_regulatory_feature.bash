#!/bin/bash

regulatory_build_file=/home/ensembl/data/RegulatoryBuild/RegBuild.bed
data_directory=/home/ensembl/data/BigWig

wiggletools  \
  mwrite_bg  \
  -  \
  meanI    \
  $regulatory_build_file \
  $data_directory/Monocytes_CD14_PB_Roadmap_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw  \
  > $data_directory/Monocytes_CD14_PB_Roadmap_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.meanI_per_regfeature.bed  

sort -k5nr \
    $data_directory/Monocytes_CD14_PB_Roadmap_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.meanI_per_regfeature.bed \
  > $data_directory/Monocytes_CD14_PB_Roadmap_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.meanI_per_regfeature.sorted.bed

head -n 10 $data_directory/Monocytes_CD14_PB_Roadmap_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.meanI_per_regfeature.sorted.bed

