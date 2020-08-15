<?php 
session_start();
$command = './botsbyuser.py validate '.$_POST['UName'].' '.$_POST['UPword'];
$output = exec($command);
echo $output;
if($output=="PW"){
	header("Location: index.php?error_sesion=1");
	exit;
}
if($output=="UW"){
	header("Location: index.php?error_sesion=2");
	exit;
}
if($output=="BT"){
	header("Location: index.php?error_sesion=3");
	exit;
}
if($output==""){
	echo "ERROR, NO SERVER RESPONSE";
	header("Locationm: index.php");
	exit;
}
$_SESSION["UserId"] = $output;
$_SESSION["UserNm"] = $_POST["UName"];
$_SESSION["SessionId"] = session_id();
$sessionId = $_SESSION["SessionId"];
header("Location: mybot.php");
exit;
?>
