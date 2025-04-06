import os

def index_deepfashion_images(base_path='deepfashion/img/'):
    indexed_images = []

    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png')):
                full_path = os.path.join(root, file)
                # Use folder names as tags (e.g., category, style)
                tags = root.lower().split(os.sep)
                indexed_images.append({
                    'path': full_path,
                    'tags': tags
                })

    return indexed_images
