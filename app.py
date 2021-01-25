
from flask import Flask, jsonify, request
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'khandelwal'
socketio = SocketIO(app)


users = [
{'id':101, 'name':'abhay', 'age':20},
{'id':102, 'name':'khushboo', 'age':21},
{'id':103, 'name':'nisha', 'age':22}
]

@app.route('/')
def index():
	return app.send_static_file('index.html')

@socketio.on('msg')
def handle_msg(data):
    socketio.emit('push', data, broadcast=True, include_self=False)

@app.route('/users')
def getUsers():
	print(users)
	return jsonify(users)

@app.route('/users/<id>')
def getuser(id):
	# result = [u for u in users if u ['id']==id]
	result = list(filter(lambda u: str(u['id'])==id, users))
	return jsonify(result)

if __name__=="__main__":
    socketio.run(app)


# from flask import Flask, jsonify, request

# app = Flask(__name__)

# users = [
# {'id':101, 'name':'abhay', 'age':20},
# {'id':102, 'name':'khushboo', 'age':21},
# {'id':103, 'name':'nisha', 'age':22}
# ]

# @app.route('/')
# def index():
# 	return app.send_static_file('index.html')

# @app.route('/users')
# def getUsers():
# 	return jsonify(users)

# @app.route('/users/<id>')
# def getuser(id):
# 	# result = [u for u in users if u ['id']==id]
# 	result = list(filter(lambda u: str(u['id'])==id, users))
# 	return jsonify(result)

# if __name__=="__main__":
# 	app.run()