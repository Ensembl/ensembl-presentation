use strict;
use warnings;

use Bio::EnsEMBL::Registry;

my $registry = 'Bio::EnsEMBL::Registry';
$registry->load_registry_from_db(
  -host => 'ensembldb.ensembl.org',
  -user => 'anonymous',
);

my $phenotype_feature_adaptor = $registry->get_adaptor('human', 'variation', 'PhenotypeFeature');
$phenotype_feature_adaptor->_include_ontology(1);
my $variation_adaptor = $registry->get_adaptor('human', 'variation', 'Variation');

my $variation = $variation_adaptor->fetch_by_name('rs2470893');

# 1
my $phenotype_features = $phenotype_feature_adaptor->fetch_all_by_Variation($variation);

foreach my $phenotype_feature (@$phenotype_features) {
  my $phenotype_description = $phenotype_feature->phenotype->description;
  my $source_name = $phenotype_feature->source->name;
  my $risk_allele = $phenotype_feature->risk_allele;
  my $p_value = $phenotype_feature->p_value;
  my @ontology_accessions = @{$phenotype_feature->get_all_ontology_accessions}; 
  print "$phenotype_description $source_name $risk_allele $p_value ", join(', ', @ontology_accessions), "\n";
}

# 2
$phenotype_features = $phenotype_feature_adaptor->fetch_all_by_phenotype_accession_source('EFO:0007872');

foreach my $phenotype_feature (@$phenotype_features) {
  my $object_id = $phenotype_feature->object_id;
  my $type = $phenotype_feature->type;
  my $phenotype_description = $phenotype_feature->phenotype->description;
  my $phenotype_source = $phenotype_feature->source->name;
  print "$type $object_id $phenotype_description $phenotype_source\n";
}

