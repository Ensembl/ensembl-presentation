import json, ensembl_rest
server = "http://rest.ensembl.org"

# Gene tree endpoint exercises

# CG-6a: Get the information for the protein genetree with the stable id ENSGT00390000003602. output should be in the orthoxml format

ext = "/genetree/id/ENSGT00390000003602?"
content_type = "text/x-orthoxml+xml"
endpoint = ensembl_rest.get_endpoint(server, ext, content_type)
print (endpoint)