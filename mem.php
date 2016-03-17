<?php
$meminstance = new Memcache();
$meminstance->pconnect('localhost', 11211);

mysql_connect("localhost", "test", "testing123") or die(mysql_error());
mysql_select_db("test") or die(mysql_error());

$query = "select id from example where name = 'new_data'";
$querykey = "KEY" . md5($query);

$result = $meminstance->get($querykey);

if (!$result) {
       $result = mysql_fetch_array(mysql_query("select id from example where name = 'new_data'")) or die('mysql error');
       $meminstance->set($querykey, $result, 0, 600);
print "got result from mysql\n";
return 0;
}

print "got result from memcached\n";
return 0;

?>
