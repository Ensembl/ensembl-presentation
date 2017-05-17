import requests, sys
import pprint

server = "http://rest.ensembl.org"
ld_endpoint = "/ld/human/{}/{}?content-type=application/json"
ld_region_endpoint = "/ld/human/region/{}/{}?content-type=application/json"

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

    '''
    1) Compute LD in the region 3:196064297-196068186 for the population 1000GENOMES:phase_3:CEU. Print all results with r2=1 and d_prime=1.
    '''

    ld_values = fetch_json(server, ld_region_endpoint.format('3:196064297-196068186', '1000GENOMES:phase_3:CEU'))
    high_ld_pairs = ( ld_value for ld_value in ld_values if float(ld_value['d_prime']) == 1.0  and float(ld_value['r2']) == 1.0)

    for pair in high_ld_pairs:
      variation1 = pair['variation1']
      variation2 = pair['variation2']
      print "Pair: {}-{}".format(variation1, variation2)


    '''
    2) Compute pairwise LD for all variants that are not further away from rs535797132 than 500kb. Print all variants that are in LD (d_prime >= 0.8) with rs535797132. For each pair of variants also print d_prime and r2. Use 1000GENOMES:phase_3:FIN as the population. 
    '''

    ld_values = fetch_json(server, ld_endpoint.format('rs535797132', '1000GENOMES:phase_3:FIN'))
    high_ld_pairs = ( ld_value for ld_value in ld_values if float(ld_value['d_prime']) >= 0.8)

    for pair in high_ld_pairs:
      variation1 = pair['variation1']
      variation2 = pair['variation2']
      d_prime = pair['d_prime']
      r2 = pair['r2']
      print "Pair: {}-{}, d_prime: {}, r2: {}".format(variation1, variation2, d_prime, r2)

