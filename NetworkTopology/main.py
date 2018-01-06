
from NetworkTopology import *
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get():
    return jsonify({"msg": "Invalid request: use POST!"})


@app.route('/', methods=['POST'])
def process_input():
    try:
        inpoo = request.get_json()
        validate_input(inpoo)

        edges_raw = inpoo["inList"]
        edges = [(e[0], e[1]) for e in edges_raw]
        adj = create_adj(edges)
        topology_type = determine_topology(adj)
        return jsonify({'type': topology_type})

    except Exception as e:
        return jsonify({"msg": "an error occured"})


@app.errorhandler(500)
def server_error(e):
    return jsonify({"msg": "A server error occurred. Please try again later."})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
