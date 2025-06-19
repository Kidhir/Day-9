# app.py

import streamlit as st
import json

from agents.image_scanner import scan_images
from agents.alt_generator import generate_alt_text
from agents.rag_retriever import retrieve_best_practices
from agents.review import review_and_edit

st.set_page_config(page_title="Auto Alt Text Generator", layout="wide")
st.title("🧠 Auto Alt Text Generator (Free AI Version)")
st.markdown("Generate alt text for images using Hugging Face vision API and local AI for accessibility refinement.")

# 📌 Input field for website or folder
url_or_folder = st.text_input("🔗 Enter website URL or local folder path")

if st.button("🚀 Scan and Generate Alt Text"):
    st.info("🔍 Scanning images...")
    images_to_fix = scan_images(url_or_folder)
    images_to_fix = [img for img in images_to_fix if img.get("src")]  # Remove bad entries

    if not images_to_fix:
        st.warning("❌ No images found or all images have proper alt text.")
    else:
        st.success(f"✅ Found {len(images_to_fix)} image(s) needing alt text.")
        generated_alts = []

        for img in images_to_fix:
            src = img.get("src")
            try:
                st.image(src, width=300, caption="Original Image")
            except Exception as e:
                st.warning(f"⚠️ Could not preview image: {src}")
                continue  # Skip this image

            alt = generate_alt_text(img)
            enhanced_alt = retrieve_best_practices(alt)

            st.markdown(f"📝 **Generated Alt Text:** _{enhanced_alt}_")
            generated_alts.append({
                "src": src,
                "alt": enhanced_alt
            })

        # 🖊️ Review and edit
        final_output = review_and_edit(generated_alts)

        # 💾 Download
        if final_output:
            st.download_button(
                label="⬇️ Download Alt Text JSON",
                data=json.dumps(final_output, indent=2),
                file_name="alt_texts.json",
                mime="application/json"
            )
        else:
            st.warning("No alt text available to download.")
