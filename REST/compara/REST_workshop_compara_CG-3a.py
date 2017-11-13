import json, ensembl_rest
server = "http://rest.ensembl.org"

# Family endpoint exercises

# CG-3a: Get the information for the family with the stable id PTHR10740_SF4

ext = "/family/id/PTHR10740_SF4"
endpoint = ensembl_rest.get_endpoint(server, ext)
print (json.dumps(endpoint, indent=4, sort_keys=True))