
from flask import Flask, render_template, request, send_from_directory
import torch
from diffusers import DiffusionPipeline
import os
from datetime import datetime

app = Flask(__name__)

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load model and attention processors
pipeline = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2", torch_dtype=torch.float32
)
pipeline = pipeline.to(device)
pipeline.unet.load_attn_procs("NouRed/sd-fashion-products")

# Ensure directory exists
GENERATED_DIR = "static/generated"
os.makedirs(GENERATED_DIR, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    image_path = None
    if request.method == "POST":
        prompt = request.form["prompt"]
        generator = torch.Generator(device=device).manual_seed(42)

        image = pipeline(prompt, num_inference_steps=30, generator=generator).images[0]
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{timestamp}.png"
        image_path = f"{GENERATED_DIR}/{filename}"
        image.save(image_path)

    return render_template("index.html", image_path=image_path)

@app.route('/static/generated/<path:filename>')
def serve_image(filename):
    return send_from_directory(GENERATED_DIR, filename)

if __name__ == "__main__":
    app.run(debug=True)
