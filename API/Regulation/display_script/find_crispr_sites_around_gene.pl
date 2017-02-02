#!/usr/bin/env perl

# -----------------------------
# EnsEMBL Regulation API course
# CRISPR
# Excercise 2
# ----------------------------

use strict;
use warnings;

use Bio::EnsEMBL::Registry;

# Load EnsEMBL Registry
Bio::EnsEMBL::Registry->load_registry_from_db(
    -host => 'ensembldb.ensembl.org',
    -user => 'anonymous'
);

# Get the array adaptor
my $gene_adaptor
    = Bio::EnsEMBL::Registry->get_adaptor( 'Human', 'Core', 'Gene' );

# Fetch all 'SERTM1' genes
my @genes = @{$gene_adaptor->fetch_all_by_external_name('SERTM1')};

# Define the CRISPR bigBed file location 
my $crispr_file_location = "/home/ensembl/data/Crispr/wge_crisprs_grch38.bb";

# For each of the retrieved genes  
foreach my $gene (@genes) {

    # The start coordinate of the region of interest is set 500bp upstream
    my $region_start = $gene->seq_region_start - 500;
    # The end coordinate of the region of interest is set 500bp downstream
    my $region_end = $gene->seq_region_end + 500;
    # Store the gene name in a variable
    my $gene_name = $gene->external_name;
    
    # Print the following message
    print "Extracting CRISPR sites around gene "
          . $gene_name 
          . "\n";
    # Define the name of the output BED file
    my $output_bed_file = "CRISPR_500bp_around_gene_" . $gene_name . ".bed";
    
    # Create the bigBed command using the genomic coordinates computed above
    my $command = "bigBedToBed -chrom=chr" 
                  . $gene->seq_region_name
                  . " -start="
                  . $region_start
                  . " -end="
                  . $region_end
                  . " " . $crispr_file_location 
                  . " " . $output_bed_file;
    
    # Run the bigBed command
    system($command);
}

