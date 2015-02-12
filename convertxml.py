import json
import xmltodict
from operator import getitem

def convert(xml_file, xml_attribs=True):
    with open(xml_file, "rb") as f:    # notice the "rb" mode
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        if not isinstance(d, list): d = [d]
        #return json.dumps(d, indent=4)
        return d

files = ["./data/nvdcve-2.0-2002.xml", "./data/nvdcve-2.0-2003.xml", "./data/nvdcve-2.0-2004.xml", "./data/nvdcve-2.0-2005.xml", "./data/nvdcve-2.0-2006.xml", "./data/nvdcve-2.0-2007.xml", "./data/nvdcve-2.0-2008.xml", "./data/nvdcve-2.0-2009.xml", "./data/nvdcve-2.0-2010.xml", "./data/nvdcve-2.0-2011.xml", "./data/nvdcve-2.0-2012.xml", "./data/nvdcve-2.0-2013.xml", "./data/nvdcve-2.0-2014.xml", "./data/nvdcve-2.0-2015.xml"]

for f in files:
	doc = convert(f)
	for i, entry in enumerate(d['nvd']['entry'] for d in doc): 
		for j, cve in enumerate(c for c in entry):
    			print json.dumps(cve)

