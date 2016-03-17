<?php
$mem = new Memcached();
$mem->addServer("127.0.0.1", 11211);

mysql_connect("localhost", "test", "test123") or die(mysql_error());
mysql_select_db("mem_test") or die(mysql_error());

$query = "SELECT name FROM sample_data WHERE id = 1";
$querykey = "KEY" . md5($query);

$result = $mem->get($querykey);

if ($result) {
    print "<p>Data was: " . $result[0] . "</p>";
    print "<p>Caching success!</p><p>Retrieved data from memcached!</p>";
} else {
    $result = mysql_fetch_array(mysql_query($query)) or die(mysql_error());
    $mem->set($querykey, $result, 10);
    print "<p>Data was: " . $result[0] . "</p>";
    print "<p>Data not found in memcached.</p><p>Data retrieved from MySQL and stored in memcached for next time.</p>";
}
?>
