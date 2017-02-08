#!/bin/bash

regulatory_build_file=/home/ensembl/data/RegulatoryBuild/RegBuild.bed

data_directory=/home/ensembl/data/BigWig

wiggletools \
  apply_paste \
    $data_directory/absolute_difference_lung_by_regulatory_feature.bed \
    meanI \
      $regulatory_build_file \
      $data_directory/Lung_H3K27ac_ChIP-Seq_Roadmap85_bwa_samse.bw \
