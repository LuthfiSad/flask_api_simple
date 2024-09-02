from flask import Flask, send_from_directory
from src.config.db_config import Config
from src.models.models import db
from src.costumer.costumer_router import costumer_routes
from src.order.order_router import order_routes
from src.auth.auth_router import auth_routes
from src.user.user_router import user_routes
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config.from_object(Config)

# Inisialisasi SQLAlchemy dengan app
db.init_app(app)

# Konfigurasi untuk unggah file
app.config['UPLOAD_FOLDER'] = 'storage/image/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Endpoint untuk mengakses file yang diunggah
@app.route('/storage/image/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Daftarkan blueprint rute
app.register_blueprint(costumer_routes)
app.register_blueprint(order_routes)
app.register_blueprint(auth_routes)
app.register_blueprint(user_routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Membuat tabel di database jika belum ada
    app.run(debug=True)
