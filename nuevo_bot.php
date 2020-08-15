<?php
	session_start();
?>

<!DOCTYPE html>
<html lang="es">
    <head>
        <title>Página Web de Lolo</title>
        <meta charset="UTF-8">
        <meta name="description" content="Webpage for isntabot project">
        <meta name="author" content="Manuel 'Lolo' Morales - @mmoralitos99">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!--
        <link rel="stylesheet" type="text/css" href="index.css">
        -->
        <style>
            .main-box{
                display: flex;
                flex-direction: column;
            }
        </style>
    </head>
    <body class="body">
        <div class="main-box">
        	<form action="genera_bots.php" method="post">
        		Total bots a generar: <input type="text" name="total_bots" placeholder="Numero de bots que se van a crear..."> <br>
        		Cuentas/Hashtags a seguir: <input type="text" name="cuentasyhashtags" placeholder="Los que pongas aquí se va a seguir.EJEMPLO DE USO: @mmoralitos99, @mmoralitosdev, #AINTTHATSAD..."> <br>
        		<input type="submit" value="GENERA LOS BOTS" name="generar">
        	</form>
            <form action="mybot.php" method="post">
                <input type="submit" value="CANCELAR" name="cancelar">
            </form>
        </div>
    </body>
</html>
