from flask import Flask,render_template,request
from urllib.request import urlopen
import json
import xmltodict
import requests

app = Flask(__name__)

urlcurp= "https://curp.nubarium.com/renapo/v2/valida_curp"
url = "https://jsonplaceholder.typicode.com/users/1"
urlxml = "http://restapi.adequateshop.com/api/Traveler?page=1("


@app.route('/archivos', methods=['GET'])
def archivos():

    return render_template('index.html')


@app.route('/API/JSON/jsonplaceholder/<string:name>',methods=['GET'])
def api(name):
    response = urlopen(url)
    jsonO = response.read()
    date = json.loads(jsonO)
    return date[name]


@app.route('/API/XML/restapi/<string:name>',methods=['GET'])
def apiXML(name):
    response = urlopen(urlxml)
    jsonXml = xmltodict.parse(response.read())
    date = json.dumps(jsonXml)
    v= date.find("email")
    print(v)
    return date


@app.route('/', methods=['POST'])
def curp():

    curp= json.dumps({
        "CURP": "RAZR811011HVZMPB01",
        "documento": "0"
    })
    head={
        'Content-Type':'application/json'
    }
    response= requests.request("POST", urlcurp, headers=head, dat=curp)
    return response.json()


@app.route('/INE/checarIne',methods=['POST'])
def checarIne():
    pas= request.authorization[""]

    return 0

if __name__ == '__main__':
    app.run(debug=True)
