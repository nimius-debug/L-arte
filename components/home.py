import streamlit as st
from PIL import Image

def style_greeting():
    st.markdown(f"""
        <style>
            p.opening-text {{
                color: #9F836D;
                text-align: center;
                font-size: x-large;
                font-weight: 600;
            }}
        </style>
        <p class="opening-text"> {st.session_state.app_text[st.session_state.language]["home"]["greeting"]} </p>
    """, unsafe_allow_html=True)

def display_home():
    style_greeting()
    # st.subheader(st.session_state.app_text[st.session_state.language]["home"]["greeting"])
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown(st.session_state.app_text[st.session_state.language]["home"]["description"])
        
        with st.expander("About me... yawn. (boring)"):
            st.markdown(st.session_state.app_text[st.session_state.language]["home"]["background"])
            st.markdown(st.session_state.app_text[st.session_state.language]["home"]["school"])
        
        st.subheader(st.session_state.app_text[st.session_state.language]["home"]["bye"])
        
    with col2:
        st.image(Image.open('img/lalo.jpg'),use_column_width= "auto")
        st.caption("Laura Lo - en el 5th piso del trump tower (Trump 2024)")
        