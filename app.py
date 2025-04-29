from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/api/cupons', methods=['GET'])
def listar_cupons():
    cupons = [
        {'id': 1, 'titulo': 'Desconto 10%', 'descricao': 'Cupom para 10% de desconto', 'imagem': 'cupom1.jpg'},
        {'id': 2, 'titulo': 'Frete Grátis', 'descricao': 'Cupom de frete grátis', 'imagem': 'cupom2.jpg'}
    ]
    return jsonify(cupons)

@app.route('/api/upload', methods=['POST'])
def upload_imagem():
    if 'imagem' not in request.files:
        return jsonify({'erro': 'Nenhum arquivo enviado'}), 400

    file = request.files['imagem']
    if file.filename == '':
        return jsonify({'erro': 'Nome de arquivo vazio'}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    return jsonify({'mensagem': 'Imagem salva com sucesso', 'filename': file.filename}), 200

@app.route('/uploads/<path:filename>')
def servir_imagem(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
