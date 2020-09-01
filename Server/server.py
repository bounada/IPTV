from flask import Flask
import json
app = Flask(__name__)

@app.route("/update", methods=['POST'])
def update():
    with open('tv.json') as json_file:
        data = json.load(json_file)
    return json.dumps(data)

@app.route("/recitation", methods=['POST'])
def recitation():
    with open('recitation.json') as json_file:
        data = json.load(json_file)
    return json.dumps(data)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=7000, debug=True)