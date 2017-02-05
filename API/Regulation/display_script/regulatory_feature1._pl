#!/usr/bin/env perl

# -----------------------------
# EnsEMBL Regulation API course
# Regulatory feature 
# Excercise 1
# ----------------------------

use strict;
use warnings;
use Bio::EnsEMBL::Registry;

# Load EnsEMBL Registry
Bio::EnsEMBL::Registry->load_registry_from_db(
    -host => 'ensembldb.ensembl.org',
    -user => 'anonymous'
);

# Get the gene adaptor
my $gene_adaptor = Bio::EnsEMBL::Registry->get_adaptor( 'Human', 'Core', 'Gene' );

# Retrieve all genes with name 'ESPN'
my $gene_name = 'ESPN';
my @genes     = @{ $gene_adaptor->fetch_all_by_external_name($gene_name) };

# Get the splice adaptor
my $slice_adaptor = Bio::EnsEMBL::Registry->get_adaptor( 'Human', 'Core', 'Slice' );

# Get the regulatory feature adaptor
my $regulatory_feature_adaptor = Bio::EnsEMBL::Registry->get_adaptor( 'Human', 'Funcgen', 'Regulatoryfeature' );

# For each of the retrieved genes create a new slice instance
# consisting of the region 1000bp upstream of the TSS of each 'ESPN' gene
foreach my $gene ( @genes ) {

  # Extract the information about the strand, the coordinate system
  # and the chromosome on which the gene is located
  my $strand          = $gene->strand;
  my $coord_system    = $gene->slice->coord_system;
  my $seq_region_name = $gene->seq_region_name;

  # The start coordinate of the new slice is set to 0
  my $slice_start = 0;
  # The end coordinate of the new slice is set to 0
  my $slice_end   = 0;

  # Check on which strand the gene is located and calculate
  # the coordinates of the upstream region accordingly
  if( $gene->strand == 1 )
  {
    $slice_start = $gene->seq_region_start - 1000;
    $slice_end   = $gene->seq_region_start;
  } else
  {
    $slice_start = $gene->seq_region_start;
    $slice_end   = $gene->seq_region_start + 1000;
  }

  # Create a new slice instance for the promoter region
  my $slice_gene = Bio::EnsEMBL::Slice->new(
    -coord_system     => $coord_system,
    -start            => $slice_start,
    -end              => $slice_end,
    -strand           => $strand,
    -seq_region_name  => $seq_region_name,
    -adaptor          => $slice_adaptor,
    );

  my $regulatory_features = $regulatory_feature_adaptor->fetch_all_by_Slice( $slice_gene );

  foreach my $regulatory_feature ( @$regulatory_features ) {
    # Print some regulatory feature info
    print "Regulatory Feature ID:  " . $regulatory_feature->stable_id . "\n";
    print "Regulatory Feature Type:   " . $regulatory_feature->feature_type->name . "\n";
  }
}
