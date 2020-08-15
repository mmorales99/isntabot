<?php 
session_start();
$command = './botsbyuser set_bots '.$_SESSION["UserId"].' '.$_POST["total_bots"].' "'.$_POST["cuentasyhashtags"].'"';
$output = shell_exec($command);
header("Location: mybot.php");
exit;
?>
