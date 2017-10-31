#!/bin/env perl

# Use the /lookup endpoint to find IRAK4,and map the coordinates for
# the gene to the GRCh37 assembly.

use strict;
use warnings;

use HTTP::Tiny;
use JSON;
use Data::Dumper;
$Data::Dumper::Terse = 1;
$Data::Dumper::Indent = 1;

my $server = "http://rest.ensembl.org";
my $lookup_endpoint = "/lookup/symbol/human/%s";
my $lookup_endpoint_expand = "/lookup/symbol/human/%s?expand=1";
my $mapping_endpoint = "/map/human/GRCh38/%s:%d..%d/GRCH37";
my $sequence_endpoint = "/sequence/id/%s";

my $http = HTTP::Tiny->new();

# Fetch an endpoint from the serverm allow overriding of the default content type
sub fetch_endpoint {
    my ($request, $content_type) = @_;
    $content_type ||= 'application/json';

    my $response = $http->get($request,
                              { headers => { 'Content-type' => $content_type } } );

    die "Failed!\n" unless $response->{success};

    if($content_type eq 'application/json') {
	return decode_json($response->{content});
    } else {
	return $response->{content};
    }
}

print "Fetching gene IRAK4\n";

my $url = $server . sprintf($lookup_endpoint_expand, 'IRAK4');
my $gene = fetch_endpoint($url);

print "Stable id: " . $gene->{id} . "\n";

print "We found transcripts:\n";

# Look through and print the transcripts
foreach my $transcript (@{$gene->{Transcript}}) {
    print "\t" . $transcript->{id} . "\n";
}
print "\n";

$url = $server. sprintf($mapping_endpoint,
			$gene->{seq_region_name},
			$gene->{start},
			$gene->{end});
my $mapped = fetch_endpoint($url);

# We're cheating, because we know in this case there is only one mapping.
# In reality we should be iterating through the array of mappings as their
# could be gaps in how the region maps between assemblies.
my $grch37_mapped = $mapped->{mappings}->[0]->{mapped};
printf "IRAK4 on GRCH37 is: %s:%d-%d\n\n", $grch37_mapped->{seq_region_name},
                                         $grch37_mapped->{start},
                                         $grch37_mapped->{end};

$url = $server . sprintf($sequence_endpoint, $gene->{id});
my $sequence = fetch_endpoint($url, 'text/x-fasta');
print $sequence;
