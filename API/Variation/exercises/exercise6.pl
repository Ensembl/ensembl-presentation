#!/usr/bin/env perl 

# find phenotype information for a variant

use strict;
use warnings;

use Bio::EnsEMBL::Registry;

my $registry = 'Bio::EnsEMBL::Registry';

$registry->load_registry_from_db(
    -host => 'ensembldb.ensembl.org',
    -user => 'anonymous'
);


# get variation adaptor
my $va = $registry->get_adaptor('human', 'variation', 'variation'); 

my @variants = ( "rs2470893", "rs6495122");

# fetch variation object 
foreach my  $var_name ( @variants){
  print "\nVariant $var_name\n";

  my $var_obj = $va->fetch_by_name( $var_name );

  # get phenotype features for the variation
  my $phenofeats = $var_obj->get_all_PhenotypeFeatures();


  # loop over phenotype features
  foreach my $pf (@{$var_obj->get_all_PhenotypeFeatures()}) {
    my $phenotype         = $pf->phenotype; # Phenotype object
    my $phe_desc          = $pf->phenotype->description();
    my $source            = $pf->source_name(); # equivalent of $pf->source->name()
    my $p_value           = $pf->p_value() || '-';
    my $risk_allele       = $pf->risk_allele() || '-';
    my $reported_gene     = $pf->associated_gene() || '-'; 


    printf("# Phenotype: %s\n> Source: %18s | p-value: %9s |  Risk allele: %4s | Associated gene(s): %5s \n\n",
      $phe_desc, $source, $p_value, $risk_allele, $reported_gene );
  }
}

### Extra part ###
print "\n\n# Part 2 #\n\n";
print "Frequencies and Ancestral Alleles\n";
# fetch variation object 
foreach my $var_name ( @variants){

  my $var_obj = $va->fetch_by_name( $var_name );
  printf( "Variant: %s | Minor Allele: %4s | Global MAF: %9s | Ancestral Allele: %4s \n", 
      $var_name, $var_obj->minor_allele(), $var_obj->minor_allele_frequency(), $var_obj->ancestral_allele() );
}

