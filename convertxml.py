import json
import xmltodict
import urllib
import sys
import os.path
import shutil

def convert(xml_file, xml_attribs=False):
    with open(xml_file, "rb") as f:    # notice the "rb" mode
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        if not isinstance(d, list): d = [d]
        #return json.dumps(d, indent=4)
        return d

def download(files, base_url):
	for f in files:
		localfile = urllib.URLopener()
		localfile.retrieve(''.join([base_url,f]),f)

def deletexml(files):
	for f in files:
		os.remove(f)

def flatten(data):
	#remove extra characters / prefixes
	flatdata = []
	datakeys = [
		#'vuln:vulnerable-configuration', 
		'vuln:vulnerable-software-list', 
		'vuln:cve-id', 
		'vuln:discovered-datetime', 
		'vuln:published-datetime', 
		'vuln:last-modified-datetime', 
	 	'vuln:cvss', 
		'vuln:security-protection', 
		'vuln:assessment_check', 
		'vuln:cwe', 
		'vuln:references', 
		'vuln:scanner',
		'vuln:summary'
	]
	for k in datakeys:
		#if k == 'vuln:vulnerable-configuration':
		#	flatdata.append({'vulnerable-configuration' : data.get(k)})
		if k == 'vuln:vulnerable-software-list':
			tlist = list()
			d = data.get(k)
			if isinstance(d, dict):
				tlist.append(d.get('vuln:product'))
			elif d is not None and len(d) > 1:
				for entry in d.get('vuln:product'):
						tlist.append(entry)
			else:
				tlist = []
			if len(tlist) > 0:
				flatdata.append({'vulnerable-software-list' : tlist[0]})				
		elif k == 'vuln:cve-id':
			flatdata.insert(0, {'cve-id' : data.get(k)})
		elif k == 'vuln:discovered-datetime':
			if data.get(k) is not None:
				flatdata.append({'discovered-datetime' : data.get(k)})
		elif k == 'vuln:published-datetime':
			if data.get(k) is not None:
				flatdata.append({'published-datetime' : data.get(k)})
		elif k == 'vuln:last-modified-datetime':
			if data.get(k) is not None:
				flatdata.append({'last-modified-datetime' : data.get(k)})
		elif k == 'vuln:cvss':
			if data.get(k) is not None:
				flatdata.append({'cvss' : data.get(k)})
		elif k == 'vuln:security-protection':
			if data.get(k) is not None:
				flatdata.append({'security-protection': data.get(k)})
		elif k == 'vuln:assessment_check':
			if data.get(k) is not None:
				flatdata.append({'assessment_check' : data.get(k)})
		elif k == 'vuln:cwe':
			if data.get(k) is not None:
				flatdata.append({'cwe' : data.get(k)})
		elif k == 'vuln:references': 
			if data.get(k) is not None:
				e = data.get(k)
				flatdata.append({'references' : e})
		elif k == 'vuln:scanner':
			if data.get(k) is not None:
				flatdata.append({'scanner' : data.get(k)})
		elif k == 'vuln:summary':
			if data.get(k) is not None:
				flatdata.append({'summary' : data.get(k)})
		else:
			flatdata = []

	return flatdata

files = [
		"nvdcve-2.0-2002.xml", 
		"nvdcve-2.0-2003.xml", 
		"nvdcve-2.0-2004.xml", 
		"nvdcve-2.0-2005.xml", 
		"nvdcve-2.0-2006.xml", 
		"nvdcve-2.0-2007.xml", 
		"nvdcve-2.0-2008.xml", 
		"nvdcve-2.0-2009.xml", 
		"nvdcve-2.0-2010.xml", 
		"nvdcve-2.0-2011.xml", 
		"nvdcve-2.0-2012.xml", 
		"nvdcve-2.0-2013.xml", 
		"nvdcve-2.0-2014.xml", 
		"nvdcve-2.0-2015.xml"
		]
modified = ["nvdcve-2.0-Modified.xml"]
base_url = "https://nvd.nist.gov/feeds/xml/cve/"

if str(sys.argv[1]) == 'download':
	download(files, base_url)
elif str(sys.argv[1]) == 'delete':
	files += modified
	deletexml(files)
elif str(sys.argv[1]) == 'convert':
	outfile = open('current.json','w')
	for f in files:
		doc = convert(f)
		for i, entry in enumerate(d['nvd']['entry'] for d in doc): 
			for j, cve in enumerate(c for c in entry):
    				outfile.write("%s\n" % json.dumps(flatten(cve)))
	outfile.close()    				
elif str(sys.argv[1]) == 'update':
	if os.path.exists('nvdall.json'):
		outfile = open('nvdall.json','a')
		download(modified, base_url)
		doc = convert(modified[0])
		for i, entry in enumerate(d['nvd']['entry'] for d in doc): 
				for j, cve in enumerate(c for c in entry):
    					outfile.write("%s\n" % json.dumps(flatten(cve)))
else:
	print "usage: convertxml.py [download, delete, convert, update]"

if os.path.exists('current.json') and str(sys.argv[1]) == 'convert':
	shutil.copyfile('current.json', 'nvdall.json')
