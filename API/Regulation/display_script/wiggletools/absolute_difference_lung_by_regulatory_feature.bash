#!/bin/bash

regulatory_build_file=/nfs/production/panda/ensembl/funcgen/api_course_material/data/RegulatoryBuild/RegBuild.bed

data_dir=/nfs/production/panda/ensembl/funcgen/api_course_material/data/WiggleTools

wiggletools \
  apply_paste \
    $data_dir/absolute_difference_lung_by_regulatory_feature.bed \
    meanI \
      $regulatory_build_file \
      abs  \
      diff \
        $data_dir/Lung_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw \
      mean \
        $data_dir/Aorta_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw \
        $data_dir/Fetal_Muscle_Leg_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw \
        $data_dir/K562_H3K27ac_ChIP-Seq_ENCODE85_bwa_samse.bw \
        $data_dir/Monocytes_CD14_PB_Roadmap_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw
