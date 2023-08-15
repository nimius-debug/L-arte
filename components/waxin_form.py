
import streamlit as st
# from streamlit_extras.switch_page_button import switch_page
from utils.generate_wax_pdf import create_wax_pdf
from components.form_components import signature_pad, display_multiple_choice_questions, contact_information,\
    display_text_input_questions, display_informed_consent,display_skin_info,display_personal_information , create_canvas
# import webbrowser
from utils.deta_db import DetaManager

#########################form#########################
def display_waxing_form():
    deta_manager = DetaManager(st.secrets["deta_key"], st.secrets["wax_base"], st.secrets["wax_drive"])
    
    from data.map_data import data
    # from data.map_data import wax_mutiplechoice_questions, wax_fillin_questions
    
    submission_flag = False
    ######################Personal Information##############################
    st.subheader(st.session_state.app_text[st.session_state.language]["personal_info"]["header"])
    contact_information(data , st.session_state.app_text[st.session_state.language]["personal_info"], key="waxing")
    
    with st.form(key='Skincare Form'):
        display_personal_information(data , st.session_state.app_text[st.session_state.language]["personal_info"], key="waxing")
        st.markdown("""---""")
        display_skin_info(data , st.session_state.app_text[st.session_state.language]["skin_info"], key="waxing")
        
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
        waxing_user_signature = create_canvas("canvas",150,250)
    
        if waxing_user_signature.image_data is not None:
             if waxing_user_signature.json_data["objects"]:
                signature_img = signature_pad(canvas_result=waxing_user_signature)
        
        #submit button
        submitted = st.form_submit_button(st.session_state.app_text[st.session_state.language]["form"]["submit"])
        if submitted:
            
            if not waxing_user_signature.json_data["objects"]:
                st.error(st.session_state.app_text[st.session_state.language]["form"]["missing_signature"])
            elif not data["personal_info"]["name"]:
                st.error(st.session_state.app_text[st.session_state.language]["form"]["missing_name"])
            elif not data["personal_info"]["email"]:
                st.error(st.session_state.app_text[st.session_state.language]["form"]["missing_email"])
            elif not data["personal_info"]["phone"]:
                st.error(st.session_state.app_text[st.session_state.language]["form"]["missing_phone"])
            else:
                with st.spinner(text="Generating PDF..."):
                    # st.write(data)
                    wax_pdf = create_wax_pdf(data, signature_img, st.session_state.app_text, st.session_state.language)
                    deta_manager.put_base(data)
                    deta_manager.put_drive(f"{data['personal_info']['name']}_waxing_form.pdf",wax_pdf)
                st.success("Form submitted successfully.")
                st.balloons()
                submission_flag = True
                filename = f"{data['personal_info']['name']}_waxing_form.pdf"
                data["personal_info"].clear()
                data["skin_info"].clear()
                data["multiple_choice_answers"].clear()
                data["answers"].clear()
                
    if submission_flag:
        st.download_button(
        "⬇️ Download PDF",
            data=wax_pdf,
            file_name=filename,
            mime="application/pdf",
        )
        st.toast("downloaded successfully.")
        
                # webbrowser.open("https://giphy.com/gifs/usanetwork-wwe-wweraw-wwelive-ngkM4UbZBTZWKrj0wI/fullscreen")
                #switch_page("Service")
