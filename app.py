from flask import Flask, render_template, request, redirect, url_for
from utils.model import generate_image_and_recommendations
import os
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/generated_images'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shop', methods=['POST'])
def shop():
    prompt = request.form['prompt']
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    image_path, recommendations = generate_image_and_recommendations(prompt, timestamp)

    return render_template('shop.html', 
                           user_prompt=prompt, 
                           generated_image=image_path, 
                           recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
