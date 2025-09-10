from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain.chat_models import init_chat_model

app = Flask(__name__)
CORS(app)  # habilita CORS em todas as rotas

# Rota POST de exemplo
@app.route("/", methods=["POST"])
def echo():
    data = request.get_json()  # tenta ler JSON do corpo
    geminiKey = request.headers.get('authorization-google')
    model = request.headers.get('model0')
    print(geminiKey)
    print(model)
    gemini = init_chat_model(model=model, model_provider="google_genai", google_api_key=geminiKey)
    if not data:
        return jsonify({"error": "Nenhum JSON recebido"}), 400
    answer_gemini = gemini.invoke(data["messages"][-1]["text"])
    return jsonify({"text": answer_gemini.content})

# Inicia o Flask
app.run(port=5000)