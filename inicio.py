from audioop import maxpp
from flask import Flask, session, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)
app.secret_key = "cairocoders-ednalan"


app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'testingdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'





@app.route('/')
def index():
    return render_template("index.html")



@app.route('/reglas')
def reglas():
    return render_template("reglas.html")






@app.route('/servidor')
def servidor():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
    cursor = conn.cursor()
    cursor.execute('select idServidor, nomserv from servidor order by idServidor')
    datos = cursor.fetchall()
    return render_template("Servidor.html", servidor = datos)

@app.route('/servidor_editar/<string:id>')
def servidor_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('select idServidor, nomserv from servidor where idServidor = %s', (id))
    dato = cursor.fetchall()
    return render_template("Servidor_edi.html", servidor=dato[0])

@app.route('/servidor_fedita/<string:id>',methods=['POST'])
def servidor_fedita(id):
    if request.method == 'POST':
        nom = request.form['descripcion']
        DirecIP = request.form['DireccionIP']
        maxp = request.form['MaxPersonas']
        ubic = request.form['ubicacion']
        antig = request.form['antiguedad']
        noInt = request.form['Nointegrantes']
        prop = request.form['nomPropietario']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
        cursor = conn.cursor()
        cursor.execute('update servidor set nomServ=%s, DireccionIP=%s, MaxPersonas=%s, ubicacion=%s, antiguedad=%s, Nointegrantes=%s , nomPropietario=%s where idServidor=%s' , (nom, DirecIP, maxp, ubic, antig, noInt, prop, id))
        conn.commit()
    return redirect(url_for('servidor'))
    
@app.route('/servidor_borrar/<string:id>')
def servidor_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('delete from servidor where idServidor = {0}'.format(id))
    conn.commit()
    return redirect(url_for('Servidor'))

@app.route('/servidor_agregar')
def servidor_agregar():
    return render_template("Servidor_agr.html")

@app.route('/servidor_fagrega', methods=['POST'])
def servidor_fagrega():
    if request.method == 'POST':
        nom = request.form['descripcion']
        DirecIP = request.form['DireccionIP']
        maxp = request.form['MaxPersonas']
        ubic = request.form['ubicacion']
        antig = request.form['antiguedad']
        noInt = request.form['Nointegrantes']
        prop = request.form['nomPropietario']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
        cursor = conn.cursor()
        cursor.execute('insert into servidor (nomServ, DireccionIP, MaxPersonas, ubicacion, antiguedad, Nointegrantes, nomPropietario) values (%s,%s,%s,%s,%s,%s,%s)',(nom, DirecIP, maxp, ubic, antig, noInt, prop))
        conn.commit()
    return redirect(url_for('servidor'))





























@app.route('/puesto')
def puesto():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
    cursor = conn.cursor()
    cursor.execute('select idPuesto, nomPue from puesto order by idPuesto')
    datos = cursor.fetchall()
    return render_template("puesto.html", pue=datos, dat=' ', catServidor=' ')

