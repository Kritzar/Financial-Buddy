from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from datetime import datetime, timedelta
import random 
from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import bcrypt
# from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
# from firebase_config import config
from pyrebase import pyrebase
# import jwt
import pandas as pd 
import pickle 

from transaction_data import get_transactions_data
from model import predict_next_week 


app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret_key'

config = {
  'apiKey': "AIzaSyCvDDl87reSFpUrfUXhJ2qhjTqA2OmhG94",
  'authDomain': "financial-87011.firebaseapp.com",
  'databaseURL': "https://financial-87011-default-rtdb.firebaseio.com",
  'projectId': "financial-87011",
  'storageBucket': "financial-87011.firebasestorage.app",
  'messagingSenderId': "181373018422",
  'appId': "1:181373018422:web:b7fad63b937cefb4ea9397",
  'measurementId': "G-3P6MP4Y72E"
}
# User model
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(200), nullable=False)

# # Create the database
# with app.app_context():
#     db.create_all()

# Registration endpoint

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

def generate_token(user_id):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    token = jwt.encode({"user_id": user_id, "exp": expiration}, app.config['SECRET_KEY'], algorithm="HS256")
    return token


@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    name = data.get("name")
 
    # hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    try:
        user = auth.create_user_with_email_and_password(email, password)
        user_id = user['localId']
        
        # Store user data in Firebase Realtime Database
        db.child("users").child(user_id).set({
            "name": name,
            "email": email,
            "user_id": user_id
        })

        transaction_data = get_transactions_data(call_api=False)  # TODO: call api 
        set_transactions_in_database(transaction_data, user_id) 

        return jsonify({"message": "User registered successfully", "user_id": user_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Login endpoint
@app.route('/login', methods=['POST'])
def login_user():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    try:
        user_id = auth.sign_in_with_email_and_password(email, password)["localId"]
        ensure_data_is_updated(user_id) 
        
        return jsonify({"message": "Login successful", "user_id": user_id }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400



@app.route("/get_transactions_data", methods=["GET"])
def get_last_data_api():
    user_id =request.args.get("user_id")

    print(user_id)
    try:
        transactions = get_data_from_database(user_id)
        if not transactions:
            return jsonify({"error": "Transactions not found"}), 404
        
        predictions = predict_next_week(transactions) 
        summary = get_finance_summary(predictions) 
        return jsonify({'transactions': transactions, 'predictions': predictions, 'summary': summary}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/post_transactions_data_into_backend", methods=["POST"])
def get_last_data():
    data = request.json
    userid=data.get("user_id")
    try:
        all_data = get_transactions_data(call_api=True)
        user = db.child("users").child(userid).get().val()
        if not user:
            return jsonify({"error": "User not found"}), 404

        db.child("transactions").child(userid).set(all_data)
        return jsonify({"message": "Transaction added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500 


def get_finance_summary(data): 
    expenses = int(sum(row['amount'] for row in data) )
    income = int(expenses * (1+0.3*random.random()))
    return {
        'expenses': expenses, 
        'income': income, 
        'budget': income - expenses
    }


def ensure_data_is_updated(user_id): 
    some_old_data = get_data_from_database(user_id, 5) 
    days_missing = no_of_days_missing(some_old_data) 
    rows_to_insert: int = days_missing * 3 

    print('inserting', rows_to_insert, 'rows')
    data_to_insert = get_transactions_data(call_api=False, rows=rows_to_insert)  # TODO: call api  
    add_transactions_in_databse(data_to_insert, user_id)
    
    
    

def no_of_days_missing(data, max_days = 30) -> int: 
    if not data: 
        return max_days 

    last_date = data[-1]['date']  
    date_obj = datetime.strptime(last_date, '%Y-%m-%d')
    
    
    delta = datetime.today() - date_obj 
    return delta.days




def set_transactions_in_database(data, user_id): 
    db.child("transactions").child(user_id).set(data) 

def get_data_from_database(user_id, days=30):  
    data = db.child("transactions").child(user_id).order_by_child("date") \
        .start_at((datetime.today() - timedelta(days=days)).strftime("%Y-%m-%d")).get().val()
    data = list( data.values()) if data else [] 

    return data 

def get_all_data_from_database(user_id): 
    return db.child("transactions").child(user_id).get().val()

def add_transactions_in_databse(data, user_id): 
    for elem in data:
        db.child("transactions").child(user_id).push(elem) 


# Protected route example
# @app.route('/protected', methods=['GET'])
# @jwt_required()
# def protected():
#     current_user = get_jwt_identity()
#     return jsonify(logged_in_as=current_user), 200
if __name__ == '__main__':
    app.run(debug=True) 
    # ensure_data_is_updated("dv6xDdDZnSh3KN5FLRTKgMklYJD2")
   