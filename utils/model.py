from utils.image_indexer import index_deepfashion_images
import random
import shutil

# Load once globally
image_db = index_deepfashion_images()

def match_prompt_to_image(prompt):
    prompt_words = prompt.lower().split()
    matches = []

    for entry in image_db:
        score = sum(word in entry['tags'] for word in prompt_words)
        if score > 0:
            matches.append((score, entry['path']))

    matches.sort(reverse=True)  # Highest score first
    return [m[1] for m in matches]

def generate_image_and_recommendations(prompt, timestamp):
    matched_images = match_prompt_to_image(prompt)

    if not matched_images:
        return None, []

    # "Generate" image = top match
    generated_img_path = matched_images[0]
    output_path = f"static/generated_images/generated_{timestamp}.jpg"
    shutil.copy(generated_img_path, output_path)

    # Recommend 6 similar ones
    recommendations = matched_images[1:7]
    return output_path, recommendations