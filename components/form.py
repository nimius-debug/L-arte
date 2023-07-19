import streamlit as st
from PIL import Image

def logo():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:
        logo = Image.open('img/logo2.png')
        st.image(logo, use_column_width= "auto")

    with col3:
        st.write(' ')
        
    
def form():

    name = st.text_input("Name")
    address = st.text_input("Address")
    city = st.text_input("City")
    state = st.text_input("State")
    zip_code = st.text_input("Zip")
    home_phone = st.text_input("Home Phone")
    work_phone = st.text_input("Work Phone")
    email = st.text_input("Email address")

    aha_usage = st.radio("Have you used any Alpha Hydroxy Acid (AHA) or glycolic products in the past 48-72 hours?", ('No', 'Yes'))
    retin_a_usage = st.radio("Are you using Retin-a, Renova or Accutane (an oral form of Retin-a)?", ('No', 'Yes'))
    skin_thinning_products_usage = st.radio("Are you using any other skin thinning products and/or drugs?", ('No', 'Yes'))
    sun_exposure = st.radio("Are you exposed to the sun on a daily basis or are you considering spending more time in the sun soon?", ('No', 'Yes'))
    tanning_bed_usage = st.radio("Do you use a tanning bed?", ('No', 'Yes'))
    is_diabetic = st.radio("Are you diabetic?", ('No', 'Yes'))
    medication = st.text_area("Are you currently taking medications? If so, please list all (including over the counter drugs/herbal supplements):")
    skin_products = st.text_area("What skin products do you regularly use on your skin?")
    cancer_history = st.text_area("Have you ever been treated for cancer? If yes, when and what types of therapies were used?")
    other_conditions = st.text_area("Please list any other illness/condition you are currently being treated for by a medical professional")
    menstrual_cycle = st.text_input("(Female clients) When is your next menstrual cycle due to begin?")
    
    if st.button("Submit"):
        st.write("Form submitted successfully.")