#!/usr/bin/env perl
use strict;
use warnings;

use Bio::EnsEMBL::Registry;

my $reg = 'Bio::EnsEMBL::Registry';

$reg->load_registry_from_db(
  -host => 'ensembldb.ensembl.org',
  -user => 'anonymous'
);

# get transcriptvariation adaptor from variation database
my $tv_adaptor = $reg->get_adaptor("human", "variation", "transcriptvariation");

# get transcript adaptor from core 
my $t_adaptor = $reg->get_adaptor("human", "core", "transcript");

# fetch the transcript
my $transcript = $t_adaptor->fetch_by_stable_id('ENST00000001008');


####################################
# 1 - get all TranscriptVariations #
####################################

my $tvs = $tv_adaptor->fetch_all_by_Transcripts([$transcript]);

print 'Number of TranscriptVariations (germline): ', scalar @{$tvs}, "\n";


# loop through transcript variation objects printing out required information
foreach my $tv_obj (@{$tvs}) {	
  my $variation_name     = $tv_obj->variation_feature->variation_name;
  my $consequence_term   = $tv_obj->display_consequence;
  my $amino_acid_change  = $tv_obj->pep_allele_string || '-';
  my $cdna_coords        = (defined $tv_obj->cdna_start) ? $tv_obj->cdna_start.'-'.$tv_obj->cdna_end : '-'; 
  my $translation_coords = (defined $tv_obj->translation_start) ? $tv_obj->translation_start.'-'.$tv_obj->translation_end : '-';

  printf("Var name: %26s | Most severe consequence: %23s | Peptide change: %4s | cDNA location: %9s | Peptide location: %s\n",
         $variation_name, $consequence_term, $amino_acid_change, $cdna_coords, $translation_coords);

}


####################################################################################
# 2 - filter for TranscriptVariations with the consequence term "missense_variant" #  
####################################################################################
my @filtered_tvs = @{$tv_adaptor->fetch_all_by_Transcripts_SO_terms([$transcript], ['missense_variant'])};
print "\nNumber of TranscriptVariations (germline) with SO term 'missense_variant': ", scalar @filtered_tvs, "\n\n";


