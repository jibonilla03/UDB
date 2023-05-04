from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1 style='text-align:center; color:#146C94'>Salvador Peña</h1>" \
        "<p>Mostrando html y css desde flask</p> " \
        "<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Universidad_don_bosco.jpg/800px-Universidad_don_bosco.jpg' width='300'/>" \
        "<img src='https://media0.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif?cid=ecf05e47tnhlhtxyd2s8lwv6p11ch1eqtpfncavs2b0sette&ep=v1_gifs_related&rid=giphy.gif&ct=g' " \
        "width='300'/>"


if __name__ == "__main__":
    app.run(debug=True)