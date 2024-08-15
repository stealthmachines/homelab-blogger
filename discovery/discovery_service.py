from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for active nodes
nodes = []

@app.route('/register', methods=['POST'])
def register_node():
    node_info = request.json
    if node_info and 'address' in node_info:
        nodes.append(node_info['address'])
        return jsonify({"message": "Node registered successfully."}), 201
    else:
        return jsonify({"message": "Invalid node data."}), 400

@app.route('/nodes', methods=['GET'])
def get_nodes():
    return jsonify({"nodes": nodes}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
