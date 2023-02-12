from flask import Flask, request, make_response, jsonify
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

@app.post('/api/candy')
def add_Candy():
    name = request.json.get('name')
    result = run_statement('CALL add_Candy (?)',[name])
    if result == None:
        return make_response(jsonify("Candy added: {}".format(name)), 200)
    else: 
        return make_response(jsonify("Something went wrong"), 500)

@app.patch('/api/candy')
def update_Candy():
    id = request.json.get('id')
    name = request.json.get('name')
    result = run_statement('CALL update_Candy (?,?)',[id,name])
    if result == None:
        return make_response(jsonify("Candy name updated: {}".format(name)), 200)
    else:
        return make_response(jsonify("Something went wrong"), 500)

@app.delete('/api/candy')
def delete_Candy():
    id = request.json.get('id')
    result = run_statement('CALL delete_Candy (?)', [id])
    if result == None:
        return make_response(jsonify("Candy deleted"), 200)
    else:
        return make_response(jsonify("Something went wrong"), 500)




app.run(debug=True)