@app.route('/puesto_fdetalle/<string:idP>', methods=['GET'])
def puesto_fdetalle(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()

    cursor.execute('select idPuesto, nomPue from puesto order by idPuesto')
    datos = cursor.fetchall()

    cursor.execute('select idPuesto,nomPue,apellidos,edad,correo,idCuenta,servidoresAntes,idiomas,habilidades from puesto where idPuesto = %s', (idP))
    dato = cursor.fetchall()

    cursor.execute('select a.idServidor, a.nomServ from servidor a, puesto b where a.idServidor = b.idServidor and b.idPuesto = %s', (idP))
    datos1 = cursor.fetchall()

    return render_template("puesto.html", pue=datos, dat=dato[0], catServidor=datos1[0])

@app.route('/puesto_borrar/<string:idP>')
def puesto_borrar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('delete from puesto where idPuesto = %s',(idP))
    conn.commit()
    return redirect(url_for('puesto'))

@app.route('/puesto_agregar')
def puesto_agregar():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    
    cursor.execute('select idServidor, nomServ from servidor ')
    datos1 = cursor.fetchall()

    return render_template("puesto_agr.html", catServidor=datos1)

@app.route('/puesto_fagrega', methods=['POST'])
def puesto_fagrega():
    if request.method == 'POST':
        if 'idServidor' in request.form:
            idServ = request.form['idServidor']
        else:
            idServ = '1'
        
        if 'servidoresAntes' in request.form:
            servAnt = request.form['servidoresAntes']
        else:
            servAnt = '1'

        nom = request.form['nombre']
        apell = request.form['apellidos']
        edad = request.form['edad']
        correo = request.form['correo']
        idCuen  = request.form['idCuenta']
        idio = request.form['idiomas']
        hab = request.form['habilidades']
        
        
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('insert into puesto (idServidor,nomPue,apellidos,edad,correo,idCuenta,servidoresAntes,idiomas,habilidades) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)', (idServ,nom, apell, edad, correo, idCuen, servAnt, idio, hab))
    conn.commit()
    cursor.execute('select idPuesto, nomPue from puesto where idPuesto=(select max(idPuesto) from puesto) ')
    dato=cursor.fetchall()
    idpue = dato[0]
    idP = idpue[0]
    
    return redirect(url_for('puesto'))




@app.route('/puesto_editar/<string:idP>')
def puesto_editar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('select idPuesto,nomPue,apellidos,edad,correo,idCuenta,servidoresAntes,idiomas,habilidades from puesto where idPuesto = %s', (idP))
    dato = cursor.fetchall()

    cursor.execute('select idServidor, nomServ from servidor')
    datos1 = cursor.fetchall()

    cursor.execute('select a.idServidor, a.nomServ from servidor a, puesto b where a.idServidor = b.idServidor and b.idPuesto = %s', (idP))
    datos2 = cursor.fetchall()  

    return render_template("puesto_edi.html", dat=dato[0], catServidor=datos1, Servidor=datos2[0])


@app.route('/puesto_fedita/<string:idP>', methods=['POST'])
def puesto_fedita(idP):
    if request.method == 'POST':
        if 'idServidor' in request.form:
            idServ = request.form['idServidor']
        else:
            idServ = '1'
        
        if 'servidoresAntes' in request.form:
            servAnt = request.form['servidoresAntes']
        else:
            servAnt = '1'

        nom = request.form['nombre']
        apell = request.form['apellidos']
        edad = request.form['edad']
        correo = request.form['correo']
        idCuen  = request.form['idCuenta']
        idio = request.form['idiomas']
        hab = request.form['habilidades']
        

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('update puesto set nomPue = %s, idServidor = %s, apellidos = %s, servidoresAntes = %s, edad = %s, correo = %s, idCuenta = %s, idiomas = %s, habilidades = %s  where idPuesto = %s', (idServ,nom, apell, edad, correo, idCuen, servAnt, idio, hab, idP))
    conn.commit()
    return redirect(url_for('puesto'))























@app.route('/requisicion_pend')
def requisicion_pend():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
    cursor = conn.cursor()
    cursor.execute('select idRequisicion, nomReq from requisi order by idRequisicion')
    datos = cursor.fetchall()
    cursor.execute('select idRequisicion, autorizar from requisi order by idRequisicion')
    datoos = cursor.fetchall()
    return render_template("requisicion_pend.html", req=datos, pue=datoos, dat=' ', catServidor=' ', catPuesto=' ')

@app.route('/requisicion_fdetalle/<string:idR>', methods=['GET'])
def requisicion_fdetalle(idR):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()

    cursor.execute('select idRequisicion, nomServ from requisi, servidor order by idRequisicion')
    datos = cursor.fetchall()

    cursor.execute('select idRequisicion, nomPue from requisi, puesto order by idRequisicion')
    datoss = cursor.fetchall()

    cursor.execute('select idRequisicion, nomReq, conducta, reglas, autorizar, idPuesto, idServidor from requisi where idRequisicion = %s', (idR))
    dato = cursor.fetchall()

    
    cursor.execute('select a.idServidor, a.nomServ from servidor a, puesto b where a.idServidor = b.idServidor and b.idPuesto = %s', (idR))
    datos1 = cursor.fetchall()

    cursor.execute('select a.idPuesto, a.nomPue from puesto a, requisi b where a.idPuesto = b.idPuesto and b.idRequisicion = %s', (idR))
    datos2 = cursor.fetchall()



    return render_template("requisicion_pend.html", req=datos, pue=datoss, dat=dato[0], catServidor=datos1[0], catPuesto=datos2[0])

@app.route('/requisicion_borrar/<string:idR>')
def requisicion_borrar(idR):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('delete from requisi where idRequisicion = %s',(idR))
    conn.commit()
    return redirect(url_for('requisicion_pend'))



@app.route('/requisicion_autorizar/<string:idR>', methods=['GET'])
def requisicion_autorizar(idR):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()


    cursor.execute('select idRequisicion, nomReq, conducta, reglas, autorizar, idPuesto, idServidor from requisi where idRequisicion = %s', (idR))
    dato = cursor.fetchall()

    cursor.execute('select idRequisicion, idCuenta from requisi, puesto order by idRequisicion')
    datos = cursor.fetchall()

    cursor.execute('select idRequisicion, nomReq from requisi order by idRequisicion')
    datoss = cursor.fetchall()

    cursor.execute('select a.idPuesto, a.nomPue from puesto a, requisi b where a.idPuesto = b.idPuesto and b.idRequisicion = %s', (idR))
    datos2 = cursor.fetchall()
    return render_template("requisicion_aut.html", dat=dato[0], catCuenta=datos[0], pue=datoss, catPuesto=datos2[0])


@app.route('/requisicion_fautorizar/<string:idR>', methods=['POST']) 
def requisicion_fautorizar(idR):
    if request.method == 'POST':

        nomAutoriza = request.form['nomAutoriza']
        
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()


    cursor.execute('update requisi set nomAutoriza = %s, autorizar = 1 where idRequisicion = %s', ( nomAutoriza, idR))
    conn.commit()


    return redirect(url_for('requisicion_pend'))



@app.route('/requisicion_agregar')
def requisicion_agregar():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    
    cursor.execute('select idServidor, nomServ from servidor ')
    datos1 = cursor.fetchall()
    cursor.execute('select idPuesto, nomPue from puesto ')
    datos2 = cursor.fetchall()
    return render_template("requisicion_agr.html", catServidor=datos1, catPuesto=datos2)




@app.route('/requisicion_fagrega', methods=['POST'])
def requisicion_fagrega():
    if request.method == 'POST':
        if 'idServidor' in request.form:
            idServ = request.form['idServidor']
        else:
            idServ = '1'
        
        if 'idPuesto' in request.form:
            idPue = request.form['idPuesto']
        else:
            idPue = '1'
        
        
        nom = request.form['nombre']
        conduct = request.form['conducta']
        reg = request.form['reglas']
        
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh')
    cursor = conn.cursor()
    cursor.execute('insert into requisi (idServidor,idPuesto,nomReq,conducta,reglas) values (%s,%s,%s,%s,%s)', (idServ, idPue, nom, conduct, reg))
    conn.commit()
    cursor.execute('select idRequisicion, nomReq from requisi where idRequisicion=(select max(idRequisicion) from requisi) ')
    dato=cursor.fetchall()

    return redirect(url_for('requisicion_pend', req=dato))









if __name__ == "__main__":
    app.run(debug=True)