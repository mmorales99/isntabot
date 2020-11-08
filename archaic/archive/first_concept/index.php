
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
    </head>
    <body class="body">
        <h1> Inicio de sesión: </h1> <br>
          <form action="inicio_sesion.php" method="POST">
            Usuario: 	<input type="text" value="" name="UName" maxlength="50"> <br>
            Contraseña: <input type="password" value="" name="UPword" maxlength="50"> <br>
            <input type="submit" name="ENTRAR" value="ENTAR" > <br>
        </form>
        <div class="error">
		<?php # completar el index
			if(isset($_GET["error_sesion"])){
				if($_GET["error_sesion"]=="1" or $_GET["error_sesion"]=="2"){
					echo 'ERROR AL INICIAR SESION, O EL USUARIO O LA CONTRASEÑA NO SE CORRESPONDE. PRUEBA OTRA VEZ. ;)';	
				}
				if($_GET["error_sesion"]=="3"){
					echo 'NO SE PUEDE DEJAR CAMPOS EN BLANCO. :|'; 
				}
			}
		?>
		</div>
    </body>
</html>
