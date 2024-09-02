from flask import Flask, jsonify, request
from config import Config
from src.models.models import db, User
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config.from_object(Config)

# Inisialisasi SQLAlchemy dengan app
db.init_app(app)

# Service untuk validasi email
def is_email_unique(email):
    return User.query.filter_by(email=email).first() is None

# Endpoint untuk mendapatkan semua user
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'name': user.name, 'email': user.email} for user in users])

# Endpoint untuk membuat user baru dengan validasi email
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    
    if not data or not data.get('name') or not data.get('email'):
        return jsonify({'error': 'Name and Email not required'}), 400
    
    # Validasi apakah email sudah ada di database
    if not is_email_unique(data['email']):
        return jsonify({'error': 'Email already exists'}), 400
    
    try:
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'id': new_user.id, 'name': new_user.name, 'email': new_user.email}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Error occurred while creating user'}), 500

# Endpoint untuk menghapus user berdasarkan ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200

# Endpoint untuk memperbarui (update) user berdasarkan ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user = User.query.get(user_id)
    
    print(data.get('name', user.name))
    
    if not data or not data.get('name') or not data.get('email'):
        return jsonify({'error': 'Name and Email not required'}), 400
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    # Validasi apakah email baru sudah ada di database, kecuali untuk user yang sama
    if user.email != data['email'] and not is_email_unique(data['email']):
        return jsonify({'error': 'Email already exists'}), 400
    
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    
    db.session.commit()
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 200

# Main program
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Membuat tabel di database jika belum ada
    app.run(debug=True)