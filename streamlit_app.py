import streamlit as st

st.set_page_config(page_title="SlideGen", layout="wide")

st.title("🚀 SlideGen App")
st.write("This will be your interactive slide generator!")

# File upload
uploaded_file = st.file_uploader("Upload a topic file (e.g., .txt or .docx)", type=["txt", "docx"])

# Options
font = st.selectbox("Choose a font", ["Arial", "Times New Roman", "Comic Sans"])
theme = st.radio("Select theme", ["Light", "Dark", "Minimal"])

# Generate button
if st.button("Generate Slides"):
    if uploaded_file is not None:
        st.success(f"Slides generated with font '{font}' and theme '{theme}'!")
        # You can add real generation code here later
    else:
        st.error("Please upload a file first.")
