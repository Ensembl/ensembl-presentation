#!/usr/bin/env perl

# -----------------------------
# EnsEMBL Regulation API course
# Binding affinity
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

# Loop through the motifs until you found the one 
# for matrix 'PB0010.1' with sequence 'CCCGCCCCCACCCC'
foreach my $motif ( @motifs ) {

    if ( $motif->binding_matrix->name eq 'PB0010.1' && $motif->seq eq 'CCCGCCCCCACCCC') {

        # Calculate the relative binding affinity of this motif 
        my $slice             = $motif->feature_Slice;
        my $sequence          = $motif->seq;
        my $binding_matrix    = $motif->binding_matrix;
        my $relative_affinity = $binding_matrix->relative_affinity($sequence);

        print "Relative affinity of the "
              . $binding_matrix->name
              . " motif with sequence\t"
              . $sequence
              . " : "
              . $relative_affinity ."\n";

        # Calculate the relative binding affinity of the changed motif 
        my $changed_sequence          = "CCCGGCCCCACCCC";
        my $changed_relative_affinity = $binding_matrix->relative_affinity($changed_sequence);

        print "Relative affinity of the "
              . $binding_matrix->name
              . " motif with sequence\t"
              . $changed_sequence
              . " : "
              . $changed_relative_affinity ."\n";

        print "                                                \t    ^\n";
    }
}
  
