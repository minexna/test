from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
	
@app.route("/test")
def test():
    return "test adresu"
	
@app.route("/suma")
def suma():
    a=5
    b=6
    return str(a+b)

@app.route("/ilo")
def ilo():
    a=5
    b=6
    return str(a*b)
	
if __name__ == '__main__':
    app.run()