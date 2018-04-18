#!/usr/bin/env perl

# -----------------------------
# EnsEMBL Regulation API course
# Microarray - Probe mapping
# Excercise 2
# ----------------------------

use strict;
use warnings;

use Bio::EnsEMBL::Registry;

# Load EnsEMBL Registry
Bio::EnsEMBL::Registry->load_registry_from_db(
    -host => 'ensembldb.ensembl.org',
    -user => 'anonymous'
);

# --------------
# excercise 2.a.
# --------------

# Define probes of interest
my $array_name  = 'HumanWG_6_V2';
my @probe_names = (
    'ILMN_1763508', 'ILMN_1861090', 'ILMN_1890175', 'ILMN_1749304',
    'ILMN_1894173', 'ILMN_1911643', 'ILMN_1891089', 'ILMN_1859810',
    'ILMN_1843473', 'ILMN_1770856'
);

# Get probe adaptor
my $probe_adaptor
    = Bio::EnsEMBL::Registry->get_adaptor( 'Human', 'Funcgen', 'Probe' );

# Fetch probes
my @probes;

for my $probe_name (@probe_names) {
    push @probes,
        $probe_adaptor->fetch_by_array_probe_probeset_name( $array_name,
        $probe_name );
}

# Fetch transcript mappings
my @transcript_ids;    # this is for 2.b.

for my $probe (@probes) {
    print 'Probe Name: ' . $probe->get_probename($array_name) . "\n";

    my $transript_mappings = $probe->get_all_Transcript_DBEntries();

    for my $transcript_mapping (@$transript_mappings) {
        print 'Transcript ID: '
            . $transcript_mapping->display_id() . "\t"
            . 'Matching Details: '
            . $transcript_mapping->linkage_annotation() . "\n";

        push @transcript_ids,
            $transcript_mapping->display_id();    # this is for 2.b.
    }
    print "------------------------" . "\n";
}

# --------------
# excercise 2.b.
# --------------

my $transcript_adaptor
    = Bio::EnsEMBL::Registry->get_adaptor( 'Human', 'Core', 'Transcript' );

for my $transcript_id (@transcript_ids) {
    my $transcript = $transcript_adaptor->fetch_by_stable_id($transcript_id);
    my $gene_id    = $transcript->get_Gene()->display_id();

    print 'Transcript ID: '
        . $transcript_id . "\t"
        . 'Gene ID: '
        . $gene_id . "\n";
}

