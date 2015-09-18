use strict;
use warnings;
use Bio::EnsEMBL::Registry;

my $registry = "Bio::EnsEMBL::Registry";

$registry->load_registry_from_db(
  -host => 'ensembldb.ensembl.org',
  -user => 'anonymous'
);

my $gene_adaptor = $registry->get_adaptor( 'Human', 'Core', 'Gene' );

my $gene = $gene_adaptor->fetch_by_stable_id('ENSG00000139618');

my $all_xrefs = $gene->get_all_DBLinks('GO');

my $ontology_term_adaptor =
  $registry->get_adaptor( 'Multi', 'Ontology', 'OntologyTerm' );

while (my $all_xref = shift @{$all_xrefs} ) {
  my $go_term =
    $ontology_term_adaptor->fetch_by_accession( $all_xref->display_id );
  if ($go_term) {
    print $go_term->accession, " ", $go_term->name, "\n";
  }
}
