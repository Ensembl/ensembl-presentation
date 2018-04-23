use strict;
use warnings;

use Bio::EnsEMBL::Registry;

my $registry = 'Bio::EnsEMBL::Registry';
$registry->load_registry_from_db(
  -host => 'ensembldb.ensembl.org',
  -user => 'anonymous',
);

my $population_adaptor = $registry->get_adaptor('human', 'variation', 'population');
my $variation_adaptor = $registry->get_adaptor('human', 'variation', 'variation');

$variation_adaptor->db->use_vcf(1);

my $variation = $variation_adaptor->fetch_by_name('rs4988235');

# 1
my $alleles = $variation->get_all_Alleles();

foreach my $allele (@$alleles) {
  my $allele_string = $allele->allele;
  my $population = $allele->population; 
  my $frequency = $allele->frequency;
  my $count = $allele->count || 'NA';
  if ($population && $frequency) {
    my $population_name = $population->name;
    if ($population_name =~ /gnomad|topmed|twinsuk|alspac/i) {
      print "$allele_string $population_name $frequency $count\n";
    }
  }
}

# 2
foreach my $allele (@$alleles) {
  my $allele_string = $allele->allele;
  my $population = $allele->population; 
  my $frequency = $allele->frequency;
  my $count = $allele->count || 'NA';
  if ($population && $frequency) {
    my $population_name = $population->name;
    if ($population_name =~ /1000GENOMES:phase_3:FIN|1000GENOMES:phase_3:CHB|1000GENOMES:phase_3:ASW/i) {
      print "$allele_string $population_name $frequency $count\n";
    }
  }
}

my $population = $population_adaptor->fetch_by_name('1000GENOMES:phase_3:ACB');

# 3
my $sample_genotypes = $variation->get_all_SampleGenotypes($population);
foreach my $sample_genotype(@$sample_genotypes) {
  my $sample_name = $sample_genotype->sample->name;
  my $genotype_string = $sample_genotype->genotype_string;
  if ($genotype_string eq 'A|G' || $genotype_string eq 'G|A') {
    print "$sample_name $genotype_string\n";
  }
}

# 4
my $population_genotypes = $variation->get_all_PopulationGenotypes($population);
foreach my $population_genotype (@$population_genotypes) {
  my $population_name = $population_genotype->population->name; 
  my $genotype_string = $population_genotype->genotype_string;
  my $frequency = $population_genotype->frequency;
  my $count = $population_genotype->count;
  print "$population_name $genotype_string $frequency $count\n";
}

