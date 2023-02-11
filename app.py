from flask import Flask, request, make_response, jsonify
# import json
from dbhelpers import run_statement


app = Flask(__name__)

@app.get('/api/candy')
def list_Candy():
    result = run_statement('CALL list_Candy')
    keys = ["name"]
    response = []
    if (type(result) == list):
        for candy in result:
            response.append(dict(zip(keys,candy)))
        return make_response(jsonify(response), 200)
    else:
        return make_response(jsonify(result), 500)

# post works as it adds to DB but message is wrong
@app.post('/api/candy')
def add_Candy():
    name = request.json.get('name')
    result = run_statement('CALL add_Candy (?)',[name])
    if result == None:
        return "Success"
    else: 
        return "There was an error"




app.run(debug=True)