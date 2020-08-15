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
            .user-box{
                display: flex;
                flex-direction: row;
                justify-content: space-around;
            }
        </style>
    </head>
    <body class="body">
        <div class="main-box">
        	<div><br><br></div>
            <div class="user-box">
                <div>ID: <?php echo $_SESSION["UserId"]; ?></div>
                <div><?php echo $_SESSION["UserNm"]?></div>
                <div><form action="cerrar_sesion.php" method="post"> <input type="submit" name="closeSession" value="Cerrar Sesion" > </form></div>
            </div>
            <div><br><br><hr><br><br></div>
            <div class="bots-box">
            	<div class="botslist-box">
            		<div><form action="nuevo_bot.php" method="post"><input type="submit" name="newBot" value="+ Nuevo Bot"></form></div>
            		<hr>
            		<div>Bots activos:
            		<?php
            			include('bot_class.php');
						$totalBots = -1;
            			$command = './botsbyuser.py get_bots '.$_SESSION['UserId']; # return a string like listbots
						$output = exec($command);
		        		if(strlen($output)>=1 && $output != "None"){
							$botsStr_list = explode(',', $output); # parte en tokens la informacion de los bots
																					# se guarda como id;correo;nombreCuenta;contrasena;{usuario1|usuario2|usuario3|...},siguienteBot
							$bots = array();
							foreach($botsStr_list as &$botStr){
								$bot = new Bot($botStr);
								array_push($bots, $bot->toArray());
								$totalBots = $totalBots + 1;
							}
							$_SESSION["UserBotsList"] = $bots;
		        		}
						$_SESSION["UserTotalBots"] = ($totalBots < 0 ? 0: $totalBots);
		        		echo $_SESSION["UserTotalBots"];
            		?><div>
            		<div>
						<?php
							if($_SESSION["UserTotalBots"] > 0){
								echo '<table>';
								echo '<tr>';
								foreach (['ID','USUARIO','PASSWORD','LISTA DE ORDENES'] as $attribute) {
									echo '<th>'.$attribute.'</th>';
								} 
								echo '</tr>';
								
								foreach ($_SESSION["UserBotsList"] as $column) {
									echo '<tr>';
									foreach(['ID','USUARIO','PASSWORD','LISTA DE ORDENES'] as $attribute) {
										echo '<td>'.$column[$attribute].'</td>';
									}
									echo '</tr>';
								} 
								echo '</table>';
							}else{
								echo 'NO HAY BOTS DISPONIBLES<br><br><br>';
								echo '<form action="nuevo_bot.php" method="post"><input type="submit" name="newBot" value="+ Nuevo Bot"></form>';
							}
						?>
					</div>
            	</div>
            	<!--<div class="botsinfo-box">
							WIP
            	</div>-->
            </div>
        </div>
    </body>
</html>
