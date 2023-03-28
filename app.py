from flask import Flask, request, render_template, redirect
import consulta_banco

app = Flask(__name__, static_folder='static')


@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "GET":
        return render_template('index.html')

    else:
        nro_consultado = request.form.get("numero")
        if nro_consultado == '':
            return render_template('numero_proib.html')
        nro_consultado = int(nro_consultado)
        if nro_consultado <= 0 or nro_consultado > 200:
            return render_template('numero_proib.html')
        query = consulta_banco.consulta(nro_consultado)
        for i in query:
            if i[0] != '':
                nro_consultado = 'vendido'
            else:
                nro_consultado = 'ok'

        if nro_consultado == 'vendido':
            return render_template('cadastrado.html')
        else:
            return redirect('/dados')


@app.route("/dados", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template('dados.html')

    else:
        numero_rifa_dados = request.form.get("numero_rifa")
        if numero_rifa_dados == '':
            return render_template('numero_proib.html')
        query = consulta_banco.consulta(numero_rifa_dados)
        for i in query:
            if i[0] != '':
                numero_rifa_dados = 'vendido'
            else:
                numero_rifa_dados = 'ok'
        print(numero_rifa_dados)
        if numero_rifa_dados == 'vendido':
            return render_template('cadastrado.html')
        else:
            numero_rifa_dados = request.form.get("numero_rifa")
            comprador = str(request.form.get("comprador"))
            telefone = request.form.get("telefone")
            Vendedor = str(request.form.get("Vendedor"))

            if (numero_rifa_dados == '' or
                    comprador == '' or
                    Vendedor == '' or
                    Vendedor == ''):
                return render_template('numero_proib.html')
            numero_rifa_dados = int(numero_rifa_dados)
            if numero_rifa_dados <= 0 or numero_rifa_dados > 300:
                return render_template('numero_proib.html')

            consulta_banco.insere_dados(int(numero_rifa_dados),
                                        comprador,
                                        telefone,
                                        Vendedor)
            return render_template('sucesso.html')


@app.route("/livres", methods=["GET", "POST"])
def livres():
    numeros_disp = consulta_banco.livres()
    return render_template('disponiveis.html', disponiveis=f'{numeros_disp}')


if __name__ == "__main__":
    app.run(debug=True)
