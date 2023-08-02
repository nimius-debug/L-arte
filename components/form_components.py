from streamlit_drawable_canvas import st_canvas
from io import BytesIO
import numpy as np
from PIL import Image
import streamlit as st
import re

@st.cache_data
def validate_email(email: str) -> bool:
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.match(email_regex, email) is not None

#1- ########### personal information #########################
def contact_information(data: dict, personal_info: dict, key: str) -> None:
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
            
    with col2: 
        data["personal_info"]["email"] = st.text_input(
            label=personal_info["email"], 
            placeholder=personal_info["email"], 
            label_visibility='hidden', 
            key=key+'_email')
        
        if not validate_email(data["personal_info"]["email"]) and data["personal_info"]["email"] :
            st.error("Please enter a valid email address.")
        
def display_personal_information(data: dict, personal_info: dict, key: str) -> None:
    col1, col2 = st.columns([2,3])

    with col1:
        data["personal_info"]["phone"] = st.text_input(
            label=personal_info["phone"], 
            placeholder=personal_info["phone"], 
            label_visibility='hidden', 
            key=key+'_phone')
            
    with col2:  
        data["personal_info"]["gender"] = st.selectbox(
            label=personal_info["gender"]["label"],
            options=personal_info["gender"]["options"] , 
            index = 1, 
            key=key+'_gender')
        
    data["personal_info"]["address"] = st.text_input(
        label=personal_info["address"], 
        placeholder=personal_info["address"], 
        key=key+'_address')
    
    col11, col22 = st.columns([3,2])
    with col11:
        data["personal_info"]["emergency_contact_name"] = st.text_input(
            label=personal_info["emergency_contact_label"], 
            placeholder=personal_info["emergency_contact_name"], 
            key=key+'_contact_name')
        
    with col22:
        data["personal_info"]["emergency_contact_phone"] = st.text_input(
            label=personal_info["emergency_contact_label"], 
            placeholder=personal_info["emergency_contact_phone"], 
            label_visibility='hidden', 
            key=key+'_contact_phone')
        
def display_skin_info(data: dict, personal_info: dict, key: str) -> None:
    col1, col2 = st.columns([3,2])
    with col1:
        data["skin_info"]["skin_goals"] = st.text_input(
            label=personal_info["skin_goals"], 
            key=key+'_skin_goals')
        
    with col2:
        data["skin_info"]["skin_type"] = st.selectbox(
            label=personal_info["skin_type"]["label"], 
            options=personal_info["skin_type"]["options"], 
            index=1, 
            key=key+'_skin_type')
    
#2- ######################## Multiple choice #########################
def display_multiple_choice_questions(data: dict, questions: dict, num_cols: int = 1) -> None:
    """
    Generates multiple-choice questions for the form.
    """
     # Create columns
    cols = st.columns(num_cols)
    # Distribute questions across columns
    for i, (key, question) in enumerate(questions.items()):
        col_index = i % num_cols  # calculate column index

        with cols[col_index]:
            data["multiple_choice_answers"][key] = st.radio(
                question, 
                options=st.session_state.app_text[st.session_state.language]["response_options"], 
                key=key
            )

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
def create_canvas(key: str, h: int = 200, w: int = 400):
    print("create canvas")
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
        stroke_width=2,
        height=h,
        width=w,
        key=key,
        update_streamlit = True
    )
    print(key)
    return canvas_result

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
