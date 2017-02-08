#!/bin/bash

regulatory_build_file=/home/ensembl/data/RegulatoryBuild/RegBuild.bed
regulatory_build_chromosome_22_file=/home/ensembl/data/RegulatoryBuild/RegBuild.chromosome22.bed

grep -e "^22" $regulatory_build_file > $regulatory_build_chromosome_22_file