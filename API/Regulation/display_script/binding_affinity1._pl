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

my $motif_dbID = '759795';

# Get the motif adaptor
my $motif_adaptor  = Bio::EnsEMBL::Registry->get_adaptor('Human', 'Funcgen', 'MotifFeature');

# Retrieve all the motifs on the Regulatory feature
my $motif = $motif_adaptor->fetch_by_dbID( $motif_dbID );

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
  
