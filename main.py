import streamlit as st
from few_shot import Few_Shots_Post
from post_generator import generate_post

length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

def main():
    st.set_page_config(page_title="LinkedIn Post Generator", page_icon="💼", layout="centered")

    st.image("https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg", width=80)
    st.markdown("<h1 style='color: #0066cc;'>AI-Powered LinkedIn Post Generator and LLM</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #0066cc;'>Build by Sumanth Komirisetty</h4>",unsafe_allow_html=True)

    st.markdown("<p style='color: grey;'>Craft professional posts in seconds using Generative AI</p>", unsafe_allow_html=True)

    st.markdown("""
        <style>
        .stButton>button {
            background-color: #0066cc;
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 500;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    fs = Few_Shots_Post()
    with col1:
        selected_tag = st.selectbox("📌 Select Topic", options=fs.get_tags())
    with col2:
        selected_length = st.selectbox("📏 Post Length", options=length_options)
    with col3:
        selected_language = st.selectbox("🌐 Language", options=language_options)

    if st.button("Generate Post"):
        post = generate_post(selected_tag, selected_length, selected_language)
        st.markdown("### ✨ Generated LinkedIn Post:")
        st.code(post, language='markdown')

if __name__ == "__main__":
    main()
