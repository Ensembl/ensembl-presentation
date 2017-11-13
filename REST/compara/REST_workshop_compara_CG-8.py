import json, ensembl_rest
server = "http://rest.ensembl.org"

# Gene tree endpoint exercises

# CG-8: Get the gene tree predicted for the human gene with the symbol HOXD4-201 in simple nh format.

ext = "/genetree/member/symbol/human/HOXD4-201"
content_type = "text/x-nh"
endpoint = ensembl_rest.get_endpoint(server, ext, content_type)
print (endpoint)