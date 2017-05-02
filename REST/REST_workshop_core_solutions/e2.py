import requests, sys
import json
import pprint

'''
Use the /lookup endpoint to find IRAK4
Loop through the transcripts and fetch the sequences and print
'''

server = "http://rest.ensembl.org"
lookup_endpoint_expanded = "/lookup/symbol/human/{}?expand=1"
sequence_endpoint = "/sequence/id"

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

def fetch_endpoint_POST(server, request, data, content_type='application/json'):
    """
    Fetch an endpoint using POST, allowing overriding of default content-type
    """
    r = requests.post(server+request,
                      headers={ "Content-Type" : content_type},
                      data=data)

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

    # Loop through and print the transcripts
    transcripts = []
    for transcript in gene['Transcript']:
        transcripts.append(transcript['id'])

    # Create the data body to be sent to the server
    data = {'ids': transcripts }

    # Fetch the sequences as a single POST call
    sequences = fetch_endpoint_POST(server,
                                    sequence_endpoint,
                                    data=json.dumps(data),
                                    content_type='text/x-fasta')

    # Print the results we received
    print sequences
