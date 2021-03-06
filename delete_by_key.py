import memcache
import subprocess
import sys
import re

server = sys.argv[1]
port = sys.argv[2]
prefix = sys.argv[3]
mc = memcache.Client([server+':'+port], debug=0)
#mc.set("key", "value")
#mc.set("notkey", "value")
output = subprocess.Popen(["memcdump", "--server=" + server], stdout = subprocess.PIPE).communicate()[0] # Get all keys
output = output.split("\n") # Split them into array
#print(output)
for key in output:
	result = re.match(prefix + '*', key)
	if result:
		mc.delete(key) # Remove key from memcached
		output.remove(key) # Remove key from array (optional)
		#print("Deleted %s" % key)
#print("Output: %s" % output)
