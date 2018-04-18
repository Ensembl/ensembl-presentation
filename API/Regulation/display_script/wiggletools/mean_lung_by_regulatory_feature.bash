#!/bin/bash

regulatory_build_file=/home/ensembl/data/RegulatoryBuild/RegBuild.bed
data_directory=/home/ensembl/data/BigWig

rm -f $data_directory/mean_lung_lung_by_regulatory_feature.bed
rm -f $data_directory/mean_lung_lung_by_regulatory_feature.sorted.bed

wiggletools \
  apply_paste \
    $data_directory/mean_lung_lung_by_regulatory_feature.bed \
    meanI \
      $regulatory_build_file \
      $data_directory/Lung_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw \

sort -k10nr \
  $data_directory/mean_lung_lung_by_regulatory_feature.bed \
  > $data_directory/mean_lung_lung_by_regulatory_feature.sorted.bed

head -n 10 $data_directory/mean_lung_lung_by_regulatory_feature.sorted.bed
