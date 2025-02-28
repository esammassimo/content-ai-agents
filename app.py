import streamlit as st

st.set_page_config(page_title="AI Content & Video Summarization", layout="wide")

st.title("🚀 AI Content Tools")
st.write("🔹 Use the sidebar to navigate between different features.")

st.markdown(
    """
    ### Available Features:
    - 📄 **[Generate SEO Content from Excel](./pages/1_Generazione_Contenuti.py)**
    - 🎬 **[Summarize YouTube Videos](./pages/2_Riassunto_Video.py)**

    Select a feature from the sidebar! 👈
    """
)