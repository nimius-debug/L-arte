import streamlit as st
import base64
from PIL import Image
from streamlit_option_menu import option_menu
#########################sidebar#########################
def sidebar():
    with st.sidebar:
        st.title("Sidebar")
        
#########################horizontal bar#########################
def horizontal_menu():
    selected_option = option_menu(
        None, ["Home", "Price",  "Forms"], 
        icons=['house-heart', 'wallet', "files"], 
        menu_icon="cast", default_index=0, orientation="horizontal",
        styles={
            "container": {
                "font-family": "Times New Roman, Times, serif",
                "font-color": "#383b3a",
                "padding": "0!important", 
                "background-color": "#EDEDED"
                },
            "icon": {
                "color": "black", 
                "font-size": "24px"
                }, 
            "nav-link": {
                "font-size": "20px", 
                "text-align": "left", 
                "margin":"0px", 
                "--hover-color": "#FFFFFF"
                },
            "nav-link-selected": {"background-color": "#647B6E"},
        }
    )
    return selected_option
    
      
#########################BACKGROUND  #########################
#########################image to base64 background #########################
@st.cache_data
def get_img_as_base64(file_pic):
    with open(file_pic, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

@st.cache_data
def set_backgound_img():
    img = get_img_as_base64("img/background.png")
    print('background image')
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    [data-testid="stSidebar"] > div:first-child {{
        background-color: #EDEDED;");
        background-position: center; 
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}

    [data-testid="stToolbar"] {{
    right: 2rem;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
#########################logo#########################
@st.cache_data
def hide_footer_streamlit():
    hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#########################logo#########################
def display_logo():
    """
    Displays the logo in the streamlit app.
    """
    col1, col2, col3 = st.columns([1,2,1])

    with col1:
        st.write(' ')

    with col2:
        logo = Image.open('img/logo.png')
        st.image(logo, use_column_width= "auto")

    with col3:
        st.write(' ')