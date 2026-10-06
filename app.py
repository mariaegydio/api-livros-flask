from flask import Flask, jsonify, request   

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Anéis',
        'autor': 'J.R.R. Tolkien'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K. Rowling'
    },
    {
        'id': 3,
        'titulo': 'O Pequeno Príncipe',
        'autor': 'Antoine de Saint-Exupéry'
    }
]

# Consultar todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar um livro pelo ID
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
            
    return jsonify({'mensagem': 'Livro não encontrado'}), 404

#editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
    return jsonify({'mensagem': 'Livro não encontrado'}), 404

#excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro_por_id(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify({'mensagem': 'Livro excluído com sucesso'})
    return jsonify({'mensagem': 'Livro não encontrado'}), 404


if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)