from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R. Tolkien'
    },
    {
        'id': 2,
        'título': 'Harry Pottre e a Pedra Filosofal',
        'autor': 'J.K. Howling'        
    },
    {
        'id': 3,
        'título': 'Habitos Atômicos',
        'autor': 'James Clear'
    },
]

# Consultar(Todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar(id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Editar
def editar_livro_por_id(id):
    livros_alterado = request.get_json()
    #continuar aqui

# Excluir
# Rodar
app.run(port=5000, host='localhost', debug=True)