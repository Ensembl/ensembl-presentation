#!/bin/bash

regulatory_build_file=/nfs/production/panda/ensembl/funcgen/api_course_material/data/RegulatoryBuild/RegBuild.bed

data_dir=/nfs/production/panda/ensembl/funcgen/api_course_material/data/WiggleTools

wiggletools \
  write
    $data_dir/mean_signal.bw \
  mean \
    $data_dir/Aorta_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw \
    $data_dir/Fetal_Muscle_Leg_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw \
    $data_dir/K562_H3K27ac_ChIP-Seq_ENCODE85_bwa_samse.bw \
    $data_dir/Monocytes_CD14_PB_Roadmap_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw
