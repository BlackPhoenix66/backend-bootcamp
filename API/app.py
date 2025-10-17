from flask import Flask, jsonify, request

app = Flask(__name__)

cart = []

@app.route('/cart', methods=['GET'])
def get_cart():
    return jsonify(cart)

@app.route('/cart', methods=['POST'])
def add_item():
    data = request.get_json()
    item = data.get('item')
    cart.append(item)
    return jsonify({'message': f"{item} добавлен в корзину", "cart": cart})

@app.route('/cart', methods=['DELETE'])
def clear_cart():
    cart.clear()
    return jsonify("message": "Корзина очищена")

@app.route('/cart/total', methods=['GET'])
def get_total():
    total = len(cart) * 100
    return jsonify({"total", total})

if __name__ == '__main__':
    app.run(debug=True)