#en views 
from movements import app #instancia creada en el init
from flask import render_template, request, url_for, redirect #trabaja con jinja
from movements.forms import MovementForm #importa la clase del formulario que hemos creado
import csv
from flask import request
import sqlite3

#DBfile = app.config['DBfile']
DBfile = 'movements/data/basededatos.db'

def consulta (query, params=()):
    conn = sqlite3.connect(DBfile)
    c = conn.cursor()
    
    c.execute(query, params)
    conn.commit()
    
    filas = c.fetchall()
    conn.close()

    if len(filas) == 0:
        return filas

    columnNames = []
    for columnName in c.description:
        columnNames.append(columnName[0])

    listaDeDiccionarios = []

    for fila in filas:
        d={}
        for ix, columnName in enumerate(columnNames):
            d[columnName]= fila[ix]
        listaDeDiccionarios.append(d)
    
    #conn.commit() #para que se guarden los datos si no, se ejecutaría un rollback automáticamente
    
    return listaDeDiccionarios
    


@app.route('/') #aplicamos el decorador
def listaIngresos():
    ingresos = consulta('SELECT id ,fecha, concepto, cantidad FROM movimientos;') 
    total=0
    for ingreso in ingresos:
        total += float(ingreso['cantidad'])
    return render_template('movementsList.html', ingresos=ingresos, total=total) #'Tengo que devolver una lista de movimientos' miTexto viene de el html, podría meterse una función
    
@app.route('/creaalta', methods=["GET", "POST"]) #aplicamos el decorador
def nuevoIngreso():
    form = MovementForm()

    if request.method == "POST":
        print(form.validate())
        if form.validate():
            consulta('INSERT INTO movimientos (fecha, concepto, cantidad) VALUES ( ?, ?, ?);', 
                    (
                    form.fecha.data, 
                    form.concepto.data, 
                    form.cantidad.data
                    )
                ) #entre paréntesis le metemos la consulta
            return redirect(url_for('listaIngresos')) #te devuelve a la página principal
        else:
            return render_template("alta.html", form=form)

    return render_template("alta.html", form=form)

@app.route('/modifica/<id>', methods=["GET", "POST"]) #aplicamos el decorador
def modificaIngreso(id):
    if request.method == "POST":
        consulta('UPDATE movimientos SET fecha = ?, concepto = ?, cantidad = ? WHERE id = ?;', 
                (
                request.form.get('fecha'), 
                request.form.get('concepto'), 
                float(request.form.get('cantidad')),
                request.form.get('id')
                )
            )
        return redirect(url_for('listaIngresos'))
    else:
        ingreso = consulta("SELECT id ,fecha, concepto, cantidad FROM movimientos WHERE id = ?;",(id,)) #entre paréntesis le metemos la consulta
        return render_template("modifica.html", ingreso=ingreso[0])

