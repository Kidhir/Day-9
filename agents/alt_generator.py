# agents/alt_generator.py

import requests
from io import BytesIO

# Hugging Face API token (free)
HF_TOKEN = "hf_SWZGjVnvdLhzuMfGhtnowiZZHjZaqFjyU"  # Replace with your actual token

def generate_alt_text(image_path):
    try:
        if image_path.startswith("http"):
            response = requests.get(image_path)
            img = Image.open(BytesIO(response.content)).convert("RGB")
        else:
            img = Image.open(image_path).convert("RGB")

        caption = processor(img, return_tensors="pt").to("cpu")
        out = model.generate(**caption)
        result = tokenizer.decode(out[0], skip_special_tokens=True)
        return result
    except Exception as e:
        print(f"[Alt Generator Error] Could not process image: {image_path}")
        print("Reason:", e)
        return "Image description could not be generated. (Do not use phrases like 'image of' or 'picture of'.)"
