import json, ensembl_rest
server = "http://rest.ensembl.org"

# Gene tree endpoint exercises

# CG-7: Get the gene tree predicted for the gene ENSG00000189221 in full nh format

ext = "/genetree/member/id/ENSG00000189221?nh_format=full"
content_type = "text/x-nh"
endpoint = ensembl_rest.get_endpoint(server, ext, content_type)
print (endpoint)