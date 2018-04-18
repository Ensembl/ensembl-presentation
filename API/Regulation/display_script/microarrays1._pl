use strict;
use warnings;
use feature qw(say);
use Data::Dumper;

use Bio::EnsEMBL::Registry;

# Find all microarray platforms that are annotated for humans in Ensembl and print their associated information.
# Hint: Check the ArrayChip object


# Load EnsEMBL Registry
Bio::EnsEMBL::Registry->load_registry_from_db(
    -host => 'ensembldb.ensembl.org',
    -user => 'anonymous'
);

# Get the array adaptor
my $array_adaptor
    = Bio::EnsEMBL::Registry->get_adaptor( 'Human', 'Funcgen', 'Array' );

# Fetch all arrays
my $arrays = $array_adaptor->fetch_all;

my $data = [];

foreach my $current_array (@$arrays) {
  my $result = {};
  $result->{Array} = $current_array->name;
  $result->{Type} = $current_array->type;
  $result->{Vendor} = $current_array->vendor;
  # Fetch the array chips of the current array
  my $array_chips = $current_array->get_ArrayChips;
  #Print some ArrayChip info
  foreach my $current_array_chip (@$array_chips) {
    push(@{$result->{ArrayChip}}, $current_array_chip->name);
    push(@{$result->{DesignID}},  $current_array_chip->design_id);
  }
  push(@{$data}, $result);
}
say Dumper($data);



# Step-by-step printing
#foreach my $current_array (@$arrays) {
#
#    # Print some array info
#    print "Array:  " . $current_array->name . "\n";
#    print "Type:   " . $current_array->type . "\n";
#    print "Vendor: " . $current_array->vendor . "\n";
#
#    # Fetch the array chips of the current array
#    my $array_chips = $current_array->get_ArrayChips;
#
#    #Print some ArrayChip info
#    foreach my $current_array_chip (@$array_chips) {
#        print "ArrayChip: "
#            . $current_array_chip->name
#            . " DesignID: "
#            . $current_array_chip->design_id . "\n";
#    }
#    print "\n";
#}
#
#
