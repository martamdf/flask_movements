#en views 
from movements import app #instancia creada en el init
from flask import render_template #trabaja con jinjer



@app.route('/') #aplicamos el decorador
def listaMovimientos():
    return render_template('movementsList.html', miTexto='Ya veremos') #'Tengo que devolver una lista de movimientos' miTexto viene de el html, podría meterse una función
    

