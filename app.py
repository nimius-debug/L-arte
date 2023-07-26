import streamlit as st
from components.waxin_form import display_waxing_form 
from components.page_components import sidebar, set_backgound_img, display_logo

st.set_page_config(
        page_title="INFORMED CONSENT RELEASE",
        page_icon=":leaves:",
        layout="centered",
        initial_sidebar_state="collapsed",
    )
def main():
    sidebar()
    set_backgound_img()
    display_logo()
    display_waxing_form()
    # Create a canvas component
    
    
if __name__ == "__main__":
    main()