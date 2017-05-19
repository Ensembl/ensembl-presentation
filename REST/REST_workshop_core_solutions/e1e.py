import requests, sys
import pprint

'''
Use the /lookup endpoint to find IRAK4, and map the coordinates for
the gene to the GRCh37 assembly.
'''

server = "http://rest.ensembl.org"
lookup_endpoint = "/lookup/symbol/human/{}"
lookup_endpoint_expanded = "/lookup/symbol/human/{}?expand=1"
mapping_endpoint = "/map/human/GRCh38/{}:{}..{}/GRCH37"
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

    mapped = fetch_endpoint(server,
                            mapping_endpoint.format(gene['seq_region_name'],
                                                    gene['start'],
                                                    gene['end']))
    print "IRAK4 on GRCh38 is: {}:{}-{}".format(gene['seq_region_name'],
                                                gene['start'],
                                                gene['end'])

    '''
    We're cheating, because we know in this case there is only one mapping.
    In reality we should be iterating through the array of mappings as their
    could be gaps in how the region maps between assemblies.
    '''
    grch37_mapped = mapped['mappings'][0]['mapped']
    print "IRAK4 on GRCh37 is: {}:{}-{}".format(grch37_mapped['seq_region_name'],
                                                grch37_mapped['start'],
                                                grch37_mapped['end'])

    # Fetch the sequence in FASTA format
    sequence = fetch_endpoint(server, sequence_endpoint.format(gene['id']), 'text/x-fasta')

    # Print the sequence we received
    print sequence
