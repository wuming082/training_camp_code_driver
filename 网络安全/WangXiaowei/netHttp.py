from flask import Flask,request,render_template_string,Response,session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gdkfksy05lx0nv8dl'
@app.route("/")
def index():
    return open(__file__).read()

@app.route("/rce",methods=["GET"])
def rce():
    data = request.args.get("name","Guest")
    return render_template_string(f"Welcome {data}")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8989,debug=False)
