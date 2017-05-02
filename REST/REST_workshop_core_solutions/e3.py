import requests, sys
import json
import pprint

'''
Use the /lookup endpoint to find IRAK4
Loop through the transcripts and fetch the sequences and print
'''

server = "http://rest.ensembl.org"
ping_endpoint = "/info/ping"

def fetch_endpoint(server, request, content_type='application/json'):
    """
    Fetch an endpoint from the server, allow overriding of default content-type
    """
    r = requests.get(server+request, headers={ "Content-Type" : content_type})

    return r

if __name__ == "__main__":

    print "Accessing ping endpoint"

    for i in range(1, 25):
        r = fetch_endpoint(server, ping_endpoint)
        print "Count {}, status: {}".format(i, r.status_code)
        print "\tRemaining limit: {}".format(r.headers['X-RateLimit-Remaining'])
