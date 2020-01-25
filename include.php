<?php
include_once "config.php";
include_once "db.php";
foreach (glob("functions/*.php") as $filename){
  include_once $filename;
}

?>
