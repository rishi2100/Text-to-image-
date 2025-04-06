import random
import os
from utils.image_utils import copy_random_image

def generate_image_and_recommendations(prompt, timestamp):
    # Simulate generation (copy random image)
    generated_img = copy_random_image('deepfashion', f'static/generated_images/generated_{timestamp}.jpg')
    
    # Simulate recommendations
    rec_images = os.listdir('deepfashion')
    recommendations = random.sample(rec_images, 6)

    rec_data = [{"path": f"deepfashion/{img}", "title": img.split('.')[0]} for img in recommendations]
    return f"generated_images/generated_{timestamp}.jpg", rec_data
