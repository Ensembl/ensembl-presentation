#!/usr/bin/env perl

# -----------------------------
# EnsEMBL Regulation API course
# Microarray - Probe mapping
# Excercise 3
# ----------------------------

use strict;
use warnings;

use Bio::EnsEMBL::Registry;

# Load EnsEMBL Registry
Bio::EnsEMBL::Registry->load_registry_from_db(
    -host => 'ensembldb.ensembl.org',
    -user => 'anonymous'
);

# Define probe of interest
my $array_name = 'HumanWG_6_V2';
my $probe_name = 'ILMN_1763508';

# Get probe adaptor
my $probe_adaptor
    = Bio::EnsEMBL::Registry->get_adaptor( 'Human', 'Funcgen', 'Probe' );

# Fetch probe
my $probe = $probe_adaptor->fetch_by_array_probe_probeset_name( $array_name,
    $probe_name );

# Fetch probe feature adaptor
my $probe_feature_adaptor
    = Bio::EnsEMBL::Registry->get_adaptor( 'Human', 'Funcgen',
    'ProbeFeature' );

# Fetch probe features
my $probe_features = $probe_feature_adaptor->fetch_all_by_Probe($probe);

# Print coordinates
for my $probe_feature (@$probe_features) {
    print 'Probe: '
        . $probe_name . "\t"
        . $probe_feature->slice()->coord_system->name() . "\t"
        . $probe_feature->slice()->seq_region_name() . "\t"
        . 'Start: '
        . $probe_feature->start() . "\t" . 'End: '
        . $probe_feature->end() . "\n";
}
