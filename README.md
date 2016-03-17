* This script deletes all items with prefix matching KEY* regular expression. Script takes 3 parameters: SERVER_IP PORT and KEY.

* Requirements
  * pyton 3x
  * python-memcache

* Example:

* delete_by_key.py localhost 11211 today
  * deletes all keys like today.213, today.123492418, todayzkjhsd .. etc on localhost port 11211.
