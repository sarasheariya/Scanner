from flask import Flask, request, render_template
from logic import lex

# we used Flask

app = Flask("My app")

@app.route("/", methods=['GET', 'POST'])
def index():
    out = []
    text = ""
    if(request.method == "POST"):
        text = request.form.get("text", "");
        out = lex(text)
    return render_template("index.html", data=out, text=text)


if __name__ == "__main__":
    app.run(debug=True)