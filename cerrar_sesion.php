<?php
	session_start();
	sleep(3);
	# WIP la desactivacion de los bots, no esta implementada la activacion total de los bots
	
	
	session_destroy();
	header("Location: index.php");
?>
