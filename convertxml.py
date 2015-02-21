import json
import xmltodict
import urllib
import tempfile

def convert(xml_file, xml_attribs=True):
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

def showkeys(data):
	k = []
	for key in data.keys():
		k.append(key)
	print k



files = ["nvdcve-2.0-2002.xml", "nvdcve-2.0-2003.xml", "nvdcve-2.0-2004.xml", "nvdcve-2.0-2005.xml", "nvdcve-2.0-2006.xml", "nvdcve-2.0-2007.xml", "nvdcve-2.0-2008.xml", "nvdcve-2.0-2009.xml", "nvdcve-2.0-2010.xml", "nvdcve-2.0-2011.xml", "nvdcve-2.0-2012.xml", "nvdcve-2.0-2013.xml", "nvdcve-2.0-2014.xml", "nvdcve-2.0-2015.xml"]
#files = ["nvdcve-2.0-2002.xml"]
base_url = "https://nvd.nist.gov/feeds/xml/cve/"

# download(files, base_url)


for f in files:
	doc = convert(f)
	for i, entry in enumerate(d['nvd']['entry'] for d in doc): 
		for j, cve in enumerate(c for c in entry):
    			print json.dumps(cve)
    			#showkeys(cve)

