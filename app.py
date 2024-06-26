from flask import Flask, request, jsonify

app = Flask(__name__)

def calcular_cedulas(valor):
    cedulas = [100, 50, 20, 10, 5, 2]
    resultado = {str(cedula): 0 for cedula in cedulas}

    for cedula in cedulas:
        if valor >= cedula:
            resultado[str(cedula)] = valor // cedula
            valor %= cedula

    return resultado

@app.route('/api/saque', methods=['POST'])
def saque():
    dados = request.get_json()
    valor = dados.get('valor')

    if not isinstance(valor, int) or valor <= 0:
        return jsonify({"erro": "Valor invalido. Por favor, insira um numero inteiro positivo."}), 400

    resultado = calcular_cedulas(valor)
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)