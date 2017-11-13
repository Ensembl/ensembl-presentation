import json, ensembl_rest
server = "http://rest.ensembl.org"

# cafe tree endpoint exercises

# Q CG-11: Get the cafe tree information for the gene tree predicted for the human gene with the symbol HOXD4-201

ext = "/cafe/genetree/member/symbol/homo_sapiens/HOXD4-201"
content_type = 'text/x-nh'
endpoint = ensembl_rest.get_endpoint(server, ext, content_type)
print (endpoint)