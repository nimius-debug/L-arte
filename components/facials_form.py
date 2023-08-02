
import streamlit as st

# from streamlit_extras.switch_page_button import switch_page
from utils.generate_pdf import create_pdf
from components.form_components import signature_pad, display_multiple_choice_questions, contact_information,\
    display_text_input_questions, display_informed_consent,display_skin_info,display_personal_information, create_canvas
import webbrowser
from utils.deta_db import DetaManager

#########################form#########################
def display_facial_form():
    deta_manager = DetaManager(st.secrets["deta_key"], st.secrets["facials_base"], st.secrets["facials_drive"])
    
    from data.map_data import data
    # from data.map_data import wax_mutiplechoice_questions, wax_fillin_questions
    
    ######################Personal Information##############################
    st.subheader(st.session_state.app_text[st.session_state.language]["personal_info"]["header"])
    contact_information(data , st.session_state.app_text[st.session_state.language]["personal_info"], key="facials")
    
    with st.form(key='Skincare Form facial'):
        display_personal_information(data , st.session_state.app_text[st.session_state.language]["personal_info"], key="facials")
        st.markdown("""---""")
        display_skin_info(data , st.session_state.app_text[st.session_state.language]["skin_info"], key="facials")
        display_multiple_choice_questions(data, st.session_state.app_text[st.session_state.language]["outdoor_activities"])
        # ######################multiple-choice questions ######################
        st.subheader(st.session_state.app_text[st.session_state.language]["skin_history"])
        display_multiple_choice_questions(data, st.session_state.app_text[st.session_state.language]["facials_multiplechoice_questions"],2)
        
        ######################answer questions ######################
        st.markdown("""---""")
        display_text_input_questions(data, st.session_state.app_text[st.session_state.language]["facials_fillin_questions"])
        
        ######################informed consent ######################
        st.markdown("""---""")
        st.subheader(st.session_state.app_text[st.session_state.language]["informed_consent"]["header"])
        display_informed_consent(data, st.session_state.app_text[st.session_state.language]["informed_consent"]["consent_text"])
        st.caption(st.session_state.app_text[st.session_state.language]["form"]["sign_form"])
        
        facial_user_signature = create_canvas("facial")
    
        if facial_user_signature.image_data is not None:
             if facial_user_signature.json_data["objects"]:
                signature_img = signature_pad(canvas_result=facial_user_signature)
        
        #submit button
        submitted = st.form_submit_button(st.session_state.app_text[st.session_state.language]["form"]["submit"])
        if submitted:
            if not facial_user_signature.json_data["objects"]:
                st.error(st.session_state.app_text[st.session_state.language]["form"]["missing_signature"])
            elif not data["personal_info"]["name"]:
                st.error(st.session_state.app_text[st.session_state.language]["form"]["missing_name"])
            elif not data["personal_info"]["email"]:
                st.error(st.session_state.app_text[st.session_state.language]["form"]["missing_email"])
            elif not data["personal_info"]["phone"]:
                st.error(st.session_state.app_text[st.session_state.language]["form"]["missing_phone"])
            else:
                with st.spinner(text="Generating PDF..."):
                    st.write(data)
                    create_pdf(data, signature_img, st.session_state.app_text, st.session_state.language)
                    # deta_manager.put_base(data)
                    # deta_manager.put_drive(f"{data['personal_info']['name']}_waxing_form.pdf",pdf)
                st.success("Form submitted successfully.")
                # st.toast("added to database successfully.")
                st.balloons()
                # webbrowser.open("https://giphy.com/gifs/usanetwork-wwe-wweraw-wwelive-ngkM4UbZBTZWKrj0wI/fullscreen")
                #switch_page("Service")