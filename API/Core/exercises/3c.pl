use strict;
use warnings;
use Bio::EnsEMBL::Registry;
use Bio::SeqIO;

my $registry = "Bio::EnsEMBL::Registry";

$registry->load_registry_from_db( -host => 'ensembldb.ensembl.org', -user => 'anonymous');

my $slice_adaptor = $registry->get_adaptor( 'Human', 'Core', 'Slice' );

# define output as fasta format
my $chromosome_output= Bio::SeqIO->new(
    -file => '>chrom20.fasta',
    -format => 'Fasta'
);

# fetch and write the sequence from chr 20
my $slice = $slice_adaptor->fetch_by_region('chromosome', '20', 1, 1e7);
$chromosome_output->write_seq($slice);

# Get all the genes on the slice
my @genes = @{ $slice->get_all_Genes };

#and print the number of them
print "Number of genes found = ", scalar(@genes), "\n";


