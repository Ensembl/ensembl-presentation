use strict;
use warnings;
use Bio::EnsEMBL::Registry;

my $registry = "Bio::EnsEMBL::Registry";

$registry->load_registry_from_db( -host => 'ensembldb.ensembl.org', -user => 'anonymous');

my $dafa = $registry->get_adaptor( 'Human', 'Core', 'DnaAlignFeature' );


#find what the refseq dna entry NM_000059 was mapped to

my @dafs = @{$dafa->fetch_all_by_hit_name("NM_000059.3")};

while (my $align = shift @dafs){
  print "\n".$align->db_name."\t";
  print $align->hseqname."\t".$align->hstart."\t".$align->hend."\n";
  print  $align->coord_system_name."\t".$align->seq_region_name."\t".$align->start."\t".$align->end."\n";
  print "aligned with a score of ".$align->score." and percentage identity ".$align->percent_id."\n";
}
