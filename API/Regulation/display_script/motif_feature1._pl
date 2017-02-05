#!/usr/bin/env perl

# -----------------------------
# EnsEMBL Regulation API course
# Motif Feature
# Excercise 1
# ----------------------------

use strict;
use warnings;
use Bio::EnsEMBL::Registry;

# Load EnsEMBL Registry
Bio::EnsEMBL::Registry->load_registry_from_db(
               -host => 'ensembldb.ensembl.org',
               -user => 'anonymous'
);

my $rf_stable_id = 'ENSR00000000667';

# Get the regulatory feature adaptor
my $regulatory_feature_adaptor = Bio::EnsEMBL::Registry->get_adaptor('Human', 'Funcgen', 'RegulatoryFeature');
# Retrieve the regulatory feature object using the stable identifier
my $regulatory_feature = $regulatory_feature_adaptor->fetch_by_stable_id( $rf_stable_id );
# Retrieve the regulatory feature slice
my $rf_slice = $regulatory_feature->feature_Slice;

# Get the motif adaptor
my $motif_adaptor  = Bio::EnsEMBL::Registry->get_adaptor('Human', 'Funcgen', 'MotifFeature');

# Retrieve all the motifs on the Regulatory feature
my @motifs = @{ $motif_adaptor->fetch_all_by_Slice( $rf_slice )};
print "Found ". scalar @motifs . ' transcription factor motifs in ' . $rf_stable_id . "\n";

# For each of the retrfeved motifs print the motif dbID, binding matrix 
# name, the sequence and the relative affinity of that sequence
foreach my $motif ( @motifs ) {
    my $sequence       = $motif->seq;
    my $binding_matrix = $motif->binding_matrix;
    
    print "Relative affinity of motif with ID "
          . $motif->dbID
          . " from matrix "
          . $binding_matrix->name
          . "  with sequence "
          . $sequence
          . " : "
          . $binding_matrix->relative_affinity($sequence)
          . "\n";
}


