#!/usr/bin/env perl 

use strict;
use warnings;

use Bio::EnsEMBL::Registry;

my $registry = 'Bio::EnsEMBL::Registry';

$registry->load_registry_from_db(
    -host => 'ensembldb.ensembl.org',
    -user => 'anonymous'
);

# get variation adaptor
my $v_adaptor = $registry->get_adaptor("human", "variation", "variation")||die "ERROR: $!\n";

# Set a flag on the variation adaptor to use VCF files for genotype
# extraction as well as the MySQL database
$v_adaptor->db->use_vcf(1);


# fetch variation object
my $var_obj = $v_adaptor->fetch_by_name('rs1333049');

# fetch all genotypes
my $sample_genos = $var_obj->get_all_SampleGenotypes();
my @sorted_sample_genos = sort {$a->sample()->name() cmp $b->sample()->name()} @{$sample_genos};

foreach my $sample_geno_obj(@sorted_sample_genos){
   
  printf("Genotype: %3s,  Sample: %27s,  Gender: %6s,  Submitter: %s\n", 
         $sample_geno_obj->genotype_string(),
         $sample_geno_obj->sample()->name(),
         $sample_geno_obj->sample()->individual()->gender(),
         (defined($sample_geno_obj->subsnp_handle()) ? $sample_geno_obj->subsnp_handle() : "-")
        );
}
