from flask import Flask, render_template, request
from model import emb_similarity
app = Flask(__name__)

# Charger le modèle une seule fois

@app.route("/", methods=["GET", "POST"])
def main():
    best_option = None
    best_score = None

    if request.method == "POST":
        question = request.form["question"]
        options = [
            request.form["option_1"],
            request.form["option_2"],
            request.form["option_3"],
            request.form["option_4"]
        ]
        (best_option, best_score) = emb_similarity(question=question, options=options)
    return render_template("index.html", best_option=best_option, best_score=best_score)

if __name__ == "__main__":
    app.run(debug=True)
