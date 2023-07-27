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

#######persist state across pages (contecnt and language)########
@st.cache_data
def load_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
    

def language_settings(lang):
    st.session_state.language = lang
    # print("language_settings", st.session_state.language)
    
####################################################################
def main():
    if 'app_text' not in st.session_state:
        st.session_state.app_text = load_json_data('data/multi_lang.json')
 
    language = st.sidebar.selectbox("Select Language", ["english", "spanish"], index=1)
    language_settings(language)
    
    sidebar()
    hide_footer_streamlit()
    set_backgound_img()
    display_logo() 
    display_waxing_form()
    # Create a canvas component
    
    
if __name__ == "__main__":
    main()