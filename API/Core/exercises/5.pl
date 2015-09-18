use strict;
use warnings;
use Bio::EnsEMBL::Registry;

my $registry = "Bio::EnsEMBL::Registry";

$registry->load_registry_from_db( -host => 'ensembldb.ensembl.org', -user => 'anonymous');

my $gene_adaptor  = $registry->get_adaptor( 'Homo sapiens', 'Core', 'Gene' );

my $gene = $gene_adaptor->fetch_by_display_label('CSNK2A1');
# get exons for all transcripts
my @transcripts = @{ $gene->get_all_Transcripts };
my @exons = @{ $gene->get_all_Exons };

print "Gene ", $gene->display_id, "\n"; 
print scalar(@transcripts), " Transcripts\n";
print scalar(@exons), " Exons\n\n";
print $gene->description, "\n\n";

my $exon_count = 0;

while (my $tr = shift @transcripts) {
  my @t_exons = @{ $tr->get_all_Exons };
  $exon_count += scalar(@t_exons);
  print $tr->display_id." has ".scalar(@t_exons)." Exons\n";
  if ($tr->translation) {
    my $pep = $tr->translate;
    print $pep->seq."\n\n";
  } else {
    print "Transcript ", $tr->stable_id, " is non-coding.\n\n";
  }
}
    
print "Total exon count = ".$exon_count."\n";
