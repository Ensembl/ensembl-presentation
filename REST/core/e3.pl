#!/bin/env perl

# Ping the server 25 times to see how rate limiting works

use strict;
use warnings;

use HTTP::Tiny;
use JSON;
use Data::Dumper;
$Data::Dumper::Terse = 1;
$Data::Dumper::Indent = 1;

my $server = "http://rest.ensembl.org";
my $ping_endpoint = "/info/ping";

my $http = HTTP::Tiny->new();

# Fetch an endpoint from the serverm allow overriding of the default content type
# Don't do error checking this time and return the response as-is
sub fetch_endpoint {
    my ($request, $content_type) = @_;
    $content_type ||= 'application/json';

    my $response = $http->get($request,
                              { headers => { 'Content-type' => $content_type } } );

    return $response;

}

print "Accessing ping endpoint\n";

for(my $i = 1; $i <= 25; $i++) {
    my $r = fetch_endpoint($server.$ping_endpoint);

    print "Count $i, status: " . $r->{status} . "\n";
    print "\tRemaining limit: " . $r->{headers}->{'x-ratelimit-remaining'} . "\n";
}
