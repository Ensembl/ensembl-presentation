#!/bin/bash

regulatory_build_file=/home/ensembl/data/RegulatoryBuild/RegBuild.bed
regulatory_build_chromosome_22_file=/home/ensembl/data/RegulatoryBuild/RegBuild.chromosome22.bed

grep -e "^22" $regulatory_build_file > $regulatory_build_chromosome_22_file

echo Features on chromosome 22 have been written to ${regulatory_build_chromosome_22_file}.

# See also in browser:
# http://www.ensembl.org/Homo_sapiens/Location/View?r=1%3A203290000-203290200
