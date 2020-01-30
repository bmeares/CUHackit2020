<?php
include "../../include.php";
if (isset($_POST['submit'])) {
  var_dump($_POST);
  if (!isset($_POST['username'])) die('Missing username');
  if (!isset($_POST['password'])) die('Missing password');
  if (!isset($_POST['displayName'])) $displayName = "NULL";
  else $displayName = $_POST['displayName'];
  $username = $_POST['username'];
  $password = $_POST['password'];
  $hash = password_hash($_POST['password'], PASSWORD_DEFAULT);
  $PlayerID = register($username, $hash, $displayName);
  $_SESSION['PlayerID'] = $PlayerID;
  $_SESSION['username'] = $username;
  echo "$username has PlayerID $PlayerID";

  if (user_exists($username)){
    $error = "User ".$username." already exists";
    die($error);
  } else {
    header('index.html'); 
  }
}
?>

<!DOCTYPE html>
<html>
    <head>
        <script>
            // document.getElementById("reg_btn").addEventListener("click", redirLogin);
            // function redirLogin() {
                // window.location.replace("index.html");
            // }
        </script>
    </head>

    <body>

    <h2>Register</h2>

    <form action="register.php" method="POST">
        <input type="text" name="username" placeholder="Username" />
        <br>
        <input type="password" name="password" placeholder="Password" />
        <br>
        <input type="password" placeholder="Confirm Password" />
        <br>
        <input type="text" name="displayname" placeholder="Display Name" />
        <br>
        <input name="submit" id="reg_btn" type="submit" value="submit">
    </form>

    </body>
</html>

