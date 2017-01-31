use strict;
use warnings;
use Bio::EnsEMBL::Registry;

my $registry = "Bio::EnsEMBL::Registry";

$registry->load_registry_from_db( -host => 'ensembldb.ensembl.org', -user => 'anonymous');


my $slice_adaptor = $registry->get_adaptor( 'Human', 'Core', 'Slice' );

my @slices = @{ $slice_adaptor->fetch_all_karyotype() };
print "Number of chromosomes:" . scalar(@slices) . "\n";
while (my $slice = shift @slices) {
  print $slice->seq_region_name, "\t", $slice->length , "\n";
}

