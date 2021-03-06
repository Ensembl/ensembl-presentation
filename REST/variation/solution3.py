import json, ensembl_rest

server = 'http://rest.ensembl.org'

vep_endpoint = '/vep/human/id/{}'
vep_post_endpoint = '/vep/human/id'
overlap_endpoint = '/overlap/region/human/{}?feature=variation'

# 1) Print VEP results for rs189863975
# a) For each overlapping transcript (transcript_consequences) print 
#          variant_allele, 
#          transcript_id, 
#          the consequence_terms 
#          and if available the polyphen_score and polyphen_prediction

variant_effects =  ensembl_rest.get_endpoint(server, vep_endpoint.format('rs189863975'))

for entry in variant_effects:
  for consequence in entry['transcript_consequences']:
    variant_allele = consequence['variant_allele']
    transcript_id  = consequence['transcript_id']
    polyphen_score = consequence.get('polyphen_score', 'no polyphen score')
    polyphen_prediction = consequence.get('polyphen_prediction', 'no polyphen prediction')
    consequence_terms = ','.join(consequence['consequence_terms'])    
    print("Variant allele: {}, Transcript ID: {}, Consequence terms: {}".format(
           variant_allele, transcript_id, consequence_terms))
    if (polyphen_score != 'no polyphen score'):
      print("   PolyPhen score: {}, PolyPhen prediction: {}".format(polyphen_score, polyphen_prediction))


# 2) Print VEP results for all variants that are located in region 19:11400000-11400500.
#    Use the overlap endpoint first to retrieve all variants in the specified region and then
#    use the VEP POST id endpoint to compute consequences for a list of variants 
    
variants = ensembl_rest.get_endpoint(server, overlap_endpoint.format('19:11400000-11400500'))
variant_ids = [str(v['id']) for v in variants]
params = {'ids' : variant_ids}
variant_effects = ensembl_rest.post_endpoint(server, vep_post_endpoint, json.dumps(params))

print("\n")
print(json.dumps(variant_effects, sort_keys=True, indent=4, separators=(',', ': ')))
print("\n")

for entry in variant_effects:
  input_id = entry['input']
  most_severe_consequence = entry['most_severe_consequence'] 
  print("Variant id: {}, Most severe consequence: {}".format(input_id, most_severe_consequence))
