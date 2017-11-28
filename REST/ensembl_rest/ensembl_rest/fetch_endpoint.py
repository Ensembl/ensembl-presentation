#!/usr/bin/python

import requests, sys, json, argparse, pprint

def get_endpoint(server, request, content_type='application/json'):
	 """
	 GET an endpoint from the server, allow overriding of default content-type
	 """
	 r = requests.get(server+request, headers={ "Content-Type" : content_type})
	 if not r.ok:
		 r.raise_for_status()
		 sys.exit()

	 if content_type == 'application/json':
		 return r.json()
	 else:
		 return r.text

def post_endpoint(server, request, params):
	"""
	POST to an endpoint
	"""
	headers={ "Content-Type" : "application/json", "Accept" : "application/json"}
	r = requests.post(server+request, headers=headers, data=params)

	if not r.ok:
		 r.raise_for_status()
		 sys.exit()

	return r.json()

def get_endpoint_efo(server, request, content_type='application/json'):

	 r = requests.get(server+request, headers={ "Content-Type" : content_type})
	 if not r.ok:
		 print (http_status_to_string(r.status_code))
		 return r.status_code

	 if content_type == 'application/json':
		 return r.json()
	 else:
		 return r.text


# Add HTTP status reason to status id
def http_status_to_string(http_status_code):
	reasons = requests.status_codes._codes[http_status_code]
	reason = reasons[0]
	string = "HTTP status code: %s. HTTP Reason: %s" %(http_status_code, reason)
	return string


if __name__ == "__main__":
	# parse arguments
	parser = argparse.ArgumentParser()
	parser.add_argument('-s', '--server', default='http://rest.ensembl.org')
	parser.add_argument('-r', '--request')
	parser.add_argument('-m', '--method', default='GET')
	parser.add_argument('-p', '--params')
	parser.add_argument('-c', '--content_type', default='application/json')

	args = sys.argv[1:]
	opts = parser.parse_args(args)
	pprint.pprint(args)
	pprint.pprint(opts)

	# call endpoint
	if opts.method.upper() == 'GET':
		if opts.content_type == 'application/json':
			endpoint = get_endpoint(opts.server, opts.request, opts.content_type)
			print (json.dumps(endpoint, indent=4, sort_keys=True))
		else:
			print (get_endpoint(opts.server, opts.request, opts.content_type))

	elif opts.method.upper() == 'POST':
		if not opts.params:
			print ("No params given to POST")
			sys.exit(1)
		endpoint = post_endpoint(opts.server, opts.request, opts.params)
		print (json.dumps(endpoint, indent=4, sort_keys=True))
	else:
		print ("Method %s is not recognised/supported. Please use GET or POST")
		sys.exit(1)
