import os
import random

def get_random_deepfashion_image(base_path='deepfashion/img/', num=1):
    image_paths = []

    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png')):
                image_paths.append(os.path.join(root, file))

    if not image_paths:
        return []

    return random.sample(image_paths, min(num, len(image_paths)))
