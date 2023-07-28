from io import BytesIO
import numpy as np
from PIL import Image
import streamlit as st

#1- ########### personal information #########################
def personal_information(data: dict, personal_info: dict, key: str) -> None:
    """
    Generates the Personal Information section of the form.
    """
    col1, col2 = st.columns([2,3])

    with col1:
        data["personal_info"]["name"] = st.text_input(
            label=personal_info["name"], 
            placeholder=personal_info["name"],
            label_visibility='hidden', 
            key=key+'_name')

        data["personal_info"]["phone"] = st.text_input(
            label=personal_info["phone"], 
            placeholder=personal_info["phone"], 
            label_visibility='hidden', 
            key=key+'_phone')
            
    with col2: 
        data["personal_info"]["email"] = st.text_input(
            label=personal_info["email"], 
            placeholder=personal_info["email"], 
            label_visibility='hidden', 
            key=key+'_email')
        
        data["personal_info"]["gender"] = st.selectbox(
            label=personal_info["gender"]["label"],
            options=personal_info["gender"]["options"] , 
            index = 1, 
            key=key+'_gender')

#2- ######################## Multiple choice #########################
def display_multiple_choice_questions(data: dict, questions: dict) -> None:
    """
    Generates multiple-choice questions for the form.
    """
    for key, question in questions.items():
        data["multiple_choice_answers"][key] = st.radio(question, options=st.session_state.app_text["spanish"]["response_options"], key=key)

#3-########################fill in questions#########################
def display_text_input_questions(data: dict, questions: dict) -> None:
    """
    Generates text input questions for the form.
    """
    for key, question in questions.items():
        text = st.text_area(question, key=key)
        lines = text.split("\n")
        data["answers"][key] = " ".join(lines)

#4-########################informed consent#########################
def display_informed_consent(data: dict, consent_text ) -> None:
    """
    Displays the Informed Consent Release section of the form.
    """
    consent_text = consent_text.format(name=data['personal_info']['name'])
    st.markdown(consent_text, unsafe_allow_html=True)
    
#5-########################signature pad#########################
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
