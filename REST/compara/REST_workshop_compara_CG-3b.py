import json, ensembl_rest
server = "http://rest.ensembl.org"

# Family endpoint exercises

# CG-3b: Get the aligned cdna sequences for only the ensembl members of the family with the stable id PTHR10740_SF4

ext = "/family/id/PTHR10740_SF4?aligned=1;sequence=cdna;member_source=ensembl"
endpoint = ensembl_rest.get_endpoint(server, ext)
print (json.dumps(endpoint, indent=4, sort_keys=True))