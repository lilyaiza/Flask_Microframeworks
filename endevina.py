from flask import Flask, request, session
import random
app = Flask(__name__)
app.secret_key = 'hola'

@app.route('/')
def endevinanum():
	if 'num_aleatori' in session:
		num_aleatori = session['num_aleatori']
	else:
		session['num_aleatori'] = int(random.randrange(0,10))

	
	return '<form method="post" action="/form">Endevina el numero: <input name="num" type=text><br><input type=submit></form>'


@app.route('/form',methods=['POST'])
def comprobar_num():
	if request.method == 'POST':
		numero = int(request.form.get("num"))
		if 'num_aleatori' in session:
			num_aleatori = int(session['num_aleatori'])
			boton_vuelta = '<br><form action="/"><input type=submit value="Volver a intentarlo"></form>'
			volver_iniciar = '<br><form action="/"><input type=submit value="Empezar de nuevo"></form>'

			if numero < num_aleatori:
				return '<h1>Fallaste :( </h1><p>Es un numero mas grande</p>' + boton_vuelta
			elif numero > num_aleatori:
				return '<h1>Fallaste :( </h1><p>Es un numero mas pequeño</p>' + boton_vuelta
			else:
				session['num_aleatori'] = int(random.randrange(0,10))
				return '<h1>Has acertado. Nuevo num:</h1>' + str(session['num_aleatori']) + volver_iniciar
		



if __name__ == '__main__':
	app.run('0.0.0.0',5000, debug=True)

