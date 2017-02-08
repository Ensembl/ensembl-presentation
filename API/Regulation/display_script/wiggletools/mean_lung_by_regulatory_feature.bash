#!/bin/bash

regulatory_build_file=/nfs/production/panda/ensembl/funcgen/api_course_material/data/RegulatoryBuild/RegBuild.bed

data_dir=/nfs/production/panda/ensembl/funcgen/api_course_material/data/WiggleTools

wiggletools \
  apply_paste \
    $data_dir/absolute_difference_lung_by_regulatory_feature.bed \
    meanI \
      $regulatory_build_file \
      $data_dir/Lung_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw \
