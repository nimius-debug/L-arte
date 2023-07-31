from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.lib.colors import black
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.utils import ImageReader
import textwrap
from io import BytesIO
from reportlab.graphics.shapes import Path

def gets_todays_date():
    import datetime
    today = datetime.date.today()
    return today.strftime("%B %d, %Y")

def session_header(c: Canvas, x: int, y: int, data: str) -> None:
    c.setFont("Times-Roman", 14)
    # c.setFont("Helvetica", 16)
    c.drawString(x, y, data)
    c.setLineWidth(1)
    c.line(50, y-5, 550, y-5)

def textbox(c: Canvas, form: Canvas.acroForm, x: int, y: int, width: int, height: int, data: str, name: str) -> None:
    # c.setFont("Helvetica", 12)
    c.setFont("Times-Roman", 12)
    c.drawString(x, y+30, f"{name} :")
    form.textfield(name=name,  x=x, y=y, width=width, height=height,
                   value=data, textColor=black, fillColor=HexColor("#EDEDED"), 
                   fieldFlags='readOnly', fontName="Times-Roman")

def create_radio_group(c: Canvas, form:Canvas.acroForm, group_name: str, question: str, data: str, x: int, y: int, options: list) -> None:
    """
    Function to create a 2 radio button group in a PDF.
    """
    # draw the question
    c.setFont("Times-Roman", 12)
    chunck_text(c, x, y, question)
    # c.drawString(x, y, question)

    # draw the 'No' radio button
    form.radio(name=group_name, value=options[0], selected=(data == options[0]), x=x, y=y-20, buttonStyle='circle',
        shape='circle',size=15, fieldFlags='readOnly')

    # draw the 'Yes' radio button
    form.radio(name=group_name,value=options[1], selected=(data == options[1]),x=x+50, y=y-20, buttonStyle='circle',
        shape='circle',size=15, fieldFlags='readOnly')

    # draw the 'No' and 'Yes' labels
    c.drawString(x+20, y-20, options[0])
    c.drawString(x+70, y-20, options[1])
    
def text_area(c: Canvas, form:Canvas.acroForm, x: int, y: int, width: int, height: int, data: str, name: str, question: str) -> None:
    """
    Function to create a text area in a PDF.
    """
    # draw the question
    c.setFont("Times-Roman", 12)
    if check_overflown(question):
        lines = textwrap.wrap(question, width=100)  # adjust width as necessary
        for i, line in enumerate(lines):
            c.drawString(x, y+80 -(i*14), line)  # adjust 14 (line height) as necessary
        form.textfield(name=name, x=x, y=y, width=width, height=height, 
                value=data, textColor=black, fillColor=HexColor("#EDEDED"), 
                fieldFlags='readOnly', fontName="Times-Roman")
    else:
        c.drawString(x, y+80, question)
        # draw the text area
        form.textfield(name=name, x=x, y=y+15, width=width, height=height, 
                value=data, textColor=black, fillColor=HexColor("#EDEDED"), 
                fieldFlags='readOnly', fontName="Times-Roman")

def check_overflown(check_text: str) -> bool:
    str_width = stringWidth(check_text, "Times-Roman", 12)
    if str_width > 500:
        return True
    else:
        return False 
     
def chunck_text(c: Canvas,x: int,y:int, data_str: str) -> None:
    c.setFont("Times-Roman", 12)
    # check if the question string is longer than 550
    if check_overflown(data_str):
        # split the question into multiple lines
        lines = textwrap.wrap(data_str, width=100)  # adjust width as necessary
        for i, line in enumerate(lines):
            c.drawString(x, y - i*14, line)  # adjust 14 (line height) as necessary
    else:
        c.drawString(x, y, data_str)

def client_signature(c: Canvas, x: int, y:int, data_bytes:BytesIO ) -> None:
    # c.setFont("Helvetica", 12)
    c.drawString(x, y, "Client Signature")
    c.line(x+90, y, x+250, y)
    # Now, you can add this "file-like" object to your PDF using reportlab
    c.drawImage(ImageReader(data_bytes), x+130, y= y-10 , width=60, height=60, mask='auto')
    c.drawString(x+350, y, "Date")
    c.line(x+380, y, x+500, y)
    c.drawString(x+400, y+5, gets_todays_date())
    

def create_pdf(data:dict, signture_img:BytesIO, app_text:dict, language:str) -> BytesIO:
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

    # Personal Info
    session_header(c, 50, 610, app_text[language]["personal_info"]["header"])
       
    # textbox(c,form, 50, 550, 200, 24, data['personal_info'][key], app_text[language]["personal_info"][key])
    textbox(c,form, 50, 550, 200, 24, data['personal_info']['name'], app_text[language]["personal_info"]["name"])
    textbox(c,form, 350, 550, 200, 24, data['personal_info']['phone'], app_text[language]["personal_info"]["phone"])
    textbox(c,form, 50, 500, 250, 24, data['personal_info']['email'], app_text[language]["personal_info"]["email"])
    textbox(c,form, 350, 500, 100, 24, data['personal_info']['gender'], app_text[language]["personal_info"]["gender"]["label"])
    
    # Multiple Choice Question
    session_header(c, 50, 450, app_text[language]["skin_history"])
    y = 430
    for key in app_text[language]["wax_mutiplechoice_questions"].keys():
        if y < 100:
            c.showPage()
            y = 650
      
        create_radio_group(c,form, key, app_text[language]["wax_mutiplechoice_questions"][key], 
                           data['multiple_choice_answers'][key], 50, y, app_text[language]["response_options"])
        y -= 40
  
    ###################### Additional Information ######################
    session_header(c, 50, 170 , app_text[language]["additional_info"])
    # text_area(c, form, 50, 70, 500, 60, data['answers']['medication'], 'medication', 'Are you currently taking medications? If so, please list all (including over the counter drugs/herbal supplements):')
    y = 70
    for key in app_text[language]["wax_fillin_questions"].keys():
        if y < 50:
            c.showPage()
            y = 650
        text_area(c,form, 50, y , 500, 60, data['answers'][key], key, app_text[language]["wax_fillin_questions"][key])    
        y -= 100

    ###################### Informed Consent Release ######################
    if y < 250:
        c.showPage()
        y = 650
    session_header(c, 50, y+70, app_text[language]["informed_consent"]["header"])
    consent_text = app_text[language]['informed_consent']['consent_text'].format(name=data['personal_info']['name']).replace("_", "")
    chunck_text(c, 50, y+50, f"{consent_text}")
    client_signature(c,50, y-200, signture_img)

    c.save()
    pdf_data = buffer.getvalue()
    return pdf_data
