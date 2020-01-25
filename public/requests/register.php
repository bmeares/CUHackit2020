<?php
include "../../include.php";
if (!isset($_POST['username'])) die('Missing username');
if (!isset($_POST['password'])) die('Missing password');
if (!isset($_POST['displayName'])) $displayName = "NULL";
else $displayName = $_POST['displayName'];
$username = $_POST['username'];
$password = $_POST['password'];
$hash = password_hash($_POST['password'], PASSWORD_DEFAULT);
$PlayerID = register($username, $hash, $displayName);
$_SESSION['playerID'] = $PlayerID;
$_SESSION['username'] = $username;
echo "$username has PlayerID $PlayerID";

if (user_exists($username)) $error = "User ".$username." already exists";

?>
