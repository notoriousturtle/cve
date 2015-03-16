import json
import shodan
import requests
import mechanize as mechanize
import cookielib
import sys

SHODAN_API_KEY = "xQlm3r5bW6GVBnAFRDYydLASeWjjpo2T"
api = shodan.Shodan(SHODAN_API_KEY)
shodan_url ="https://api.shodan.io/shodan/host/search"

def get_first(iterable, default=None):
    if iterable:
        for item in iterable:
            return item
    return default

term = str(sys.argv[1])

#find all cve-ids that contain the term
cve_list = []
with open('nvdall.json') as f:
	for record in f:
		if term in record:
			cve_list.append(get_first(json.loads(record)))


# Wrap the request in a try/ except block to catch errors
try:
        payload = {'query' : term, 'key' : SHODAN_API_KEY }
        results = requests.get(shodan_url,params=payload)

        # Show the results
        r = results.json()        
        m = r.get('matches') 
        for i, rec in enumerate(d for d in m):
        	rec['cve-count']=len(cve_list)
        	rec['cve-id']=cve_list

        print json.dumps(r)

except shodan.APIError, e:
        print 'Error: %s' % e