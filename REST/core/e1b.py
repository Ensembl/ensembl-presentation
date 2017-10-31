import requests, sys
import pprint

'''
Use the /lookup endpoint to find IRAK4
'''

server = "http://rest.ensembl.org"
lookup_endpoint = "/lookup/symbol/human/{}"

def fetch_json(server, request):
    """
    Fetch an endpoint from the server and return the decoded JSON results.
    """
    r = requests.get(server+request, headers={ "Content-Type" : "application/json"})

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    return r.json()

if __name__ == "__main__":

    print "Fetching gene IRAK4"

    # Fetch the record for the gene IRAK4
    gene = fetch_json(server, lookup_endpoint.format('IRAK4'))

    # Extract the stable id from the dictionary and print
    print "Stable id: {}".format(gene['id'])
