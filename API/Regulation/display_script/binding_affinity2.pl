#!/usr/bin/env perl

# -----------------------------
# EnsEMBL Regulation API course
# Binding affinity
# Excercise 2
# ----------------------------

use strict;
use warnings;
use Bio::EnsEMBL::Registry;
# use feature qw(say);
# use Data::Dumper;

# Load EnsEMBL Registry
Bio::EnsEMBL::Registry->load_registry_from_db(
    -host => 'ensembldb.ensembl.org',
    -user => 'anonymous'
);

my $rf_stable_id = 'ENSR00000000667';

# Get the regulatory feature adaptor
my $regulatory_feature_adaptor = $registry->get_adaptor( 'Human', 'Funcgen', 'Regulatoryfeature' );

# Retrieve the regulatory feature object using the stable identifier
# 

# Get the epigenome adaptor
my $epigenome_adaptor          = $registry->get_adaptor('Human', 'Funcgen', 'Epigenome');

# Retrieve the epigenome object for 'A549'
my $epigenome = $epigenome_adaptor->fetch_by_name('A549');


my @motifs = @{ $rf->get_RegulatoryEvidence('motif',$epigenome)};
say "Found ".scalar @mf . ' binding site motifs in ENSR00000000667';
my $mf = $mf[0];
my $slice_motif = $mf->feature_Slice;
my $seq = $mf->seq;

my $bm = $mf->binding_matrix;
say "Relative affinity of the ".$bm->name." motif\t$seq :".$bm->relative_affinity($seq);
say "Relative affinity of changed motif\tCCCGGCCCCACCCC :".$bm->relative_affinity("CCCGGCCCCACCCC");
say "                                  \t    ^";


# get method_link_species_set object for GERP conservation scores for mammals
my $mlss_a = $registry->get_adaptor("Multi", "compara", "MethodLinkSpeciesSet");
my $mlss   = $mlss_a->fetch_by_method_link_type_species_set_name("GERP_CONSERVATION_SCORE", "mammals");

#Get GERP scores for Motif Feature using the slice
my $display_size = $slice_motif->end - $slice_motif->start + 1;
my $cs_adaptor   = $registry->get_adaptor("Multi", 'compara', 'ConservationScore');
my $scores       = $cs_adaptor->fetch_all_by_MethodLinkSpeciesSet_Slice($mlss, $slice_motif, $display_size);
say join("\t",split('',$seq));


map { printf("%.3f\t", $_->diff_score); } @$scores;
say '';
say '                                ^';

say $bm->frequencies;
say "         ^\n";
