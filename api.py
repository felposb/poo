from flask import Flask, request, jsonify
import json
from models import Produto, Cidade, Estado, Cliente, Mecanico, Agendamento, Fornecedor, Veiculo

app = Flask(__name__)
def carregar(a):
    with open(a, "r") as f:
        return json.load(f)
def salvar(a, d):
    with open(a, "w") as f:
        json.dump(d, f, indent=4)
PRODUTOS = 'dados/produtos.json'  


@app.post("/produtos")
def criar_produto():
    produtos = carregar(PRODUTOS)
    dados = request.get_json()
    produto = Produto.criar(dados)
    produtos.append(produto.to_dict())
    salvar(PRODUTOS, produtos)
    return jsonify({"mensagem": "Criado"}), 201


app.run(debug=True)