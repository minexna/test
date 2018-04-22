from flask import Flask
from flask import render_template
app = Flask(__name__)
import socket

@app.route("/")
def hello():
    #my=ip=get_ip()
    return render_template("index.html", my_ip=get_ip(),moja_suma=22,moja_roznica=odejmowanie())
def odejmowanie():
    a=743
    b=219
    return str(a-b)

@app.route("/test")
def test():
    return "test adresu"
    
def get_ip():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    return ip_address

@app.route("/ilo")
def ilo():
    a=5
    b=6
    return str(a*b)
	
if __name__ == '__main__':
    app.run()