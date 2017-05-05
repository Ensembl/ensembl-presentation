#!/bin/env perl

# Use the /lookup endpoint to find IRAK4, print all transcript stable id(s)
# Loop through the transcripts and fetch the sequences and print

use strict;
use warnings;

use HTTP::Tiny;
use JSON;
use Data::Dumper;
$Data::Dumper::Terse = 1;
$Data::Dumper::Indent = 1;

my $server = "http://rest.ensembl.org";
my $lookup_endpoint_expand = "/lookup/symbol/human/%s?expand=1";
my $sequence_endpoint = "/sequence/id";

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

# Fetch an endpoint using POST, allowing overriding of default content-type
sub fetch_endpoint_POST {
    my ($request, $data, $content_type) = @_;
    $content_type ||= 'application/json';

    my $response = $http->request('POST', $request,
                                  { headers => { 'Content-type' => $content_type },
                                    content => $data } );

    die "Failed!\n" unless $response->{success};

    if($content_type eq 'application/json') {
	return decode_json($response->{content});
    } else {
	return $response->{content};
    }
}

print "Fetching gene IRAK4\n";

# Fetch the record for the gene IRAK4
my $url = $server . sprintf($lookup_endpoint_expand, 'IRAK4');
my $gene = fetch_endpoint($url);

# Extract the stable id from the dictionary and print
print "Stable id: " . $gene->{id} . "\n";

my @transcripts;
foreach my $transcript (@{$gene->{Transcript}}) {
    push @transcripts, $transcript->{id};
}
 
# Create the data body to be sent to the server
my $data = encode_json( { ids => \@transcripts } );

# Fetch the sequences as a single POST call
my $sequences = fetch_endpoint_POST($server.$sequence_endpoint,
				    $data,
				    'text/x-fasta');

# Print the results we received
print "$sequences";
