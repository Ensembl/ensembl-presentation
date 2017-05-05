#!/bin/env perl

# Use the /lookup endpoint to find IRAK4

use strict;
use warnings;

use HTTP::Tiny;
use JSON;
use Data::Dumper;
$Data::Dumper::Terse = 1;
$Data::Dumper::Indent = 1;

my $server = "http://rest.ensembl.org";
my $lookup_endpoint = "/lookup/symbol/human/%s";

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

my $url = $server . sprintf($lookup_endpoint, 'IRAK4');
my $gene = fetch_endpoint($url);

print Dumper $gene;
print "\n";
