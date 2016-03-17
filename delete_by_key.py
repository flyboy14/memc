import memcache
import subprocess
import sys
import re

server=sys.argv[1]
port=sys.argv[2]
mc = memcache.Client([server+':'+port], debug=0)
#mc.set("key", "value")
#mc.set("notkey", "value")
output = subprocess.Popen(["memcdump", "--server="+server], stdout=subprocess.PIPE).communicate()[0]
output=output.split("\n")
#print(output)
for i in output:
	result = re.match(sys.argv[3]+'*', i) # sys.argv[1] is an external parameter
	if result:
		mc.delete(i)
		output.remove(i)
		#print("Deleted %s" % i)
#print("Output: %s" % output)
