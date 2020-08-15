# MANUAL DE USO Y GUIA DE INSTALACION  




### DEPEDENCIAS  


-Selenium:  
Para instalarlo:  

~~~
pip3 install selenium
~~~  
o como alternativa usar:  (en caso de no tener pip instalado)  
~~~ 
cd selenium-3.141.0/ && python setup.py install
~~~  
	
-ChromeDriver:  
Para instalarlo:  
1. correr el comando:  
~~~
google-chrome --version  
~~~
2. ir a:  
[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)  
3. descargar el driver para la misma version que este instalada (en el repositorio se ha usado la version 84)  
4. descomprimir el archivo descargado  
5. mover a una carpeta cualquiera  
6. añadir el ejecutable al path de linux
		
		
### MODO DE EMPLEO  


Dar permisos de ejecucion a los archivos .py:  
~~~
chmod +x *.py  
~~~
Generar el primer usuario y la base de datos:  
~~~
./botsbyuser.py new_user nombre_usuario password
~~~
	
		
##### COMANDOS  
**./botsbyuser.py [opt] [arg1...3]**  
	
opt:  
- new_user	->	genera un usuario nuevo, si ya hay uno igual, lo descarta	{arg1 = nombre usuario; arg2 = contraseña}  
- validate	->	comprueba la existencia de un par usuario/contraseña y le asigna una id para operar con ella	{arg1 = nombre usuario; arg2 = contraseña | devuelve codigos de error si no es correcto el par usuario/contraseña}  
- get_bots	->	devuelve una lista con las cuentas generadas por un usuario concreto {arg1 = id del usuario a consultar}  
- set_bots	->	le asigna una cantidad de autocuentas a un usuario {arg1 = id usuario a modificar; arg2 = total de autocuentas; arg3 = lista de cuentas a las que seguir}  
