import json, ensembl_rest
server = "http://rest.ensembl.org"

# cafe tree endpoint exercises

# CG-9: Get the cafe tree information for the genetree with the stable id ENSGT00390000003602. output should be in the json format.

ext = "/cafe/genetree/id/ENSGT00390000003602"
endpoint = ensembl_rest.get_endpoint(server, ext)
print (json.dumps(endpoint, indent=4, sort_keys=True))