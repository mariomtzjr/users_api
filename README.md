# SQLAlchemy with Flask using GitHub Users API.

### Requirements
- Python 3.9
- Docker
- Flask
- Flask Restful
- Flask SQLAlchemy
- Flask Migrate
- Flask Marshmallow
- Marshmallow SQLAlchemy
- Requests
- Flask Paginate
- Flask Script

### Setup project
First, we need to create a virtual environment and after activate it, for that, is necessary run the following command:  
`python3 -m venv <virtual_env_name>`  
`source <virtual_env_name>/bin/activate`  

#### Clone this repository
`git clone git@github.com:mariomtzjr/users_api.git`  

####
Go inside new cloned repository: 
`cd users_api`

### Populate database
To populate our database using Github Users API, we need to run the following command:  
`python3 scripts/seed.py`  

By default, this scripts will be insert 150 users, but currently, the Github Users API only returns 30 users. If you want to specify the number of users to insert, run the following command:  
`python3 scripts/seed.py -t <users_number>` or `python3 scripts/seed.py --total <users_number>`  

### Set up Flask app
To start Flask app, we need to do some steps:  
1. `export FLASK_APP="main:app"``
2. `export FLASK_ENV="development"`
3. `export APP_SETTINGS_MODULE="config.default.DevelopmentConfig"`
---
4. `python3 manage.py db init`  
5. `python3 manage.py db migrate`
6. `python3 manage.py db upgrade`

Finally, run:  
`python3 manage.py runserver`

Server will be running over __http://127.0.0.1:5000__

### Set up Flask app with Docker
To start Flask app on Docker, run the following command (it's necessay have Docker running):  
`docker-compose build`  
`docker-compose --env-file .env up`


### Test the Flask app
*Endpoints for web*
- Users list: __http://127.0.0.1:5000/__
- Users list with pagination limit: __http://127.0.0.1:5000/users?pagination=<limit>__
- Users list of determitaned page: __http://127.0.0.1:5000/users/<int:page>__
- Users list of determinated page with pagination limit: __http://127.0.0.1:5000/users/<int:page>?pagination=<limit>__

*Endpoints for Api*  
- Users list with pagination limit (25 by default): __http://127.0.0.1:5000/users/profiles__
- Users list of determinated page: __http://127.0.0.1:5000/api/users/profiles?page=<page>__*
- Users list with specified pagination limit: __http://127.0.0.1:5000/api/users/profiles?pagination=<pagination>__
- Users list with order parameter: __http://127.0.0.1:5000/api/users/profiles?order_by=<id|type>__
- Specific user filtering by username parameter: __http://127.0.0.1:5000/api/users/profiles?username=<term>__
- Specific user filtering by id parameter: __http://127.0.0.1:5000/api/users/profiles?id=<id>__


#### Developement notes
1. Realic?? un get a la Api de Github Users y solamente retorna 30 usuarios.
2. Revisar documentaci??n de SQLite para crear conexi??n y realizar inserci??n de datos.
3. Por defecto, al crear una conexi??n con SQLite, se valida si ya existe un archivo db, de lo contrario lo crea.
4. A la hora de crear un archivo db, debe de crearse sobre /app/main/database.
5. Como el test requiere que se utilice Flask, necesito revisar mis ejercicios sobre ese Framework.
6. La app requiere de usar vistas, debe de ser algo similar a django la implementaci??n de templates.
7. Las vistas necesitan ser responsivas, para eso voy a utilizar Boostrap 4 y con los contextos me aseguro de mostrar de manera correcta los cards de los profiles.
8. Creando la estructura del proyecto con archivos iniciales.
9. No recuerdo c??mo obtener los argumentos al ejecutar un script. Revisando documentaci??n.
10. Voy a utilizar Git Flow para que sea m??s pr??ctico la creaci??n de features y su gesti??n.
11. Creaci??n de primer feature/populate_database.
12. Preparo la vista, el modelo y la carpeta del template.
13. Revisar c??mo implementar una paginaci??n con Flask, lo he hecho antes con Django y DRF, pero no con Flask.
14. Implementando paginaci??n en Flask, devuelve correctamente los ??tems por cada p??gina pero los elementos no cambian.
15. Trato de resolver los resultados de la paginaci??n. Sigue sin funcionar, he consultado respuestas en Stackoverflow, pero no funcionan.
16. Requiero implementar un manager para personalizar comando a la hora de inicializar la base de datos.
17. Estoy revisando la documentaci??n de flask-script y flask-migrate.
18. Qued?? implementado la forma personalizada de inicializar la bd.
19. Uno de mis ejercicios sobre Flask, incluye la creaci??n de una APi, por lo tanto me puede servir para extender la funcionalidad existente.
20. La API deber?? responder en formato JSON, por lo tanto, necesito usar jsonify y hacer un dump de la data.
21. La API deber?? sosportar un filtrado por username y id, order por type y id y controlar el tama??o de la paginaci??n.
22. Investigando c??mo implementar una flask api with pagination.
23. Encontr?? una forma de paginar. Implementando.
24. La paginaci??n funciona correctamente. Tengo problemas a la hora de especificar el par??metro page.
25. Control de paginaci??n funciona correctamente, a??ado un par??metro __start__ que indica el id a partir del cual comenzar?? la p??gina siguiente. A??n no logro relacionarlo con el par??metro page.
25. Filtrado por username y id funciona correctamente si se indican.
27. Necesito crear una cuenta en Azure, pero requiero un m??todo de pago.
28. App creada en Azure, deploy exitoso.
29. Creaci??n de los archivos docker para virtualizar la Flask app.
30. Despu??s de varias correcciones, la app levanta correctamente.
31. Cada que se requiere volver a levantar la applicaci??n, es necesario elimitar carpeta de migrations y la base de datos.
32. Subiendo repositorio a Dockerhub para poder utilizarlo en Azure.
33. Se necesita crear una instancia de contenedor en Docker. Creando.
34. Hay un error a la hora de hacer el deploy del contenedor, al parecer no puede acceder a la instancia de DockerHub


