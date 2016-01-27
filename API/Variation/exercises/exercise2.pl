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
my $v_adaptor = $reg->get_adaptor("human", "variation", "variation");

# Set a flag on the variation adaptor to use VCF files for genotype
# extraction as well as the MySQL database
$v_adaptor->db->use_vcf(1);

# fetch the variation by name
my $variation = $v_adaptor->fetch_by_name('rs1333049');

# get all the alleles
my @alleles = @{$variation->get_all_Alleles()};

print "Variation name: ", $variation->name, "\n";

foreach my $allele(@alleles) {
    
  my $allele_frequency = (defined($allele->frequency)) ? sprintf("%.2f", $allele->frequency) : "-";
  
  printf("Allele: %1s  Frequency: %4s  Population: %46s  Submitter: %s\n", 
         $allele->allele,
         $allele_frequency,
         (defined($allele->population) ? $allele->population->name : "-"),
         (defined($allele->subsnp_handle) ? $allele->subsnp_handle : "-")
        );
}
