import json, ensembl_rest
server = "http://rest.ensembl.org"

# Homology endpoint exercises

#Q CG-13: Get all the orthologs human gene with the symbol HOXD4-201 in orthoxml format

ext = "/homology/symbol/human/HOXD4-201"
content_type = "text/x-orthoxml+xml"
endpoint = ensembl_rest.get_endpoint(server, ext, content_type)
print (endpoint)