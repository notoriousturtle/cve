import json
import xmltodict
from operator import getitem

def convert(xml_file, xml_attribs=True):
    with open(xml_file, "rb") as f:    # notice the "rb" mode
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        if not isinstance(d, list): d = [d]
        #return json.dumps(d, indent=4)
        return d

def getFromDict(dataDict, mapList):
    return reduce(lambda d, k: d[k], mapList, dataDict)

def extract(dict_in, dict_out):
    for key, value in dict_in.iteritems():
        if isinstance(value, dict): # If value itself is dictionary
            extract(value, dict_out)
        elif isinstance(value, unicode):
            # Write to dict_out
            dict_out[key] = value
    return dict_out

doc = convert("nvdcve-2.0-2015.xml")

nvd= doc["nvd"]

print json.dumps(nvd, indent = 4)

#myKeys = ['entry','id','vuln:vulnerable-software-list']

#for d in doc.values():
#	print d['nvd']

#print json.dumps(dict([(i, doc[i]) for i in myKeys if i in doc]), indent=4)


#print getFromDict(doc, ['nvd','entry','id','vuln:vulnerable-software-list'])


#print  {e: doc[e] for e in (u'@id',u'vuln:vulnerable-software-list')}
