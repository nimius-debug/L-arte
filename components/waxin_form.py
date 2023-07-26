
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from streamlit_extras.switch_page_button import switch_page
from utils.generate_pdf import create_pdf
from components.form_components import signature_pad, display_multiple_choice_questions,\
    personal_information, display_text_input_questions
import webbrowser

#########################form#########################
def display_waxing_form():
    from utils.map_data import data
    from utils.map_data import wax_mutiplechoice_questions, wax_fillin_questions
    #############Personal Information##################
    personal_information(data, key="waxing")
    with st.form(key='Skincare Form'):
       
        # ######################multiple-choice questions ######################
        display_multiple_choice_questions(data, wax_mutiplechoice_questions)
        ######################answer questions ######################
        st.markdown("""---""")
        display_text_input_questions(data, wax_fillin_questions)

        # data["answers"]["medication"] = st.text_input("Are you currently taking medications? If so, please list all (including over the counter drugs/herbal supplements):")
        # data["answers"]["skin_products"] = st.text_input("What skin products do you regularly use on your skin?")
        # data["answers"]["cancer_history"] = st.text_input("Have you ever been treated for cancer? If yes, when and what types of therapies were used?")
        # data["answers"]["other_conditions"] = st.text_input("Please list any other illness/condition you are currently being treated for by a medical professional")
        # data["answers"]["menstrual_cycle"] = st.text_input("(Female clients) When is your next menstrual cycle due to begin?")
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
                # webbrowser.open("https://giphy.com/gifs/usanetwork-wwe-wweraw-wwelive-ngkM4UbZBTZWKrj0wI/fullscreen")
                #switch_page("Service")
