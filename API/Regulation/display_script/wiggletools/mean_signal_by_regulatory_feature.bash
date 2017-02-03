#!/bin/bash

regulatory_build_file=/nfs/production/panda/ensembl/funcgen/api_course_material/data/RegulatoryBuild/RegBuild.bed

data_dir=/nfs/production/panda/ensembl/funcgen/api_course_material/data/WiggleTools

wiggletools  \
  mwrite_bg  \
  -  \
  meanI    \
  $regulatory_build_file \ 
  $data_dir/Monocytes_CD14_PB_Roadmap_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw  \
  > $data_dir/Monocytes_CD14_PB_Roadmap_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.meanI_per_regfeature.bed  

sort -k5nr \
    $data_dir/Monocytes_CD14_PB_Roadmap_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.meanI_per_regfeature.bed \
  > $data_dir/Monocytes_CD14_PB_Roadmap_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.meanI_per_regfeature.sorted.bed

head -n 10 $data_dir/Monocytes_CD14_PB_Roadmap_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.meanI_per_regfeature.sorted.bed

