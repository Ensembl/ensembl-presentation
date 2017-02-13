#!/bin/bash

regulatory_build_file=/home/ensembl/data/RegulatoryBuild/RegBuild.bed
data_directory=/home/ensembl/data/BigWig

mean_signal_file=$data_directory/mean_signal.wig

rm -f $mean_signal_file

wiggletools \
  write \
    $mean_signal_file \
  mean \
    $data_directory/Aorta_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw \
    $data_directory/Fetal_Muscle_Leg_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw \
    $data_directory/K562_H3K27ac_ChIP-Seq_ENCODE85_bwa_samse.bw \
    $data_directory/Monocytes_CD14_PB_Roadmap_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw

absolute_difference_file=$data_directory/absolute_difference_file.wig

rm $absolute_difference_file

wiggletools \
  write \
    $absolute_difference_file \
      abs  \
      diff \
        $data_directory/Lung_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw \
        $mean_signal_file

rm -f $data_directory/absolute_difference_lung_by_regulatory_feature.bed

wiggletools \
  apply_paste \
    $data_directory/absolute_difference_lung_by_regulatory_feature.bed \
    meanI \
      $regulatory_build_file \
      $absolute_difference_file

sort -k10nr \
  $data_directory/absolute_difference_lung_by_regulatory_feature.bed \
  > $data_directory/absolute_difference_lung_by_regulatory_feature.sorted.bed

head -n 10 $data_directory/absolute_difference_lung_by_regulatory_feature.sorted.bed
