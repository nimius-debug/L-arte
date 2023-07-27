import streamlit as st
import json
from components.waxin_form import display_waxing_form 
from components.page_components import sidebar, set_backgound_img, display_logo, hide_footer_streamlit

st.set_page_config(
        page_title="INFORMED CONSENT RELEASE",
        page_icon=":leaves:",
        layout="centered",
        initial_sidebar_state="collapsed",
    )

@st.cache_data
def load_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def main():
    if 'app_text' not in st.session_state:
        st.session_state.app_text = load_json_data('data/multi_lang.json')
    
    if 'language' not in st.session_state:
        st.session_state.language = 'english'
    
    hide_footer_streamlit()
    sidebar()
    set_backgound_img()
    display_logo()
    display_waxing_form()
    # Create a canvas component
    
    
if __name__ == "__main__":
    main()