import json
import xmltodict
 
def convert(xml_file, xml_attribs=True):
    with open(xml_file, "rb") as f:    # notice the "rb" mode
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        #return json.dumps(d, indent=4)
        return d

def getFromDict(dataDict, mapList):
    return reduce(lambda d, k: d[k], mapList, dataDict)

doc = convert("nvdcve-2.0-2015.xml")

#print json.dumps(doc, indent=4)

myKeys = ['entry','id','vuln:vulnerable-software-list']

print json.dumps(dict([(i, doc[i]) for i in myKeys if i in doc]), indent=4)


#print getFromDict(doc, ['nvd','entry','id','vuln:vulnerable-software-list'])


#print  {e: doc[e] for e in (u'@id',u'vuln:vulnerable-software-list')}
