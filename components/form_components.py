from io import BytesIO
import numpy as np
from PIL import Image
import streamlit as st

#1- ########### personal information #########################
def personal_information(data: dict, key: str) -> None:
    """
    Generates the Personal Information section of the form.
    """
    st.subheader("Personal Information")
    col1, col2 = st.columns([2,3])

    with col1:
        data["personal_info"]["name"] = st.text_input("Name", placeholder="Name", label_visibility='hidden', key=key+'_name')
        data["personal_info"]["phone"] = st.text_input("Phone", placeholder="Phone", label_visibility='hidden', key=key+'_phone')
            
    with col2: 
        data["personal_info"]["email"] = st.text_input("Email address", placeholder="Email address", label_visibility='hidden', key=key+'_email')
        data["personal_info"]["gender"] = st.selectbox('Gender', ('Male', 'Female', 'Other') , index = 1, key=key+'_gender')

#2- ######################## Multiple choice #########################
def display_multiple_choice_questions(data: dict, questions: dict) -> None:
    """
    Generates multiple-choice questions for the form.
    """
    st.subheader("Skin History")
    for key, question in questions.items():
        data["multiple_choice_answers"][key] = st.radio(question, ('No', 'Yes'))

#3-########################fill in questions#########################
def display_text_input_questions(data: dict, questions: dict) -> None:
    """
    Generates text input questions for the form.
    """
    for key, question in questions.items():
        data["answers"][key] = st.text_input(question, key=key)

#########################signature pad#########################
@st.cache_data
def signature_pad(canvas_result)-> BytesIO:
    # Convert the numpy array to PIL image
    image_data = canvas_result.image_data
    image = Image.fromarray(np.uint8(image_data))

    # Convert the PIL image to a bytes object
    image_byte_arr = BytesIO()
    image.save(image_byte_arr, format='PNG')
    image_byte_arr = image_byte_arr.getvalue()

    # Create a BytesIO object
    image_io = BytesIO(image_byte_arr)
    
    return image_io
