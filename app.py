import streamlit as st
import json
from components.waxin_form import display_waxing_form
from components.page_components import sidebar, set_backgound_img, display_logo, hide_footer_streamlit,horizontal_menu
from components.price_list import set_vertical_title, facials_prices
from components.facials_form import display_facial_form
from components.form_components import create_canvas
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
    
    #gloabal settings
    set_backgound_img()
    hide_footer_streamlit()
    # database
    
    selection = horizontal_menu()
    if selection == 'Forms':
        display_logo() 
        col1, col2 = st.columns(2)
        with col1:
            language = st.radio(
                label="Select Language",
                options=["English", "Spanish"],
                index=1,
                horizontal=True,
            ).lower()  # convert to lower case to match keys in json
            language_settings(language)
        with col2:
            forms = st.selectbox("Select Form",["Waxing Form", "Facial Form"] , index=0)
        
        if forms=="Waxing Form":
            display_waxing_form()
        else:
            display_facial_form()
    # elif selection == 'Price':
    #     set_vertical_title()
    #     col1, col2 = st.columns([1,3])
    #     with col1:
    #         st.title("PRICE LIST")
            
    #     with col2:
    #         facials_prices()
    #         st.title("Facials")
    #         st.markdown("## Waxing")
    #         st.write("Eyebrows: $15")
            
           
            
    # Create a canvas component
    # css-10trblm e1nzilvr0
    # css-10trblm e1nzilvr0
if __name__ == "__main__":
    main()