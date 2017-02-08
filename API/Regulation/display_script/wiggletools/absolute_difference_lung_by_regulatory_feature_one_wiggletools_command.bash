#!/bin/bash

regulatory_build_file=/home/ensembl/data/RegulatoryBuild/RegBuild.bed
data_directory=/home/ensembl/data/BigWig

rm -f $data_directory/absolute_difference_lung_by_regulatory_feature.bed

wiggletools \
  apply_paste \
    $data_directory/absolute_difference_lung_by_regulatory_feature.bed \
    meanI \
      $regulatory_build_file \
      abs  \
      diff \
        $data_directory/Lung_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw \
      mean \
        $data_directory/Aorta_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw \
        $data_directory/Fetal_Muscle_Leg_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw \
        $data_directory/K562_H3K27ac_ChIP-Seq_ENCODE85_bwa_samse.bw \
        $data_directory/Monocytes_CD14_PB_Roadmap_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw

sort -k10nr \
  $data_directory/absolute_difference_lung_by_regulatory_feature.bed \
  > $data_directory/absolute_difference_lung_by_regulatory_feature.sorted.bed

head -n 10 $data_directory/absolute_difference_lung_by_regulatory_feature.sorted.bed


