from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

@app.route('/analizar-estatus', methods=['POST'])
def analizar_estatus():
    try:
        datos = request.get_json()

        resumen = "\n".join(
            f"- {item['estatus']}: {item['total']} proyectos"
            for item in datos
        )

        prompt = (
            "Eres un analista de procesos de incubación. "
            "Distribución:\n" + resumen
        )

        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)

        return jsonify({"analisis": response.text})

    except Exception as e:
        return jsonify({"error": str(e)})
