from flask import Flask, render_template, request, redirect, url_for
from utils.model import generate_image_and_recommendations
import os
import time
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/generated_images'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shop', methods=['POST'])
def shop():
    prompt = request.form['prompt']
    timestamp = int(time.time())

    image_path, recommendations = generate_image_and_recommendations(prompt, timestamp)

    if image_path:
        generated_image = image_path.replace("static/", "")
    else:
        generated_image = ""

    recommendations = [img.replace("static/", "") for img in recommendations]

    return render_template('shop.html',
                           prompt=prompt,
                           generated_image=generated_image,
                           recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
