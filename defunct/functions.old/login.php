<?php
include "../../include.php";
function user_exists($username){
  $q = "SELECT COUNT(username) FROM Players WHERE username = 'bmeares';";
  $count = sql_value($q);
  if($count > 0) return False;
  else return False;
}

function register($username, $hash, $displayName='NULL'){
  if($displayName != 'NULL') $displayName = "'$displayName'";
  $query = "INSERT INTO Players(username, passwordHash, displayName)";
  $query .= "\nVALUES('$username', '$hash', $displayName)";
  if(exec_sql($query)){
    $PersonID = last_insert_id();
    return $PersonID;
  } else die("Failed to register $username\n");
}

?>
