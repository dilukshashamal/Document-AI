from flask import Blueprint, render_template, request, flash, send_from_directory, redirect
import os
from werkzeug.utils import secure_filename
from google.cloud import documentai_v1beta3 as documentai
import uuid
import json

# Create a Blueprint for the routes
main_routes = Blueprint('main_routes', __name__)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the main page (index)
@main_routes.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            # Save the uploaded file
            filename = secure_filename(file.filename)
            upload_folder = app.config['UPLOAD_FOLDER']
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
            file_path = os.path.join(upload_folder, filename)
            file.save(file_path)
            
            # Process the image with Google Document AI
            try:
                text, json_path = extract_text_from_image(file_path)
                return render_template('index.html', filename=filename, text=text, json_path=json_path)
            except Exception as e:
                flash(f"Error processing image: {e}")
                return redirect(request.url)
        else:
            flash('Invalid file type. Only PNG, JPG, and JPEG are allowed.')
            return redirect(request.url)

    return render_template('index.html')

# Route to download the JSON file
@main_routes.route('/download/<json_path>')
def download_file(json_path):
    return send_from_directory(app.config['UPLOAD_FOLDER'], json_path, as_attachment=True)

# Function to extract text from an image using Google Document AI
def extract_text_from_image(file_path):
    client = documentai.DocumentUnderstandingServiceClient()
    
    # Read the image file
    with open(file_path, 'rb') as image_file:
        input_config = documentai.types.InputConfig(
            mime_type='application/pdf' if file_path.endswith('.pdf') else 'image/jpeg',
            raw_document=documentai.types.RawDocument(content=image_file.read())
        )

    # Define the processor ID from config.py
    processor_id = app.config['OCR_PROCESSOR_ID']
    name = f'projects/{app.config["GCP_PROJECT_ID"]}/locations/us/documentProcessors/{processor_id}'
    
    # Process the document using Google Document AI
    request = documentai.types.ProcessRequest(name=name, raw_document=input_config.raw_document)
    result = client.process_document(request=request)

    # Extract the text from the result
    document = result.document
    text = ''
    for page in document.pages:
        for paragraph in page.paragraphs:
            for word in paragraph.words:
                text += word.text + ' '
            text += '\n'

    # Save the extracted text as a JSON file
    json_filename = f'{uuid.uuid4().hex}.json'
    json_path = os.path.join(app.config['UPLOAD_FOLDER'], json_filename)
    with open(json_path, 'w') as json_file:
        json.dump(document.to_dict(), json_file)

    return text, json_filename
