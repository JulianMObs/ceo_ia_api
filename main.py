from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

genai.configure(api_key=os.environ["AIzaSyDZDR-R40JbcAuAsU02_fhUfu4BgBRLCA0"])

@app.route('/analizar-estatus', methods=['POST'])
def analizar_estatus():
    datos = request.get_json()
    resumen = "\n".join(f"- {item['estatus']}: {item['total']} proyectos" for item in datos)
    prompt = f"Eres un analista de incubación. Analiza:\n{resumen}"
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return jsonify({"analisis": response.text})

