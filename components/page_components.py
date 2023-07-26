import streamlit as st
import base64
from PIL import Image

#########################sidebar#########################
def sidebar():
    page_bg_img = f"""
        <style>
        [data-testid="stSidebar"] > div:first-child {{
        background-color: #EDEDED;");
        background-position: center; 
        background-repeat: no-repeat;
        background-attachment: fixed;
        }}
        </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
    with st.sidebar:
        st.title("Sidebar")
        
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