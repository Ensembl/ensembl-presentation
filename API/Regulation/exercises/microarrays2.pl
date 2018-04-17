use strict;
use warnings;
use feature qw(say);

use Data::Dumper;

use Bio::EnsEMBL::Registry;


# You have performed a microarray experiment with the array "HumanWG_6_V2". The following probes gave you a positive signal: 
# ILMN_1763508, ILMN_1861090, ILMN_1890175, ILMN_1749304, ILMN_1894173, ILMN_1911643, ILMN_1891089, ILMN_1859810, ILMN_1843473,  ILMN_1770856
#  a) Which transcripts do they map to? 
#  b) Which genes do these transcripts belong to? Hint: You need the Transcript Adaptor from Core.


# Load EnsEMBL Registry
Bio::EnsEMBL::Registry->load_registry_from_db(
    -host => 'ensembldb.ensembl.org',
    -user => 'anonymous'
);

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
    say 'Probe Name: ' . $probe->get_probename($array_name);

    my $transript_mappings = $probe->fetch_all_ProbeTranscriptMappings();

    for my $transcript_mapping (@$transript_mappings) {
        print 'Transcript ID: '
            . $transcript_mapping->stable_id() . "\t"
            . 'Matching Details: '
            . $transcript_mapping->description() . "\n";

        push @transcript_ids,
            $transcript_mapping->stable_id();    # this is for 2.b.
    }
    say "------------------------";
}


my $transcript_adaptor
    = Bio::EnsEMBL::Registry->get_adaptor( 'Human', 'Core', 'Transcript' );

for my $transcript_id (@transcript_ids) {
    my $transcript = $transcript_adaptor->fetch_by_stable_id($transcript_id);
    my $gene_id    = $transcript->get_Gene->stable_id();

    print 'Transcript ID: '
        . $transcript_id . "\t"
        . 'Gene ID: '
        . $gene_id . "\n";
}
