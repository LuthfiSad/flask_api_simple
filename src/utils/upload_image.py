from flask import request, current_app
from werkzeug.utils import secure_filename
import os
from ..utils.handle_response import handle_response
import uuid

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

def upload_image():
    if 'image' not in request.files:
        return False, handle_response(status=400, code="BAD_REQUEST", message="No file part")
    
    file = request.files['image']
    
    if file.filename == '':
        return False, handle_response(status=400, code="BAD_REQUEST", message="No selected file")
    
    if file and allowed_file(file.filename):
        # Generate a random filename
        ext = file.filename.rsplit('.', 1)[1].lower()
        filename = f"{uuid.uuid4().hex}.{ext}"
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return True, filename  # Return True and filename for success
    else:
        return False, handle_response(status=400, code="BAD_REQUEST", message="Invalid file type")

