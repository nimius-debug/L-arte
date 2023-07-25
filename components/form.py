import base64
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
from pdf import create_pdf
from io import BytesIO
import numpy as np
import webbrowser
#########################signature pad#########################
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

#########################image to base64 background #########################
@st.cache_data
def get_img_as_base64(file_pic):
    with open(file_pic, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

@st.cache_data
def backgound_img():
    img = get_img_as_base64("img/Home.png")
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
def logo():
    col1, col2, col3 = st.columns([1,2,1])

    with col1:
        st.write(' ')

    with col2:
        logo = Image.open('img/logo.png')
        st.image(logo, use_column_width= "auto")

    with col3:
        st.write(' ')
        
#########################form#########################
def form():
    
    data = {
        "personal_info": {},
        "multiple_choice_answers": {},
        "answers": {},
    }
    #############Personal Information##################
    st.subheader("Personal Information")
    col1, col2 = st.columns([2,3])
    with col1:
        data["personal_info"]["name"] = st.text_input("Name", placeholder= "Name",label_visibility='hidden')
        data["personal_info"]["phone"] = st.text_input("Phone",placeholder="Phone",label_visibility='hidden')
            
    with col2: 
        data["personal_info"]["email"] = st.text_input("Email adress", placeholder="Email address",label_visibility='hidden')
        data["personal_info"]["gender"] = st.selectbox( 'Gender', ('Male', 'Female', 'Other') , index = 1)
        
    with st.form(key='Skincare Form'):
       
        ######################multiple-choice questions ######################
        st.subheader("Skin History")
        data["multiple_choice_answers"]["aha_usage"] = st.radio("Have you used any Alpha Hydroxy Acid (AHA) or glycolic products in the past 48-72 hours?", ('No', 'Yes'))
        data["multiple_choice_answers"]["retin_a_usage"] = st.radio("Are you using Retin-a, Renova or Accutane (an oral form of Retin-a)?", ('No', 'Yes'))
        data["multiple_choice_answers"]["skin_thinning_products_usage"] = st.radio("Are you using any other skin thinning products and/or drugs?", ('No', 'Yes'))
        data["multiple_choice_answers"]["sun_exposure"] = st.radio("Are you exposed to the sun on a daily basis or are you considering spending more time in the sun soon?", ('No', 'Yes'))
        data["multiple_choice_answers"]["tanning_bed_usage"] = st.radio("Do you use a tanning bed?", ('No', 'Yes'))
        data["multiple_choice_answers"]["is_diabetic"] = st.radio("Are you diabetic?", ('No', 'Yes'))

        ######################answer questions ######################
        st.markdown("""---""")
        data["answers"]["medication"] = st.text_input("Are you currently taking medications? If so, please list all (including over the counter drugs/herbal supplements):")
        data["answers"]["skin_products"] = st.text_input("What skin products do you regularly use on your skin?")
        data["answers"]["cancer_history"] = st.text_input("Have you ever been treated for cancer? If yes, when and what types of therapies were used?")
        data["answers"]["other_conditions"] = st.text_input("Please list any other illness/condition you are currently being treated for by a medical professional")
        data["answers"]["menstrual_cycle"] = st.text_input("(Female clients) When is your next menstrual cycle due to begin?")
        st.markdown("""---""")

        
        ######################informed consent ######################
        st.subheader("Informed Consent Release")
        st.markdown(f"I ________{data['personal_info']['name']}________ , do fully understand all the questions above and have answered them\
            all correctly and honestly. I understand that the services offered are not a substitute for medical care. I\
            understand that the skin care professional will completely inform me of what to expect in the course of\
            treatment and will recommend adjustments to my regimen if deemed necessary. I also am aware that\
            individual results are dependent upon my age, skin condition, and lifestyle. I agree to actively participate\
            in following appointment schedules and home care procedures to the best of my ability, so that I may\
            obtain maximum effectiveness. In the event that I may have additional questions or concerns regarding\
            my treatment or suggested home product routine, I will inform my skin care professional immediately.\
            I release and hold harmless the skin care professional Laura Lopez, SKIN by Laura Lo, and the\
            staff harmless from any liability for adverse reactions that may result from this treatment.",
            unsafe_allow_html=True)
        st.caption("Please sign the form")
        canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
        stroke_width=2,
        height=150,
        width=250,
        key="canvas",
        )
        
        if canvas_result.image_data is not None:
             if canvas_result.json_data["objects"]:
                data["signature_img"] = signature_pad(canvas_result=canvas_result)
        
        #submit button
        submitted = st.form_submit_button("Submit")
        if submitted:
            if not canvas_result.json_data["objects"]:
                st.warning("Please sign the form")
            elif not data["personal_info"]["name"]:
                st.warning("Please enter your name")
            elif not data["personal_info"]["email"]:
                st.warning("Please enter your email address")
            elif not data["personal_info"]["phone"]:
                st.warning("Please enter your phone number")
            else:
                st.success("Form submitted successfully.")
                st.write(data)
                create_pdf(data)
                webbrowser.open("https://giphy.com/gifs/usanetwork-wwe-wweraw-wwelive-ngkM4UbZBTZWKrj0wI/fullscreen")
                #switch_page("Service")
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