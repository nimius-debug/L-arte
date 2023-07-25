import streamlit as st
from components.form import form , logo, backgound_img,sidebar

st.set_page_config(
        page_title="INFORMED CONSENT RELEASE",
        page_icon=":leaves:",
        layout="centered",
        initial_sidebar_state="collapsed",
    )
def main():
    sidebar()
    backgound_img()
    logo()
    form()
    # Create a canvas component
    
    
if __name__ == "__main__":
    main()