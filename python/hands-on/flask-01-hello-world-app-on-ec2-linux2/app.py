from flask import Flask

app = Flask(__name__)

@app.route("/")
def head():
    return "Sampiyon Fenerbahce"

@app.route("/second")
def second():
    return """Sarı lacivert rengimiz Fenerbahçe'm her şeyimiz 
    Hiçbir şeye değişmeyiz 
    Çünkü FENERBAHCELIYIZ"""

@app.route("/tuba")
def tuba():
    return "Sevde & Tuba % Ömer"

@app.route("/tuba/sevde")
def third():
    return "Bu sayfa Tuba nin altindaki Sevde altdizinde bulunmaktadir"

@app.route("/forth/<string:id>")  #dinamik id yapilarinin sonuna hangi rakam koysak o rakam cikar.100lerce alt dizine ulasmak icin bu yapiyi kullaniyoruz.100, sayfaya ulasmak icin /100 yazarak o dizine bu kodla gider
def forth(id):
    return f"Suanda acik olan makale numaraniz {id}'dir "

if __name__ == "__main__":
    app.run(debug = True)

