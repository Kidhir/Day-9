# app.py (Streamlit)
import streamlit as st
from graph import final_graph

st.title("🧠 AI-Powered Alt Text Generator")

url = st.text_input("Enter a website URL to scan for images")
context = st.text_area("Optional context (e.g., page description)")

if st.button("Generate Alt Text"):
    with st.spinner("Running agents..."):
        try:
            result = final_graph.invoke({"url": url, "context": context})
            st.success("Alt text generation complete!")
            st.write(result)
        except Exception as e:
            st.error(f"Error: {e}")
