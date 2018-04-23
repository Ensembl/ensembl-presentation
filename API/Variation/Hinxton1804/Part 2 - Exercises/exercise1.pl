#!/usr/bin/env perl

use strict;
use warnings;

use Bio::EnsEMBL::Registry;

my $reg = 'Bio::EnsEMBL::Registry';

$reg->load_registry_from_db(
    -host => 'ensembldb.ensembl.org',
    -user => 'anonymous'
);

# get a variation adaptor
my $va = $reg->get_adaptor("human", "variation", "variation");

# iterate through the variations
foreach(qw(rs1333049 rs56385407 COSM998 CI003207)) {
  my $v = $va->fetch_by_name($_);
	
  print "Variation ", $v->name(), " is a ", $v->var_class(), " and comes from ", $v->source_name(), "\n";
}

# get a platypus variation adaptor
my $va_platypus = $reg->get_adaptor("platypus", "variation", "variation");
my $v_platypus = $va_platypus->fetch_by_name('rs69772326');

# Print from the new variation object
print "Variation ", $v_platypus->name(), " is a ", $v_platypus->var_class(), " and comes from ", $v_platypus->source_name(), "\n";





