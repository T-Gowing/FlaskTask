from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import fruits
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'Are you feeling fruity????'}), 200

@app.route('/api/fruits', methods=['GET', 'POST'])
def fruits_handler():
    fns = {
        'GET': fruits.index,
        'POST': fruits.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/api/fruits/<int:fruit_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def fruit_handler(fruit_id):
    fns = {
        'GET': fruits.show,
#         'PATCH': fruits.update,
#         'PUT': fruits.update,
        'DELETE': fruits.destroy
    }
    resp, code = fns[request.method](request, fruit_id)
    return jsonify(resp), code

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500

if __name__ == "__main__":
    app.run(debug=True)
