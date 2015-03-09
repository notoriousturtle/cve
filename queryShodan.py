import json
import shodan
import requests

#SHODAN_API_KEY = "g3SS8MUtcF7ofJeREKZEJsMFqFGmazz5"
SHODAN_API_KEY = "xQlm3r5bW6GVBnAFRDYydLASeWjjpo2T"
api = shodan.Shodan(SHODAN_API_KEY)

shodan_url ="https://api.shodan.io/shodan/host/search"

# Wrap the request in a try/ except block to catch errors
try:
        # Search Shodan
        results = api.search('wms')
        #https://api.shodan.io/shodan/host/search?key={YOUR_API_KEY}&query={query}&facets={facets}
        #payload = {'query' : 'country:CN', 'key' : SHODAN_API_KEY }
        #results = requests.get(shodan_url,params=payload)
        #print results.url

        # Show the results
        #print results
        print 'Results found: %s' % results['total']
        for result in results['matches']:
                print 'IP: %s' % result['ip_str']
                print result['data']
                print ''
except shodan.APIError, e:
        print 'Error: %s' % e