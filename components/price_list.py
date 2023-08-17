import streamlit as st
import base64
import pandas as pd
from PIL import Image
from streamlit_option_menu import option_menu

#########################Style#########################
@st.cache_data
def style_menu_title():
    vertical_l = f"""
        <style>
        h1#menu-precios, h1#price-menu {{
                font-size: 4rem;
                color: #647B6E;
                font-family:"sans-serif";
                text-align: center;
            }}
        </style>
    """
    st.markdown(vertical_l, unsafe_allow_html=True)
    
@st.cache_data
def style_subheader():
    st.markdown("""
    <style>
        h3#waxing ,h3#facials, h3#advanced-facials, h3#lashes-brows, 
        h3#faciales, h3#faciales-avanzados, h3#pesta-as-cejas, h3#depilaci-n-con-cera  { 
            text-align: center;
        }
       
    </style>
    """, unsafe_allow_html=True)
    
@st.cache_data  
def style_opening():
    st.markdown("""
        <style>
            p.opening-text {
                color: #9F836D;
                text-align: center;
                font-size: large;
                font-weight: 600;
            }
        </style>
        <p class="opening-text"> Open 9:30 am - 5:00 pm | Tuesday | Friday | Sunday  </p>
    """, unsafe_allow_html=True)
    
######################### DISPLAY Facials #########################  
def display_facials():
    st.subheader(st.session_state.app_text[st.session_state.language]["pricing"]["facials"]["label"])
    st.markdown(st.session_state.app_text[st.session_state.language]["pricing"]["facials"]["description"])
    
    df = pd.DataFrame(
        {
            "name": list(st.session_state.app_text[st.session_state.language]["pricing"]["facials"]["name"].values()),
            "price": ["$55", "$60", "$58", "$18"],
        }
    )   
 
    st.dataframe(
        df,
        column_config={
            "name": st.column_config.TextColumn(
                label="Type of Facial",
                disabled=True,
                width="medium"
            ),
            "price": st.column_config.NumberColumn(
                label="Price",
                disabled=True,
                format="$%d",
                width="small"
            ),   
        },
        hide_index=True,
        use_container_width = True,
    )

######################### DISPLAY Avance Facials #########################
def display_advance_facials():
    st.subheader(st.session_state.app_text[st.session_state.language]["pricing"]["advanced_facials"]["label"])
    st.markdown(st.session_state.app_text[st.session_state.language]["pricing"]["advanced_facials"]["description"])
    
    df = pd.DataFrame(
        {
            "name": list(st.session_state.app_text[st.session_state.language]["pricing"]["advanced_facials"]["name"].values()),
            "price": ["$85", "$90", "$230", "$250"],
        }
    )   
 
    st.dataframe(
        df,
        column_config={
            "name": st.column_config.TextColumn(
                label="Type of Facial",
                disabled=True,
                width="medium"
            ),
            "price": st.column_config.NumberColumn(
                label="Price",
                disabled=True,
                format="$%d",
                width="small"
            ),   
        },
        hide_index=True,
        use_container_width = True,
    )
######################### DISPLAY Waxing #########################

def display_waxing():
    st.subheader(st.session_state.app_text[st.session_state.language]["pricing"]["waxing"]["label"])
    # print(st.session_state.app_text[st.session_state.language]["pricing"]["waxing"]["name"].values())
    df = pd.DataFrame(
        {
            "name": list(st.session_state.app_text[st.session_state.language]["pricing"]["waxing"]["name"].values()),
            "price" : ["$8.00","$15.00","$15.00","$20.00","$45.00","$60.00","$50.00","$23.00"],
        }
    )   
    
    st.dataframe(
        df,
        column_config={
            "name": st.column_config.TextColumn(
                label="Hair Removal",
                disabled=True,
                width="medium"
            ),
            "price": st.column_config.NumberColumn(
                label="Price",
                disabled=True,
                format="$%d",
                width="small"
            ),   
        },
        hide_index=True,
        use_container_width = True,
    )
    
######################### DISPLAY Lashes & Brows #########################
def display_LashesBrows():
    st.subheader(st.session_state.app_text[st.session_state.language]["pricing"]["lashes_brows"]["label"])
    df = pd.DataFrame(
        {
            "name": list(st.session_state.app_text[st.session_state.language]["pricing"]["lashes_brows"]["name"].values()),
            "price" : ["$45.00","$55.00","$40.00","$48.00","$60.00"],
        }
    )   
    
    st.dataframe(
        df,
        column_config={
            "name": st.column_config.TextColumn(
                label="Lashe & Brows",
                disabled=True,
                width="medium"
            ),
            "price": st.column_config.NumberColumn(
                label="Price",
                disabled=True,
                format="$%d",
                width="small"
            ),   
        },
        hide_index=True,
        use_container_width = True,
    )

######################### PRICE PAGE #########################

def Price_page():
    
    style_opening()
    style_subheader()
    style_menu_title()
    
    st.title(st.session_state.app_text[st.session_state.language]["pricing"]["menu"])
    st.markdown("---")
    col1, col2 = st.columns([1,1],gap="large")
    with col1:
        display_facials()
        display_advance_facials()
       
    with col2:
        display_waxing()
        display_LashesBrows()
    
    
    