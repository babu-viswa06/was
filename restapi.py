# GET - Retrieve all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data_store), 200 # type: ignore

# POST - Add a new item to the list
@app.route('/items', methods=['POST'])
def post_item():
    item = request.get_json()
    data_store.append(item)
    return jsonify(item), 201

# PUSH (treated as PUT) - Update or insert item at a specific index
@app.route('/items/<int:index>', methods=['PUT'])
def push_item(index):
    item = request.get_json()
    if index < len(data_store):
        data_store[index] = item
        return jsonify(item), 200
    elif index == len(data_store):  # allow appending
        data_store.append(item)
        return jsonify(item), 201
    else:
        return jsonify({'error': 'Index out of range'}), 400

# DELETE - Remove item at a specific index
@app.route('/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    if 0 <= index < len(data_store):
        removed = data_store.pop(index)
        return jsonify(removed), 200
    return jsonify({'error': 'Index out of range'}), 404
