=head1 LICENSE

Copyright [1999-2015] Wellcome Trust Sanger Institute and the EMBL-European Bioinformatics Institute
Copyright [2016-2017] EMBL-European Bioinformatics Institute

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

=cut


=head1 CONTACT

  Please email comments or questions to the public Ensembl
  developers list at <http://lists.ensembl.org/mailman/listinfo/dev>.

  Questions may also be sent to the Ensembl help desk at
  <http://www.ensembl.org/Help/Contact>.

=cut

package RESTHelper;

use strict;
use warnings;

use Time::HiRes;
use HTTP::Tiny;
use JSON;
use Exporter;
use Carp;

my $http = HTTP::Tiny->new();
my $server = 'http://rest.ensembl.org';
my $global_headers = { 'Content-Type' => 'application/json' };
my $last_request_time = Time::HiRes::time();
my $request_count = 0;

# Wrapper which unpacks JSON documents automatically Perl structures
sub perform_json_action {
  my ($endpoint, $parameters) = @_;
  my $headers = $global_headers;
  my $content = perform_rest_action($endpoint, $parameters, $headers);
  return {} unless $content;
  my $data = decode_json($content);
  return $data;
}

# Utilty function to send requests to rest.ensembl.org and react to errors or rate limiting
# Endpoint: The route on the server, e.g. '/lookup/id'
# Parameters: [[$name,$value],... ] e.g. [ ['expand',1], ['format', 1] ]
# Headers: Key-value pairs of HTTP Header settings, e.g. { Accept => 'text/plain'}

sub perform_rest_action {
  my ($endpoint, $parameters, $headers) = @_;
  $parameters ||= [];
  $headers ||= {};
  $headers->{'Content-Type'} = 'application/json' unless exists $headers->{'Content-Type'};
  if($request_count == 15) { # check every 15
    my $current_time = Time::HiRes::time();
    my $diff = $current_time - $last_request_time;
    # if less than a second then sleep for the remainder of the second
    if($diff < 1) {
      Time::HiRes::sleep(1-$diff);
    }
    # reset
    $last_request_time = Time::HiRes::time();
    $request_count = 0;
  }

  my $url = $server.$endpoint;

  if(@$parameters) {
    my @params;
    foreach my $pair (@$parameters) {
      push(@params, $pair->[0].'='.$pair->[1]);
    }

    my $param_string = join(';', @params);
    $url.= '?'.$param_string;
  }
  my $response = $http->get($url, {headers => $headers});
  my $status = $response->{status};
  if(!$response->{success}) {
    # Quickly check for rate limit exceeded & Retry-After (lowercase due to our client)
    if($status == 429 && exists $response->{headers}->{'retry-after'}) {
      my $retry = $response->{headers}->{'retry-after'};
      Time::HiRes::sleep($retry);
      # After sleeping see that we re-request
      return perform_rest_action($endpoint, $parameters, $headers);
    }
    else {
      my ($status, $reason) = ($response->{status}, $response->{reason});
      carp "Failed for $endpoint! Status code: ${status}. Reason: ${reason}\n";
    }
  }
  $request_count++;
  if(length $response->{content}) {
    return $response->{content};
  }
  return;
}

1;
