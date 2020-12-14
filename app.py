from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def index():
    req = requests.get('https://torre.bio/api/bios/1')
    data = json.loads(req.content)
    return render_template('index.html', data=data)  


@app.route('/bio/<int:id>', methods = ['GET'])
def getBio(id):
    req = requests.get(f'https://torre.bio/api/bios/{id}')
    data = json.loads(req.content)
    return render_template('index.html', data=data) 


@app.route('/opportunities', methods = ['GET', 'POST'])
def getOportunities():
    req = requests.post('https://search.torre.co/opportunities/_search/?offset=0&size=10&aggregate=false', json = {"test": "test"})
    data = req.json()
    return render_template('index.html', data=data) 


@app.route('/people', methods = ['GET', 'POST'])
def getPeople():
    req = requests.post('https://search.torre.co/people/_search/?[offset=0&size=10&aggregate=false]', json = {"test": "test"})
    data = req.json()
    return render_template('index.html', data=data) 

    