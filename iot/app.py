from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

#temperatura
def ler_dht11():
    temperatura = round(random.uniform(20, 35), 1)
    umidade = round(random.uniform(30, 80), 1)
    return {"temperatura": temperatura, "umidade": umidade}

#sensor de movimento
def ler_sensor_movimento():
    movimento = random.choice([True, False])
    return {"movimento": movimento}

#sendor de proximidade
def ler_sensor_proximidade():
    distancia = round(random.uniform(5, 200), 1) 
    return {"distancia": distancia}

#Quando alguém acessar o endereço, a função abaixo será chamada.
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dados")
def dados():
    return jsonify({
        "dht11": ler_dht11(),
        "movimento": ler_sensor_movimento(),
        "proximidade": ler_sensor_proximidade()
    })

if __name__ == "__main__":
    app.run(debug=True)
