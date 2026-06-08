from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_valor_final(valor_investido, taxa_anual, meses):
    taxa_mensal = taxa_anual / 100 / 12
    return valor_investido * (1 + taxa_mensal) ** meses

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulador_investimento', methods=['POST'])
def simulador_investimento():
    valor_investido = float(request.form['valor_investido'])

    taxas = {
        "poupança": 6.0,
        "cdb": 10.0,
        "cdi": 15.0,
        "tesouro_direto": 11.0,
        "acoes": 25.0
    }
    taxa = taxas.get(request.form['tipo_investimento'], 0)

    tempo = int(request.form['tempo'])
    tempo_investimento = request.form['tempo_investimento']

    if tempo_investimento == "Anos":
        meses = tempo * 12
    else:
        meses = tempo

    valor_final = calcular_valor_final(valor_investido, taxa, meses)
    return render_template('index.html', valor_final=round(valor_final, 2))

if __name__ == '__main__':
    app.run(debug=True)