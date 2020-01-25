<?php
include "../../include.php";
function user_exists($username){
  $query = "IF EXISTS(SELECT username FROM Players WHERE username = '$username') SELECT 'exists' ELSE SELECT 'dne'";
  $exists = sql_value($query);
  if($exists == "exists") return True;
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
