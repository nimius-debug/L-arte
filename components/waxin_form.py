
import streamlit as st
from streamlit_drawable_canvas import st_canvas
# from streamlit_extras.switch_page_button import switch_page
from utils.generate_pdf import create_pdf
from components.form_components import signature_pad, display_multiple_choice_questions, personal_information, display_text_input_questions, display_informed_consent
import webbrowser
from utils.deta_db import DetaManager

#########################form#########################
def display_waxing_form():
    deta_manager = DetaManager(st.secrets["deta_key"], st.secrets["base_name"], st.secrets["drive_name"])
    
    from data.map_data import data
    # from data.map_data import wax_mutiplechoice_questions, wax_fillin_questions
    
    #############Personal Information##################
    st.subheader(st.session_state.app_text[st.session_state.language]["personal_info"]["header"])
    personal_information(data , st.session_state.app_text[st.session_state.language]["personal_info"], key="waxing")
    
    with st.form(key='Skincare Form'):
        
        # ######################multiple-choice questions ######################
        st.subheader(st.session_state.app_text[st.session_state.language]["skin_history"])
        display_multiple_choice_questions(data, st.session_state.app_text[st.session_state.language]["wax_mutiplechoice_questions"])
        
        ######################answer questions ######################
        st.markdown("""---""")
        display_text_input_questions(data, st.session_state.app_text[st.session_state.language]["wax_fillin_questions"])
        
        ######################informed consent ######################
        st.markdown("""---""")
        st.subheader(st.session_state.app_text[st.session_state.language]["informed_consent"]["header"])
        display_informed_consent(data, st.session_state.app_text[st.session_state.language]["informed_consent"]["consent_text"])
        
        st.caption(st.session_state.app_text[st.session_state.language]["form"]["sign_form"])
        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
            stroke_width=2,
            height=150,
            width=250,
            key="canvas",
        )
    
        if canvas_result.image_data is not None:
             if canvas_result.json_data["objects"]:
                signature_img = signature_pad(canvas_result=canvas_result)
        
        #submit button
        submitted = st.form_submit_button(st.session_state.app_text[st.session_state.language]["form"]["submit"])
        if submitted:
            if not canvas_result.json_data["objects"]:
                st.error(st.session_state.app_text[st.session_state.language]["form"]["missing_signature"])
            elif not data["personal_info"]["name"]:
                st.error(st.session_state.app_text[st.session_state.language]["form"]["missing_name"])
            elif not data["personal_info"]["email"]:
                st.error(st.session_state.app_text[st.session_state.language]["form"]["missing_email"])
            elif not data["personal_info"]["phone"]:
                st.error(st.session_state.app_text[st.session_state.language]["form"]["missing_phone"])
            else:
                with st.spinner(text="Generating PDF..."):
                    pdf = create_pdf(data, signature_img, st.session_state.app_text, st.session_state.language)
                    deta_manager.put_base(data)
                    deta_manager.put_drive(f"{data['personal_info']['name']}.pdf",pdf)
                st.success("Form submitted successfully.")
                # st.toast("added to database successfully.")
                st.balloons()
                # webbrowser.open("https://giphy.com/gifs/usanetwork-wwe-wweraw-wwelive-ngkM4UbZBTZWKrj0wI/fullscreen")
                #switch_page("Service")
