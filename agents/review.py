# agents/review.py

import streamlit as st

def review_and_edit(image_alts):
    st.markdown("### 🔍 Review and Edit Alt Texts")
    final_output = []

    for i, img in enumerate(image_alts):
        st.image(img['src'], width=300, caption=f"Image {i+1}")
        new_alt = st.text_input(f"Alt text for Image {i+1}", value=img['alt'], key=f"alt_{i}")
        final_output.append({
            "src": img['src'],
            "alt": new_alt
        })

    return final_output
