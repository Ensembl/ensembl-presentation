use strict;
use warnings;

use Bio::EnsEMBL::Registry;

my $registry = 'Bio::EnsEMBL::Registry';
$registry->load_registry_from_db(
  -host => 'ensembldb.ensembl.org',
  -user => 'anonymous',
);


my $ld_feature_container_adaptor = $registry->get_adaptor('human', 'variation', 'LDFeatureContainer');
$ld_feature_container_adaptor->db->use_vcf(1);
my $variation_adaptor = $registry->get_adaptor('human', 'variation', 'Variation');
my $population_adaptor = $registry->get_adaptor('human', 'variation', 'Population');
my $slice_adaptor = $registry->get_adaptor('human', 'core', 'Slice');

# 1) LD in a region 
# Compute all LD values for the region chr 12 between 11053716-11073715  and population 1000GENOMES:phase_3:CEU
my $slice = $slice_adaptor->fetch_by_region('chromosome', 12, 11053716, 11073715);
my $population = $population_adaptor->fetch_by_name('1000GENOMES:phase_3:CEU');
my $ldfc = $ld_feature_container_adaptor->fetch_by_Slice($slice, $population);
my $ld_results  = $ldfc->get_all_ld_values;
foreach my $ld_result (@$ld_results) {
  my $d_prime = $ld_result->{d_prime};
  my $r2 = $ld_result->{r2};
  my $variation_name1 = $ld_result->{variation_name1};
  my $variation_name2 = $ld_result->{variation_name2};
  if ($r2 == 1 && $d_prime == 1) {
    print "$variation_name1 $variation_name2 $d_prime $r2\n";
  }
}

# 2) LD for a variation feature Compute all LD values for rs7304579 and population 1000GENOMES:phase_3:YRI

my $variation = $variation_adaptor->fetch_by_name('rs7304579');
my $variation_feature = $variation->get_all_VariationFeatures->[0];
$population = $population_adaptor->fetch_by_name('1000GENOMES:phase_3:YRI');
$ldfc = $ld_feature_container_adaptor->fetch_by_VariationFeature($variation_feature, $population);
$ld_results  = $ldfc->get_all_ld_values;
foreach my $ld_result (@$ld_results) {
  my $d_prime = $ld_result->{d_prime};
  my $r2 = $ld_result->{r2};
  my $variation_name1 = $ld_result->{variation_name1};
  my $variation_name2 = $ld_result->{variation_name2};
  print "$variation_name1 $variation_name2 $d_prime $r2\n";
}

