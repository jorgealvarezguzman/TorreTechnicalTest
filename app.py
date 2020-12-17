from flask import Flask, render_template, redirect, request
import requests
import json

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def index():
    return redirect('opportunities')


@app.route('/bio/<int:id>', methods = ['GET'])
def getBio(id):
    req = requests.get(f'https://torre.bio/api/bios/{id}')
    data = json.loads(req.content)
    return render_template('index.html', data=data) 


@app.route('/opportunities/', methods = ['GET', 'POST'])
@app.route('/opportunities/<string:keyword>', methods = ['GET', 'POST'])
def getOportunities(keyword=None):
    req = requests.post('https://search.torre.co/opportunities/_search/?offset=0&size=18&aggregate=false', json = {"test": "test"})
    data = req.json()

    keyword = request.form.get("search")

    if (keyword):
        filtered_data = [x for x in data['results'] if (keyword.lower() in json.dumps(x).lower())]
        return render_template('opportunity.html', opportunities=filtered_data)

    return render_template('opportunity.html', opportunities=data['results'])


@app.route('/test', methods = ['GET', 'POST'])
def test():
    req = requests.post('https://search.torre.co/opportunities/_search/?offset=0&size=10&aggregate=false', json = {"test": "test"})
    data = req.json()
    return render_template('index.html', data=data['results'])