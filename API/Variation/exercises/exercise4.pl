#!/usr/bin/env perl

use strict;
use warnings;

use Bio::EnsEMBL::Registry;

my $registry = 'Bio::EnsEMBL::Registry';

$registry->load_registry_from_db(
  -host => 'ensembldb.ensembl.org',
  -user => 'anonymous'
);

############################################################################
# 1 - Retrieve variation features on region of interest                    #
# http://www.ensembl.org/Homo_sapiens/Location/View?r=13:48987260-48990000 #
############################################################################
print "# Part 1 #\n";

# get variation feature adaptor
my $variationfeature_adaptor = $registry->get_adaptor('human', 'variation', 'variationfeature');

# get slice adaptor 
my $slice_adaptor = $registry->get_adaptor('human', 'core', 'slice');

# get a slice for this region
my $slice = $slice_adaptor->fetch_by_region('chromosome', 13, 48987260, 48990000);

# get all variation features in this region
my @vfs = @{$variationfeature_adaptor->fetch_all_by_Slice($slice)};

# loop over variation features located in the given region
foreach my $vf (@vfs) {

  printf("Variation: %11s | Alleles: %4s | Location: %s:%i-%i\n", 
         $vf->variation_name,
         $vf->allele_string,
         $vf->seq_region_name,
         $vf->seq_region_start,
         $vf->seq_region_end
  );
}
print "\n";


###################################################
# 2 - Get locations for a list of variation names #
###################################################
print "# Part 2 #\n";
# Get location from API object -> Variation

my @variation_names = ('rs7107418', 'rs671', 'rs17646946', 'rs4988235');

# get variation adaptor 
my $va = $registry->get_adaptor('human', 'variation', 'variation');

foreach my $name (@variation_names) {
  my $variation = $va->fetch_by_name($name);

  # get all variation features for our variation:
  my @vfs = @{$variation->get_all_VariationFeatures()};
  foreach my $vf (@vfs) {
    
    printf("Variation: %10s | Alleles: %5s | Location: %s:%i-%i\n", 
         $vf->variation_name,
         $vf->allele_string,
         $vf->seq_region_name,
         $vf->seq_region_start,
         $vf->seq_region_end
    );
  }
}



