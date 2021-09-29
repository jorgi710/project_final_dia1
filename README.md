# project_final_dia1
Se va a utilizar - >Django, html, css, jwt (json web token), django_rest_framework

1- Vamos a ajustar los settings y librerias que vamos a utilizar:

  Como vamos a usar el framework django rest, importamos la liberia -> pip install djangorestframework
  
  Como se va a trabjar ocn jwt importo esa libreria -> pip install djangorestframework-simplejwt
  
  Como el servidor de la base de datos que se eligio es possgress, importo la libreria -> pip install psycopg2
  
  Por ahora creo que no vamos a importar nada mas. 
  
  
2- Vamos a settings.py para hacer los ajustes necesarios a nuestro proyecto: 

  -> Vamos a configurar el JWT para generar el token
  -> Para ello ir a la url official -> https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html
  -> Y seguir cada paso tal cual la documentación
  -> Ojo agregar las urls y en sttings.install ->  'rest_framework_simplejwt', 'rest_framework'
  
  -> Vamos a hacer la conexion con la base de datos 
    
    1- Debo ir a keroku -> crear new app -> (darle nombre, Ejm : andres711) -> create app -> Resources -> Find more add-ons -> Heroku Postgres -> Install Heroku Postgres
        -> App to provision to -> (name de app, Ejm: andres711) -> Submit Order Form -> Heroku Postgres -> Settings -> View Credentials -> Password,user,host, database,port,etc.
    
    2- Ahora si nos devolvemos al projecto y creamos la conexion con la base de datos -> Copiamos el host, name_db, user, port, password que estan en heroku.
    
    3- Hacer la conexion en PyCharm
 
 3- Luego de crear la conexion vamos a crear nuestra primera aplicacion  
 
    1- En la terminar pasamos el comando (Al final ponemos el nombre que deseemos, Ejm:home)-> python manage.py startapp home 
    2- Agregar la app a settings.py.installed_apps -> 'home'
    3- Finalmente verificar que la app no tenga problema con el siguiente comando -> python manage.py  check home
    
 4- Vamos primero a crear las tablas en el archivo modelo de nuestra home
 
    1- Creamos la estructura de la tabla en la sintaxis de Django (Esto es porque el codifica y crea el SQL a cualquier servidor sea MySQL, MariaDB, Postgres, etc)
    
    2- Cada que se haga un cambio en el modelo se debe ejecutar -> python manage.py makemigrations  -> Con este comando se crea la migracion con codigo 0001
    
    3- Ahora ahy que decirle que genere el SQL -> python manage.py sqlmigrate home 0001 -> Ese home es el nombre de la APP Y el 0001 el codigo de migracion.
    
    4- Ahora vamos a decirle que cree las tablas en el servidor en este caso Postgres -> 
    
    
    
  
  
    
