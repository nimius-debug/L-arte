import streamlit as st
import base64
import pandas as pd
from PIL import Image
from streamlit_option_menu import option_menu

@st.cache_data
def set_vertical_title():
    vertical_l = f"""
        <style>
        h1#price-list {{
                font-size: 3rem;
                color: #647B6E;
                font-family:"sans-serif";
                text-align: center;
            }}
        @media screen and (min-width: 700px) {{
            h1#price-list {{
                font-size: 5rem;
                color: #647B6E;
                font-family:"sans-serif";
                writing-mode: vertical-lr;
                text-orientation: sideways;
            }}
        }}
        </style>
    """
    st.markdown(vertical_l, unsafe_allow_html=True)

# @st.cache_data
def facials_prices():
    # st.markdown('''
    #     <style>
    #         @media (max-width: 640px){
    #             div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-of-type(2) .css-1r6slb0 {
    #                 min-width: calc(10% - 1.5rem) !important;
    #             }
    #         }
    #     </style>''', unsafe_allow_html=True)
    
    print('facials prices')
 
    st.subheader("Facials")
    services = [
        ("Acne Facial", "$60"),
        ("Brightening Facial", "$55"),
        ("Anti Aging Facial", "$55"),
        ("Relaxing Facial", "$50"),
        ("Back Facial", "$40"),
        ("Dermaplane add-on", "$15"),
    ]

    for service, price in services:
        html_content = f'<div style="width: 300px; display: flex; justify-content: space-between;">\
                        <span>{service}</span>\
                        <span>{price}</span>\
                    </div>'
    st.markdown(html_content, unsafe_allow_html=True)
    
    st.text(f"Acne Facial {'$60':>20}")
    st.text(f"Brightening Facial {'$55':>20}")
    st.text(f"Anti Aging Facial {'$55':>20}")
    st.text(f"Relaxing Facial {'$50':>20}")
    st.text(f"Back Facial {'$40':>20}")
    st.text(f"Dermaplane add-on {'$15':>20}")
    
     
    df = pd.DataFrame(
        {
            "name": ["Acne Facial", "Brightening Facial", "Anti Aging Facial", "Relaxing Facial", "Back Facial", "Dermaplane add-on"],
            "price": ["$60", "$55", "$55", "$50", "$40", "$15"],
        }
    )   
    
    st.dataframe(
        df,
        column_config={
            "name": st.column_config.TextColumn(
                label="name",
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
    col1, col2 = st.columns([2,1])
    
    with col1:
        st.write("Acne Facial")
        st.write("Brightening Facial")
        st.write("Anti Aging Facial")
        st.write("Relaxing Facial")
        st.write("Back Facial")
        st.write("Dermaplane add-on")
        
    with col2:
        st.write("$60")
        st.write("$55")
        st.write("$55")
        st.write("$50")
        st.write("$40")
        st.write("$15")
        
     