from flask import Flask, render_template

app = Flask(__name__)

# criar a 1ª pagina do site
# pagina sempre tem um route = qual é o caminho q vem depois do dominio
# route -> calculapython15.com/
# função = o que você quer exibir naquela página

@app.route("/")
def page1():
    return render_template("index.html")








# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

# servidor do heroku


