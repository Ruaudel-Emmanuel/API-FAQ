from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

API_URL = "https://api.perplexity.ai/chat/completions"
API_KEY = "Placez ici votre clé API"

HTML = """
<h1>FAQ Dynamique IA</h1>
<form method="post">
    <input name="question" placeholder="Pose ta question..." required>
    <button type="submit">Demander</button>
</form>
{% if answer %}
    <h2>Réponse :</h2>
    <div>{{ answer }}</div>
{% endif %}
"""

def ask_api(question):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": question}]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    return response.json()["choices"]["message"]["content"]

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    if request.method == "POST":
        question = request.form["question"]
        answer = ask_api(question)
    return render_template_string(HTML, answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
