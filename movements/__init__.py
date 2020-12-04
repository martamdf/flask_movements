from flask import Flask

app = Flask(__name__) #instance_relative_config=True) #se le añade el instance__ para decirle que la configuración de la aplicación flask no se va a hacer directmente en el código, sino desde un fichero externo
#app.config.from_object('config')#esto es el fichero externo donde está esa configuración (creamos el fichero config.py) aquí te carga todas las variables del fichero config

from movements import views #esto es para que coja el enrutamiento que está en el archivo views.py