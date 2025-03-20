from flask import Flask, request, jsonify

# Initialize extensions
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
    
    # Hash the password for better security
    hashed_password = Bcrypt.hashpw(password.encode('utf-8'), Bcrypt.gensalt()).decode('utf-8')

    try:
        user = auth.create_user_with_email_and_password(email, password)
        user_id = user['localId']

        # Store user data in Firebase
        db.child("users").child(user_id).set({
            "email": email,
            "password": hashed_password,
            "user_id": user_id
        })

        return jsonify({"message": "User registered successfully", "user_id": user_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/login', methods=['POST'])
def login_user():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    try:
        user = auth.sign_in_with_email_and_password(email, password)
        user_id = user['localId']
        token = generate_token(user_id)
        return jsonify({"message": "Login successful", "token": token}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    