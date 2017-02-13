#!/bin/bash

regulatory_build_file=/home/ensembl/data/RegulatoryBuild/RegBuild.bed
data_directory=/home/ensembl/data/BigWig

rm -f $data_directory/absolute_difference_lung_by_regulatory_feature_one_command.bed

wiggletools \
  apply_paste \
    $data_directory/absolute_difference_lung_by_regulatory_feature_one_command.bed \
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
  $data_directory/absolute_difference_lung_by_regulatory_feature_one_command.bed \
  > $data_directory/absolute_difference_lung_by_regulatory_feature_one_command.sorted.bed

head -n 10 $data_directory/absolute_difference_lung_by_regulatory_feature_one_command.sorted.bed

# See:
# http://dec2016.archive.ensembl.org/Homo_sapiens/Share/27401dc122354ce8e0e4541be61f35c3?redirect=no;mobileredirect=no
