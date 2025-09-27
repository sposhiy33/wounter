from flask import Flask, render_template, request, jsonify
import json
import os

# Initialize the Flask application
app = Flask(__name__)

# This route serves the main HTML page.
@app.route('/')
def index():
    """
    Renders the main HTML page for the point editor.
    """
    return render_template('index.html')

# This route handles the image and coordinate file upload.
@app.route('/upload', methods=['POST'])
def upload_image():
    """
    Handles the upload of an image and its corresponding points.

    In a real-world scenario, you would add the logic here to:
    1. Receive the image file and the list of points.
    2. Save the image and create a text file for the coordinates.
    3. Send both files to your remote compute cluster via an API call.
    """
    if request.method == 'POST':
        # The image file can be accessed via request.files
        # image_file = request.files['image']
        
        # The points data can be accessed from the form data
        # points = json.loads(request.form.get('points'))
        
        # Since this is a frontend-focused example, we will simulate
        # the backend processing and just return a success response.
        
        # In your actual implementation, you would replace this with a call
        # to your compute cluster.
        # result = send_to_cluster(image_file, points)

        return jsonify({'status': 'success', 'message': 'Image and points received.'})
    
    return jsonify({'status': 'error', 'message': 'Invalid request method.'}), 405

# This allows running the app directly from the script
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
