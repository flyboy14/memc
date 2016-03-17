import memcache
import subprocess 
import sys
import re

mc = memcache.Client(['127.0.0.1:11211'], debug=0)
mc.set("key", "value")
mc.set("notkey", "value")
output = subprocess.Popen(["memcdump", "--servers=localhost"], stdout=subprocess.PIPE).communicate()[0]
output=output.split("\n")
print(output)
for i in output:
#	print(i)
	result = re.match(sys.argv[1]+'*', i)
	if result:
		mc.delete(i)
		output.remove(i)
		print("Deleted %s" % i)
print("Output: %s" % output)
#print(output)
#mc.delete("another_key")
