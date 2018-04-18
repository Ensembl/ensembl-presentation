#!/bin/bash

data_directory=/home/ensembl/data/BigWig

wiggletools \
  write \
    ./sums_deleteme.wig \
  sum  \
    $data_directory/Monocytes_CD14_PB_Roadmap_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw  \
    $data_directory/Lung_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw  \
    $data_directory/Fetal_Muscle_Leg_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw \
    $data_directory/Aorta_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw \
    $data_directory/K562_H3K27ac_ChIP-Seq_ENCODE85_bwa_samse.bw


