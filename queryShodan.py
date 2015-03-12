import json
import shodan
import requests
import mechanize as mechanize
import cookielib

#SHODAN_API_KEY = "g3SS8MUtcF7ofJeREKZEJsMFqFGmazz5"
SHODAN_API_KEY = "xQlm3r5bW6GVBnAFRDYydLASeWjjpo2T"
api = shodan.Shodan(SHODAN_API_KEY)

shodan_url ="https://api.shodan.io/shodan/host/search"

#emulate browser requests with mechanize to use REST API
def make_browser():

        # Browser
        br = mechanize.Browser()

        # Cookie Jar
        cj = cookielib.LWPCookieJar()
        br.set_cookiejar(cj)

        # Browser options
        br.set_handle_equiv(True)
        br.set_handle_gzip(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)

        # Follows refresh 0 but not hangs on refresh > 0
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        # Want debugging messages?
        #br.set_debug_http(True)
        #br.set_debug_redirects(True)
        #br.set_debug_responses(True)

        # User-Agent (this is cheating, ok?)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

        return br



# Wrap the request in a try/ except block to catch errors
try:
        #brwsr = make_browser()
        #brwsr.add_password(shodan_url, 'spara', 'P3pit0iloveyou')
        # Search Shodan
        #results = api.search('wms')
        #https://api.shodan.io/shodan/host/search?key={YOUR_API_KEY}&query={query}&facets={facets}
        payload = {'query' : 'China', 'key' : SHODAN_API_KEY }
        results = requests.get(shodan_url,params=payload)
        #print ''.join([shodan_url,'?key=',SHODAN_API_KEY,'&query=country:CN'])
        #results = brwsr.open(''.join([shodan_url,'&query=country:CN']))
        #print results.url

        # Show the results
        #print brwsr.response().read()
        r = results.json()
        print json.dumps(r)
        

        m = r.get('matches') 
        for i, data in enumerate(d['data'] for d in m): 
                print data
        #        for info in m:
        #                print info


        #print 'Results found: %s' % results['total']
        #for result in results['matches']:
        #        print 'IP: %s' % result['ip_str']
        #        print result['data']
        #        print ''
except shodan.APIError, e:
        print 'Error: %s' % e