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
        text = st.text_area(question, key=key)
        lines = text.split("\n")
        data["answers"][key] = " ".join(lines)

#4-########################informed consent#########################
def display_informed_consent(data: dict) -> None:
    """
    Displays the Informed Consent Release section of the form.
    """
    st.subheader("Informed Consent Release")
    consent_text = f"""I ________{data['personal_info']['name']}________ , do fully understand all the questions above and have answered them
            all correctly and honestly. I understand that the services offered are not a substitute for medical care. I
            understand that the skin care professional will completely inform me of what to expect in the course of
            treatment and will recommend adjustments to my regimen if deemed necessary. I also am aware that
            individual results are dependent upon my age, skin condition, and lifestyle. I agree to actively participate
            in following appointment schedules and home care procedures to the best of my ability, so that I may
            obtain maximum effectiveness. In the event that I may have additional questions or concerns regarding
            my treatment or suggested home product routine, I will inform my skin care professional immediately.
            I release and hold harmless the skin care professional Laura Lopez, SKIN by Laura Lo, and the
            staff harmless from any liability for adverse reactions that may result from this treatment."""
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
