import requests, sys
import pprint

'''
Use the /lookup endpoint to find IRAK4, print all transcript stable id(s)
Then find the associated sequence
'''

server = "http://rest.ensembl.org"
lookup_endpoint = "/lookup/symbol/human/{}"
lookup_endpoint_expanded = "/lookup/symbol/human/{}?expand=1"
sequence_endpoint = "/sequence/id/{}"

def fetch_endpoint(server, request, content_type='application/json'):
    """
    Fetch an endpoint from the server, allow overriding of default content-type
    """
    r = requests.get(server+request, headers={ "Content-Type" : content_type})

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    if content_type == 'application/json':
        return r.json()
    else:
        return r.text

if __name__ == "__main__":

    print "Fetching gene IRAK4"

    # Fetch the record for the gene IRAK4
    gene = fetch_endpoint(server, lookup_endpoint_expanded.format('IRAK4'))

    # Extract the stable id from the dictionary and print
    print "Stable id: {}".format(gene['id'])

    print "We found transcripts:"

    # Loop through and print the transcripts
    for transcript in gene['Transcript']:
        print "\t{}".format(transcript['id'])

    # Fetch the sequence in FASTA format
    sequence = fetch_endpoint(server, sequence_endpoint.format(gene['id']), 'text/x-fasta')

    # Print the sequence we received
    print sequence
