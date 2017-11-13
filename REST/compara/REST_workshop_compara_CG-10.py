import json, ensembl_rest
server = "http://rest.ensembl.org"

# cafe tree endpoint exercises

# Q CG-10: Get the cafe tree for gene tree predicted for the gene ENSG00000189221 in nh format. Notice anything?

ext = "/cafe/genetree/member/id/ENSG00000189221"
content_type = 'text/x-nh'
endpoint = ensembl_rest.get_endpoint(server, ext, content_type)
print (endpoint)