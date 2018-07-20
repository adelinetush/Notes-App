from flask import Flask, render_template
from flask import jsonify, request, abort, g, url_for

from app import app
from app.controller.UserController import UserController
from app.controller.EntryController import EntryController

user = UserController()
entry = EntryController()

uname = ""
upassword = ""

@app.route('/')
@app.route("/index")
def main():
    return render_template('index.html', name="Ad")

@app.route('/signup')
@app.route('/signup')
def signup():
    return render_template('signup.html', title='SignUp')


#Saving and retrieving
@app.route("/auth/register")
def register():
    name = request.args.get('username')
    email = request.args.get('email')
    password = request.args.get('password')
    if email is None or password is None:
        abort(400)
    response = user.register(name, email, password)
    print(response)
    return jsonify(response)

@app.route("/auth/login")
def login():
    email = request.args.get('email')
    password = request.args.get('password')
    response = user.login(email, password)
    return jsonify(response)

#Entry Functions
@app.route("/ae",methods=['POST'])
def addEntry():
    r = request.get_json()
    response = entry.add_entry(r)
    return jsonify(response)

@app.route("/api/v1/gue", methods=['GET'])
def get_user_entry():
    email = request.args.get('email')
    res = entry.get_user_entry(email)
    return jsonify(res)

@app.route("/api/v1/gae")
def get_all_entry():
    res = entry.get_all_entry()
    return jsonify(res)

@app.route("/de")
def delete_entry():
    id = request.args.get('id')
    ir = int(id)
    res = entry.delete_entry(ir)
    return jsonify(res)

@app.route("/api/v1/gse", methods=['GET'])
def return_entry():
    id = request.args.get('id')
    ir = int(id)
    res = entry.return_entry(ir)
    return jsonify(res)

@app.route("/api/v1/ue" , methods=['POST'])
def update_entry():
    ent = request.get_json()
    res = entry.update_entry(ent)
    return jsonify(res)