import streamlit as st

st.set_page_config(page_title="SlideGen", layout="wide")

st.title("🚀 SlideGen App")
st.write("This is your AI-powered slide generator. Upload content, choose a style, and generate slides!")

# Upload section
uploaded_file = st.file_uploader("📄 Upload a topic file (TXT only for now)", type=["txt"])

# Options
font = st.selectbox("🖋️ Choose a font", ["Arial", "Times New Roman", "Comic Sans"])
theme = st.radio("🎨 Select theme", ["Light", "Dark", "Colorful"])

# Generate slides
if st.button("🎬 Generate Slides"):
    if uploaded_file is not None:
        content = uploaded_file.read().decode("utf-8")

        st.success("✅ Slide content generated!")
        st.subheader("🖼️ Slide Preview")
        st.markdown(f"**Font:** {font} | **Theme:** {theme}")
        
        for i, line in enumerate(content.split("\n")[:5],
