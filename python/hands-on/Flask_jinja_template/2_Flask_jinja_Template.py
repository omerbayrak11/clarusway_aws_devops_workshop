from flask import Flask,render_template #index htmlyi calistirmak icin renden cagisiriyoruz

app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html",number1= 12,number2 = 13) # index html ye degisken tanimliyoruz cagirdigimizda gelmesi {{}}yaziyoruz

@app.route("/ikinci") #/http://127.0.0.1:5000/ikinci yazarsak ikinci sayfa cikar
def head2():
    return render_template("yeni.html",hazırlayan = "omer")

if __name__ == "__main__":
    app.run(debug = True)