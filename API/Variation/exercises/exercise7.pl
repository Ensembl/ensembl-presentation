#!/usr/bin/env perl 

use strict;
use warnings;

use Bio::EnsEMBL::Registry;

my $registry = 'Bio::EnsEMBL::Registry';

$registry->load_registry_from_db(
    -host => 'ensembldb.ensembl.org',
    -user => 'anonymous'
);

# get adaptor
my $va = $registry->get_adaptor("human", "variation", "variation")||die "ERROR: $!\n";

print "\n### Part 1 ###\n";
foreach my $name(qw( rs3730070 rs11765954 rs671 )){

    # get the variation object 
    my $var_obj = $va->fetch_by_name($name);

    # find all publications citing this variant
    my $publications = $var_obj->get_all_Publications();

    foreach my $pub_obj(@{$publications}){

        my $pmid = ($pub_obj->pmid()) ? $pub_obj->pmid() : '';
        my $year = ($pub_obj->year()) ? $pub_obj->year() : '';
	
        printf("%10s | PMID: %8s | Year: %4i | Title: %s\n",
          $name, $pmid, $year, $pub_obj->title());
    }
}

### Extra - get other variants for a publication ###

my $pmid = 18187665;
print "\n### Part 2 ###\n";
print "Variants cited in PMID:$pmid\n";

# get adaptor
my $pa = $registry->get_adaptor("human", "variation", "publication") || die "ERROR: $!\n";
my $pub_obj = $pa->fetch_by_pmid($pmid);
my $variations = $pub_obj->variations;
foreach my $v (@{$variations}){
  print $v->name() . "\n";
}




