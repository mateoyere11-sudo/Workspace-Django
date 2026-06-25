import requests
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'clave-secreta-flask'

API_BASE = 'http://127.0.0.1:8000/api'
AUTH = ('yeremi', '1234567890.m')

def get_auth():
    return AUTH

@app.route('/')
def index():
    return redirect(url_for('espacio_lista'))

@app.route('/espacios/')
def espacio_lista():
    r = requests.get(f'{API_BASE}/espacios/', auth=get_auth())
    espacios = r.json() if r.ok else []
    return render_template('espacio_lista.html', espacios=espacios)

@app.route('/espacios/nuevo/', methods=['GET', 'POST'])
def espacio_crear():
    error = None
    if request.method == 'POST':
        data = {
            'nombre_sala'       : request.form['nombre_sala'],
            'tipo_espacio'      : request.form['tipo_espacio'],
            'capacidad_personas': request.form['capacidad_personas'],
            'piso_edificio'     : request.form['piso_edificio'],
            'precio_hora'       : request.form['precio_hora'],
            'tiene_aire'        : 'tiene_aire'        in request.form,
            'tiene_proyector'   : 'tiene_proyector'   in request.form,
            'estado_disponible' : 'estado_disponible' in request.form,
            'descripcion'       : request.form.get('descripcion', ''),
        }
        r = requests.post(f'{API_BASE}/espacios/', json=data, auth=get_auth())  # ← coma añadida
        if r.ok:
            return redirect(url_for('espacio_lista'))
        error = r.json()
    return render_template('espacio_form.html', titulo='Nuevo Espacio', espacio=None, error=error)  # ← fuera del if

@app.route('/espacios/<int:pk>/editar/', methods=['GET', 'POST'])
def espacio_editar(pk):
    error   = None
    espacio = {}
    if request.method == 'POST':
        data = {
            'nombre_sala'       : request.form['nombre_sala'],
            'tipo_espacio'      : request.form['tipo_espacio'],
            'capacidad_personas': request.form['capacidad_personas'],
            'piso_edificio'     : request.form['piso_edificio'],
            'precio_hora'       : request.form['precio_hora'],
            'tiene_aire'        : 'tiene_aire'        in request.form,
            'tiene_proyector'   : 'tiene_proyector'   in request.form,
            'estado_disponible' : 'estado_disponible' in request.form,
            'descripcion'       : request.form.get('descripcion', ''),
        }
        r = requests.put(f'{API_BASE}/espacios/{pk}/', json=data, auth=get_auth())
        if r.ok:
            return redirect(url_for('espacio_lista'))
        error = r.json()
    else:
        r       = requests.get(f'{API_BASE}/espacios/{pk}/', auth=get_auth())
        espacio = r.json() if r.ok else {}
    return render_template('espacio_form.html', titulo='Editar Espacio', espacio=espacio, error=error)

@app.route('/espacios/<int:pk>/eliminar/', methods=['GET', 'POST'])
def espacio_eliminar(pk):
    if request.method == 'POST':
        requests.delete(f'{API_BASE}/espacios/{pk}/', auth=get_auth())
        return redirect(url_for('espacio_lista'))
    r       = requests.get(f'{API_BASE}/espacios/{pk}/', auth=get_auth())
    espacio = r.json() if r.ok else {}
    return render_template('espacio_confirm_delete.html', espacio=espacio)


@app.route('/servicios/')
def servicio_lista():
    r         = requests.get(f'{API_BASE}/servicios/', auth=get_auth())
    servicios = r.json() if r.ok else []
    return render_template('servicio_lista.html', servicios=servicios)


@app.route('/servicios/nuevo/', methods=['GET', 'POST'])
def servicio_crear():
    error = None
    if request.method == 'POST':
        data = {
            'reserva'           : request.form['reserva'],
            'tipo_servicio'     : request.form['tipo_servicio'],
            'descripcion'       : request.form.get('descripcion', ''),
            'cantidad'          : request.form['cantidad'],
            'precio_unitario'   : request.form['precio_unitario'],
            'solicitud_especial': request.form.get('solicitud_especial', ''),
            'hora_entrega'      : request.form.get('hora_entrega') or None,
            'estado_servicio'   : request.form['estado_servicio'],
        }
        r = requests.post(f'{API_BASE}/servicios/', json=data, auth=get_auth())
        if r.ok:
            return redirect(url_for('servicio_lista'))
        error = r.json()
    return render_template('servicio_form.html', titulo='Nuevo Servicio', servicio=None, error=error)


@app.route('/servicios/<int:pk>/editar/', methods=['GET', 'POST'])
def servicio_editar(pk):
    error    = None
    servicio = {}
    if request.method == 'POST':
        data = {
            'reserva'           : request.form['reserva'],
            'tipo_servicio'     : request.form['tipo_servicio'],
            'descripcion'       : request.form.get('descripcion', ''),
            'cantidad'          : request.form['cantidad'],
            'precio_unitario'   : request.form['precio_unitario'],
            'solicitud_especial': request.form.get('solicitud_especial', ''),
            'hora_entrega'      : request.form.get('hora_entrega') or None,
            'estado_servicio'   : request.form['estado_servicio'],
        }
        r = requests.put(f'{API_BASE}/servicios/{pk}/', json=data, auth=get_auth())
        if r.ok:
            return redirect(url_for('servicio_lista'))
        error = r.json()
    else:
        r        = requests.get(f'{API_BASE}/servicios/{pk}/', auth=get_auth())
        servicio = r.json() if r.ok else {}
    return render_template('servicio_form.html', titulo='Editar Servicio', servicio=servicio, error=error)


@app.route('/servicios/<int:pk>/eliminar/', methods=['GET', 'POST'])
def servicio_eliminar(pk):
    if request.method == 'POST':
        requests.delete(f'{API_BASE}/servicios/{pk}/', auth=get_auth())
        return redirect(url_for('servicio_lista'))
    r        = requests.get(f'{API_BASE}/servicios/{pk}/', auth=get_auth())
    servicio = r.json() if r.ok else {}
    return render_template('servicio_confirm_delete.html', servicio=servicio)

if __name__ == '__main__':
    app.run(debug=True, port=5000)