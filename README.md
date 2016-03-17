* This script deletes from memcached all keys with prefix matching KEY* regular expression. Script takes 3 parameters: SERVER_IP, PORT and KEY.

* Requirements
  * pyton 3x
  * python-memcache
  * libmemcached-tools

* Usage example:

* python delete_by_key.py localhost 11211 today
  * Deletes all keys like today.213, today.123492418, todayzkjhsd... on localhost port 11211.
