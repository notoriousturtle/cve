import csv
import json
import tempfile

tf = tempfile.TemporaryFile(mode='w+b')

f = open('allitems100.csv',"r")
#lines = open('allitems100.csv',"r").read()

#for l in lines:
#	rec = [d.replace('|','","') for d in l]
#	tf.write(''.join(rec))


#tf.seek(0)

#for a in tf.readlines():
#	print a

#tf.seek(0)

#f = open(ntf,'r')
reader = csv.DictReader(f)
out = json.dumps([row for row in reader], indent=4, separators=(',', ': '))
print out

tf.close()