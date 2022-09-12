# Seguridad ABC

## Instalación

1. Install Virtualenv and activate it
```sh
$ virtualenv -p python3 venv
```
```sh
$ source venv/bin/activate
```
2. Install requirements.txt
```sh
$ pip3 install -r requirements.txt
```

## Ejecución

se ingresas a cada apliacion y se ejecuta el comando
```sh
$ python3 app.py
```

para levantar el hearbeat se debe hacer lo siguiente
desde la carpeta de monitor_apertura

```sh
$ celery -A config_heartbeat.celery worker --loglevel=info
```
```sh
$ celery -A config_heartbeat.celery beat --loglevel=info
```
En la carpeta Pruebas
```sh
$ celery -A config_celey.celery worker --loglevel=INFO

```
```sh
$ celery -A config_celey.celery beat --loglevel=INFO

```

## Descripción de los servicios

Esta rama (main) muestra la comunicación entre servicios de manera asíncrona e implementa el patrón CQRS. Para la comunicación asíncrona se utiliza Redis como plataforma de mensajería.

El ejemplo implementa dos servicios:

#### monitor aperturas

Al implemetar el patrón CQRS las operaciones que expone este servicio se implementan en una partes: comandos (python3 app.py) 
 En el archivo vistas.py se tienen las siguientes operaciones:

- Crear una nueva regla: Esta operación se implementa en la función AgregarRegla a través del método post.

Se puede observar que una vez creada la regla se guarda en la base de datos para

#### Reportes

Al implemetar el patrón CQRS las operaciones que expone este servicio se implementan en una partes: consultas (app.py).
En el archivo vistas se tienen las siguientes operaciones:

- Consulta la base de datos de moitor reportes para devolver sus reglas creadas por usuario.


#### API Gateway

En este ejemplo se utiliza la configuración post para implementar el componente API Gateway. 
Para cad aplicacion se le dispuso de un puerto para poder comunicarse entre ellas 
por ejemplo http://localhost:5004/monitor_aperturas/reglas/1 y http://localhost:5002//monitor_aperturas/reglas

```
http://localhost:5004/monitor_aperturas/reglas/1
http://localhost:5002/monitor_aperturas/reglas
http://192.168.0.6:5020/hearbeat
```

#### Comunicación asíncrona


###### Notificar cambios

en el heartbeat se notifica si la aplicacion esta funcionado correctamente 


###### Actualizar cambios

Para el ejemplo, la actualización de un producto se realiza por parte del servicio de órdenes, el cual modifica la cantidad en stock del producto. Por lo anterior, el archivo updater.py implementa la actualización del producto cuyo id publica el servicio de órdenes en la cola. En la carpeta ordenes, en el archivo base.py se define la función process_order la cual verifica que el producto sea válido y si es así cambia el estado de la orden y publica en la cola el id del producto incluído en la orden.
