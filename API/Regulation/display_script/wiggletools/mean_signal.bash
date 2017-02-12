#!/bin/bash

regulatory_build_file=/home/ensembl/data/RegulatoryBuild/RegBuild.bed
data_directory=/home/ensembl/data/BigWig

rm -f $data_directory/mean_signal.bw

wiggletools \
  write \
    $data_directory/mean_signal.bw \
  mean \
    $data_directory/Aorta_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw \
    $data_directory/Fetal_Muscle_Leg_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw \
    $data_directory/K562_H3K27ac_ChIP-Seq_ENCODE85_bwa_samse.bw \
    $data_directory/Monocytes_CD14_PB_Roadmap_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw

echo The result is in $data_directory/mean_signal.bw
