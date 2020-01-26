<?php
$root = "/home/master/CUHackit2020/";
include_once "$root"."db.php";
function exec_sql($query){
  global $db;
  $result = $db->query($query);
  return $result;
}
function sql_value($query){
  $result = exec_sql($query);
  $v = mysqli_fetch_row($result);
  return $v[0];
}
function last_insert_id(){
  global $db;
  return $db->insert_id;
}

?>
