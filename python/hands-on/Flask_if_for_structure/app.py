from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def head():
    first = "This is my first condition experience in Flask"
    return render_template("index.html",mesaj = first) # html de if yapilari kullanabiliriz.py dosyasinda tanimlayip serverde o mesaji yayinlayabiliriz true ise if false ise else dondurur.

@app.route("/for")
def for_example():
    names = ['omer','tuba','sevde']
    return render_template("deneme.html",isimler = names)

if __name__ == '__main__':
    app.run(debug = True)