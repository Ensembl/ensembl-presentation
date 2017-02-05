#!/usr/bin/perl
use strict;
use warnings;
use Bio::EnsEMBL::Registry;
use feature qw(say);
use Data::Dumper;

# Set to run for test with new release. Tested on: e87
my $test = 1;

# Genes are often regulated by regulatory elements like promoters which are upstream of the gene.
# Transcription Factors often bind in these regions and influence the expression level of the gene.
# In this exercise you will get the coordinates upstream of a gene and  identify the regulatory element(s) there.
# Then you will look which TF Binding site motifs are found, what their affinity is and how a mutation can affect it.
# Binding Matrices and motif strength
# Each MotifFeature is associated with a PWM, which are represented by the 'BindingMatrix' class.
# The MotifFeature score represents the relative binding affinity with respect to the PWM defined in the BindingMatrix.
# Check potential effect of changes in the sequence of the motif feature on the relative strength of that motif feature.

# Fetch the gene with the external name ESPN
# Get the feature slice object linked to the gene
# Expand the slice by 1000bp to the 5' end
# Shorten the slice so it ends at the starting position (Hint: use the negative length of the slice for that)
# Fetch all regulatory features on that slice
# Print out (XXXXXXX what do we want here? Depends on other exercises)
# Fetch the epigenome HUVEC
# Get the motifs of the Transcription Factors which bind in that region via the regulatory evidence for the HUVEC epigenome
# Use the first Motif that you found
# Get the motif sequence
# Get the feature slice of the motif sequence
# Print the binding matrix name, the motif sequence and the relative affinity of the binding matrix
# Change the C at position 5 to a G
# Print the relative affinity of the binding matrix again
#
# Promoter region.
# Poised in all except:
# Active in EPC(VB), Gastric, HMEC, HUVEC,
# Repressed: DND-41, HSMM, IMR90, Monocytes-CD14+ (PB) Roadmap, Ovary, Small Interstine,


# Load Registry

my $registry = 'Bio::EnsEMBL::Registry';
$registry->load_registry_from_db(
    -host => 'ensembldb.ensembl.org',
    -user => 'anonymous'
);

my $gene_a  = $registry->get_adaptor('Human', 'core', 'gene');
my $slice_a = $registry->get_adaptor('Human', 'core', 'slice');
my $rfa     = $registry->get_adaptor('Human', 'funcgen', 'regulatoryfeature');

my $gene_name = 'ESPN';
my @genes     = @{ $gene_a->fetch_all_by_external_name($gene_name) };

#say 'Found ' . scalar(@genes) . " gene(s) named $gene_name"  ;

if($test and scalar(@genes) != 1){
  die 'Check exercise, more than 1 gene returned';
}

my $espn_gene = shift @genes;

my $start           = $espn_gene->seq_region_start;
my $end             = $espn_gene->seq_region_start - 1000;
my $strand          = $espn_gene->strand;
my $coord_system    = $espn_gene->slice->coord_system;
my $seq_region_name = $espn_gene->seq_region_name;

my $slice_gene = Bio::EnsEMBL::Slice->new(
  -coord_system     => $coord_system,
  -start            => $start,
  -end              => $end,
  -strand           => $strand,
  -seq_region_name  => $seq_region_name,
  -adaptor          => $slice_a,
);

## Alternative way
## slice_gene   : 1: 6424788-6461370
## regfeat: 1: 6422771-6425891
## 1st argument expands the 5' by 1000bp
## 2nd argument shortens 3' by the length of the gene, hence gives us the start

#my $slice_gene = $espn_gene->feature_Slice();
#my $new_end = -1 * ($slice_gene->length);
#$slice_gene = $slice_gene->expand(1000, $new_end);
#

my $rfs = $rfa->fetch_all_by_Slice($slice_gene);
my $rf = $rfs->[0];

if($test){
  if(scalar @$rfs != 1){
    die 'Check exercise, more than one RegulatoryFeature returned';
  }
  if($rf->stable_id ne 'ENSR00000000667'){
    die 'Check exercise, StableID ENSR00000000667 expected, not: '. $rf->stable_id;
  }
}

my $epg_a     = $registry->get_adaptor('Human', 'funcgen', 'epigenome');
my $epigenome = $epg_a->fetch_by_name('A549');


my @mf = @{$rf->get_RegulatoryEvidence('motif',$epigenome)};
say "Found ".scalar @mf . ' binding site motifs in ENSR00000000667';
my $mf = $mf[0];
my $slice_motif = $mf->feature_Slice;
my $seq = $mf->seq;

my $bm = $mf->binding_matrix;
say "Relative affinity of the ".$bm->name." motif\t$seq :".$bm->relative_affinity($seq);
say "Relative affinity of changed motif\tCCCGGCCCCACCCC :".$bm->relative_affinity("CCCGGCCCCACCCC");
say "                                  \t    ^";


# get method_link_species_set object for GERP conservation scores for mammals
my $mlss_a = $registry->get_adaptor("Multi", "compara", "MethodLinkSpeciesSet");
my $mlss   = $mlss_a->fetch_by_method_link_type_species_set_name("GERP_CONSERVATION_SCORE", "mammals");

#Get GERP scores for Motif Feature using the slice
my $display_size = $slice_motif->end - $slice_motif->start + 1;
my $cs_adaptor   = $registry->get_adaptor("Multi", 'compara', 'ConservationScore');
my $scores       = $cs_adaptor->fetch_all_by_MethodLinkSpeciesSet_Slice($mlss, $slice_motif, $display_size);
say join("\t",split('',$seq));


map { printf("%.3f\t", $_->diff_score); } @$scores;
say '';
say '                                ^';

say $bm->frequencies;
say "         ^\n";

