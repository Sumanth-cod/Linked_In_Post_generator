import streamlit as st
from few_shot import Few_Shots_Post

from post_generator import generate_post

length_options=["Short","Medium","Long"]
language_options=["English","Hinglish"]
def main():
    st.title("LinkedIn Post generator")

    col1,col2,col3=st.columns(3)
    fs=Few_Shots_Post()
    with col1:
        selected_tag=st.selectbox("Title",options=fs.get_tags())
    with col2:
        selected_length=st.selectbox("Title",options=length_options)

    with col3:
        selected_language=st.selectbox('Title',options=language_options)

    if st.button("Generate"):
        post=generate_post(selected_tag,selected_length,selected_language)
        st.write(post)
if __name__=="__main__":
    main()