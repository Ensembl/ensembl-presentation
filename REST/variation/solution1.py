import requests, sys
import pprint
import json

server = "http://rest.ensembl.org"
variation_endpoint = "/variation/human/{}?content-type=application/json&pops=1"
variation_post_endpoint = "/variation/human?content-type=application/json"
overlap_region_endpoint = '/overlap/region/human/{}?feature={};content-type=application/json'
overlap_id_endpoint = '/overlap/id/{}?feature={};content-type=application/json'
lookup_id_endpoint = '/lookup/id/{}?content-type=application/json;expand=1'

def fetch_json(server, request, method, params):
  """
  Fetch an endpoint from the server and return the decoded JSON results.
  """

  if method == 'post':
    r = requests.post(server+request, headers={ "Content-Type" : "application/json"}, data=params)
  else:
    r = requests.get(server+request, headers={ "Content-Type" : "application/json"})

  if not r.ok:
    r.raise_for_status()
    sys.exit()

  return r.json()


if __name__ == "__main__":
  '''
  1) Print all variants that are located on chromosome 17 between 80348215 and 80348333. Use the overlap endpoint to get the
  location (seq_region_name, start, end), alleles, consequence_type and clinical_significance for each variant in the region. 

  2) Get the variant class, evidence attributes, source and the most_severe_consequence for all variants in that region from
  the  variant endpoint. Send the variant ids as post request.
  '''

  variants = fetch_json(server, overlap_region_endpoint.format('17:80348215..80348333', 'variation'), 'get', '')
  for v in variants:
    assembly_name = v['assembly_name'] 
    seq_region_name = v['seq_region_name']
    start = v['start']
    end = v['end']
    alleles = '/'.join(v['alleles'])
    consequence_type = v['consequence_type']
    clinical_significance = v['clinical_significance']
    print "Location: {}:{}:{}-{}, Alleles: {}, Consequence: {}, Clinical significance: {}".format(assembly_name, seq_region_name, start, end, alleles, consequence_type, clinical_significance)

  variant_ids = [str(v['id']) for v in variants]

  params = {'ids' : variant_ids}
  variants = fetch_json(server, variation_post_endpoint, 'post', json.dumps(params))

  for key, value in variants.iteritems():
    variant_class =  variants[key]['var_class'] 
    evidence_attributes = ','.join(variants[key]['evidence'])
    most_severe_consequence = variants[key]['most_severe_consequence']
    print "Variant class: {}, Evidence: {}, Most severe consequence: {}".format(variant_class, evidence_attributes, most_severe_consequence)  

  '''
  3) Foreach protein coding transcript for the gene ENSG00000145354 print the number of overlapping variants. 
  '''

  gene = fetch_json(server, lookup_id_endpoint.format('ENSG00000145354'), 'get', '')  
  transcripts = gene['Transcript']
  for t in transcripts:
    if t['biotype'] == 'protein_coding':
      transcript_id = t['id']
      features = fetch_json(server, overlap_id_endpoint.format(transcript_id, 'variation'), 'get', '')
      print "Transcript {} has {} overlapping variants.".format(transcript_id, len(features))


