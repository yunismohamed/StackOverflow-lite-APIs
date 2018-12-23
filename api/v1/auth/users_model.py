"""
User details are added or removed here"""

from flask import jsonify, make_response

all_users = [] # DB of all the registered users

def add_user(username, email, password):
    for user in all_users:
        if username == user['username']:
            return jsonify('Username exists'), 400
        if email == user['email']:
            return jsonify('Email exists'), 400
    
    new_user = {
        'username': username,
        'email': email,
        'password': password
    }
    all_users.append(new_user)    
    response = make_response(jsonify({
        'Status': 'Successfully registered',
        'Username': username
    }))
    
    return response


           
           
