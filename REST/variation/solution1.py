import json, ensembl_rest

server = 'http://rest.ensembl.org'

overlap_region_endpoint = '/overlap/region/human/{}?feature={}'
variation_post_endpoint = '/variation/human'
lookup_id_endpoint = '/lookup/id/{}?expand=1'
overlap_id_endpoint = '/overlap/id/{}?feature={}'

# 1) Print all variants that are located on chromosome 17 between 80348215 and 80348333. 
#    Use the overlap endpoint to get the location (seq_region_name, start, end), 
#    alleles, consequence_type and clinical_significance for each variant in the region. 

request = overlap_region_endpoint.format('17:80348215..80348333', 'variation') 

variants = ensembl_rest.get_endpoint(server, request)
for v in variants:
  assembly_name = v['assembly_name'] 
  seq_region_name = v['seq_region_name']
  start = v['start']
  end = v['end']
  alleles = '/'.join(v['alleles'])
  consequence_type = v['consequence_type']
  clinical_significance = v['clinical_significance']
  print("Location: {}:{}:{}-{}, Alleles: {}, Consequence: {}, Clinical significance: {}".format(assembly_name, seq_region_name, start, end, alleles, consequence_type, clinical_significance))


# 2) Get the variant class, evidence attributes, source and the most_severe_consequence 
#    for all variants in that region from the variant endpoint. 
#    Send the variant ids as post request.
variant_ids = [str(v['id']) for v in variants]
params = {'ids' : variant_ids}

request = variation_post_endpoint
variants = ensembl_rest.post_endpoint(server, request, json.dumps(params))

print("\n")
for key, value in variants.items():
  variant_class =  variants[key]['var_class'] 
  evidence_attributes = ','.join(variants[key]['evidence'])
  most_severe_consequence = variants[key]['most_severe_consequence']
  print("Variant class: {}, Evidence: {}, Most severe consequence: {}".format(variant_class, evidence_attributes, most_severe_consequence))


#
# 3) Foreach protein coding transcript for the gene ENSG00000145354 
#    print the number of overlapping variants. 
# 
print("\n")
request = lookup_id_endpoint.format('ENSG00000145354')
gene = ensembl_rest.get_endpoint(server, request)  
transcripts = gene['Transcript']
for t in transcripts:
  if t['biotype'] == 'protein_coding':
    transcript_id = t['id']
    features = ensembl_rest.get_endpoint(server, overlap_id_endpoint.format(transcript_id, 'variation'))
    print("Transcript {} has {} overlapping variants.".format(transcript_id, len(features)))
