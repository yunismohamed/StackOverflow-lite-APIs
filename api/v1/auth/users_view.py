"""
Responses to requests regarding the user are set up here"""

from flask import Blueprint, jsonify, request, make_response, json
from api.v1.auth.users_model import add_user

v1 = Blueprint('v1', __name__, url_prefix='/api/v1/auth')

@v1.route('/', methods=['GET'])
def index():
    """Redirects to the /"""

    response = jsonify({
        'Status': 'Success',
        'Message': 'You can successfully get to the root route'
    }), 200

    return response

@v1.route('/signup', methods=['POST'])
def register():
    """Creates a new user account"""
    
    try:
        new_user = request.get_json()   
        username = new_user['username']
        email = new_user['email']
        password = new_user['password']

    except:
        return jsonify({
        'Status': 'Invalid input format'        
    })    

    response = add_user(username, email, password)

    return response

   

