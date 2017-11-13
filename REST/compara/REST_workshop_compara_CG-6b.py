import json, ensembl_rest
server = "http://rest.ensembl.org"

# Gene tree endpoint exercises

# CG-6b: Get the NcRNA gene tree with the stable id RF01168. output in phyloxml format with sequences aligned

ext = "/genetree/id/RF01168?aligned=1;sequence=cdna"
content_type = "text/x-phyloxml+xml"
endpoint = ensembl_rest.get_endpoint(server, ext, content_type)
print (endpoint)