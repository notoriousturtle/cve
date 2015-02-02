import csvkit
import json


#data = []
f = open('allitems100.csv',"r")
#data = f.readlines()
f = [d.replace('|','","') for d in f]
header = []
header = f[0]
print header, f
#del f[0]
#print header
#print "\n"
#out = json.dumps(zip(header,data))
#print out
reader = csvkit.DictReader(f)
out = json.dumps([row for row in reader], indent=4, separators=(',', ': '))
print out