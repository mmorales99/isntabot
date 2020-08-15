<?php
	session_start();
	sleep(3);
	# falta añadir el guardado de la base de datos y la posterior desactivacion
	
	
	session_destroy();
	header("Location: index.php");
?>
