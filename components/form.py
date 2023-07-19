import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas

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
    # st.markdown("""
    # <style>
    # [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
    #     gap: 0rem;
    # }
    # </style>
    # """,unsafe_allow_html=True)
    with st.form(key='Skincare Form'):
        col1, col2 = st.columns([2,3])
        with col1:
            name = st.text_input("Name", placeholder= "Name",label_visibility='hidden')
            home_phone = st.text_input("Phone",placeholder="Phone",label_visibility='hidden')
        with col2: 
            email = st.text_input("Email adress", placeholder="Email address",label_visibility='hidden')
        st.markdown("""---""")
        # address = st.text_input("Address")
        # city = st.text_input("City")
        # state = st.text_input("State")
        # zip_code = st.text_input("Zip")
        # home_phone = st.text_input("Phone")
        # work_phone = st.text_input("Work Phone")
        
        st.title("Skin History")
        aha_usage = st.radio("Have you used any Alpha Hydroxy Acid (AHA) or glycolic products in the past 48-72 hours?", ('No', 'Yes'))
        retin_a_usage = st.radio("Are you using Retin-a, Renova or Accutane (an oral form of Retin-a)?", ('No', 'Yes'))
        skin_thinning_products_usage = st.radio("Are you using any other skin thinning products and/or drugs?", ('No', 'Yes'))
        sun_exposure = st.radio("Are you exposed to the sun on a daily basis or are you considering spending more time in the sun soon?", ('No', 'Yes'))
        tanning_bed_usage = st.radio("Do you use a tanning bed?", ('No', 'Yes'))
        is_diabetic = st.radio("Are you diabetic?", ('No', 'Yes'))
        
        
        st.markdown("""---""")
        medication = st.text_area("Are you currently taking medications? If so, please list all (including over the counter drugs/herbal supplements):")
        skin_products = st.text_area("What skin products do you regularly use on your skin?")
        cancer_history = st.text_area("Have you ever been treated for cancer? If yes, when and what types of therapies were used?")
        other_conditions = st.text_area("Please list any other illness/condition you are currently being treated for by a medical professional")
        menstrual_cycle = st.text_input("(Female clients) When is your next menstrual cycle due to begin?")
        st.markdown("""---""")
        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
            stroke_width=2,
            height=150,
            key="canvas",
        )
        print(canvas_result.image_data)
        #submit button
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Form submitted successfully.")