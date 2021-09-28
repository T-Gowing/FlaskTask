from werkzeug.exceptions import BadRequest

fruits = [
    {'id': 1, 'fruit': 'strawberry', 'taste': 'sweet', 'colour': 'red'},
    {'id': 2, 'fruit': 'apple', 'taste': 'sweet', 'colour': 'red'},
    {'id': 3, 'fruit': 'banana', 'taste': 'potassuim', 'colour': 'yellow'},
    {'id': 4, 'fruit': 'blackcurrant', 'taste': 'sour', 'colour': 'purple'},
    {'id': 5, 'fruit': 'lemon', 'taste': 'sour', 'colour': 'yellow'},
    {'id': 6, 'fruit': 'mango', 'taste': 'sweet', 'colour': 'orange'},
    {'id': 7, 'fruit': 'passionfruit', 'taste': 'sour', 'colour': 'yellow'},
    {'id': 8, 'fruit': 'pineapple', 'taste': 'bitter', 'colour': 'yellow'},
    {'id': 9, 'fruit': 'kiwi', 'taste': 'sour', 'colour': 'green'},
    {'id': 10, 'fruit': 'raspberry', 'taste': 'good', 'colour': 'pink'}
]

def index(req):
    return [fruit for fruit in fruits], 200

def show(req, fruit_id):
    return find_by_fruit_id(fruit_id), 200

def create(req):
    new_fruit = req.get_json()
    new_fruit['id'] = max([fruit['id'] for fruit in fruits]) + 1
    fruits.append(new_fruit)
    return new_fruit, 201

# def update(req, fruit_id):
#     fruit = find_by_fruit_id(fruit_id)
#     data = req.get_json()
#     print(data)
#     for key, val in data.items():
#         fruit[key] = val
#     return fruit, 200

def destroy(req, fruit_id):
    fruit = find_by_fruit_id(fruit_id)
    fruits.remove(fruit)
    return fruit, 204

def find_by_fruit_id(fruit_id):
    try:
        return next(fruit for fruit in fruits if fruit['id'] == fruit_id)
    except:
        raise BadRequest(f"We don't have that fruit with id {fruit_id}!")