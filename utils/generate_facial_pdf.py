from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
from utils.pdf_helpers import gets_todays_date, session_header, textbox,chunck_text,client_signature,\
    create_personal_info,create_multichoice_questionnaire,create_fillin_questionnaire

def create_facial_pdf(data:dict, signture_img:BytesIO, app_text:dict, language:str) -> BytesIO:
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    form = c.acroForm
    c.setTitle(f"wax_release_for, {data['personal_info']['name']} {gets_todays_date()}")
    c.setFont("Times-Roman", 12)
    logo_path = "img/pdflogo.png"  # replace with your logo file
    logo_width, logo_height = 200,200 # logo.getSize()
    # calculate x and y coordinates to center the image
    x = (letter[0] - logo_width) / 2
    y = (letter[1] - logo_height - 20)

    # Centered Logo
    c.drawImage(logo_path, x, y, width=logo_width, height=logo_height)

    # # Personal Info
    create_personal_info(c, form, data["personal_info"], app_text[language]["personal_info"])
    
    # #Skin INFO
    c.line(50,380, 550, 380)
    textbox(c,form, 50, 330, 330, 24, data['skin_info']['skin_goals'], app_text[language]["skin_info"]["skin_goals"])
    textbox(c,form, 450, 330, 100, 24, data['skin_info']['skin_type'], app_text[language]["skin_info"]["skin_type"]["label"])
    
    # Multiple Choice Question
    session_header(c, 50, 300, app_text[language]["skin_history"])
    
    y = create_multichoice_questionnaire(c, form, data['multiple_choice_answers'], app_text[language]["wax_mutiplechoice_questions"], app_text[language]["response_options"],250)
    print("y_after multiplechoice", y)
    
    
    ###################### Fill-in questions ######################
    session_header(c, 50, y , app_text[language]["additional_info"])
    y = create_fillin_questionnaire(c, form, data['answers'], app_text[language]["wax_fillin_questions"], y)
    print("y_after fillin", y)
    

    ###################### Informed Consent Release ######################
    session_header(c, 50, y, app_text[language]["informed_consent"]["header"])
    consent_text = app_text[language]['informed_consent']['consent_text'].format(name=data['personal_info']['name']).replace("_", "")
    chunck_text(c, 50, y-30, f"{consent_text}")
    client_signature(c,50, y-240, signture_img)

    c.save()
    pdf_data = buffer.getvalue()
    return pdf_data
