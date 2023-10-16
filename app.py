import streamlit as st
import json
from components.waxin_form import display_waxing_form
from components.page_components import set_backgound_img, display_logo, hide_footer_streamlit,horizontal_menu
from components.price_list import Price_page
from components.facials_form import display_facial_form
from components.home import display_home
from components.footer import footer

st.set_page_config(
        page_title="skinbylauraLo",
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
    # Only set the default value if it hasn't been set yet
    st.session_state.language = lang
    
####################################################################
def main():
    if 'app_text' not in st.session_state:
        st.session_state.app_text = load_json_data('data/multi_lang.json')
    if 'language' not in st.session_state:
        st.session_state.language = 'spanish'  # Default language
        
    #gloabal settings
    set_backgound_img()
    hide_footer_streamlit()
    # database
    
    selection = horizontal_menu()
    ##### Home #####
    if selection == 'Home':
        ###########ssession state################
        current_language = st.session_state.language.capitalize()
        language = st.radio(
            label="Select Language",
            options=["English", "Spanish"],
            index=0 if current_language == "English" else 1,  # Set the default index based on current language
            horizontal=True,
        ).lower()  # convert to lower case
        
        #Update the language setting
        language_settings(language)
        display_logo()
        ##### Home #####
        display_home()
        
        
    ##### Prices #####
    elif selection == 'Price':
            Price_page()
            
    ##### Forms #####
    elif selection == 'Forms':
        display_logo() 
        col1, col2 = st.columns(2)
        with col1:
            current_language = st.session_state.language.capitalize()
            language = st.radio(
                label="Select Language",
                options=["English", "Spanish"],
                index=0 if current_language == "English" else 1,  # Set the default index based on current language
                horizontal=True,
            ).lower()  # convert to lower case
            
            language_settings(language)
        with col2:
            forms = st.selectbox("Select Form",["Waxing Form", "Facial Form"] , index=0)
        
        if forms=="Waxing Form":
            display_waxing_form()
        else:
            display_facial_form()
    
    footer()
    
           
if __name__ == "__main__":
    main()