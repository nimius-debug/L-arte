from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.colors import black
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.utils import ImageReader
from io import BytesIO
import textwrap

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
    
def create_personal_info(c: Canvas, form:Canvas.acroForm, personal_info:dict, app_text_personal_info:dict):
    # Personal Info
    session_header(c, 50, 610, app_text_personal_info["header"])
    textbox(c,form, 50, 550, 250, 24, personal_info['name'], app_text_personal_info["name"])
    textbox(c,form, 450, 550, 100, 24,personal_info['phone'], app_text_personal_info["phone"])
    textbox(c,form, 50, 500, 280, 24, personal_info['email'], app_text_personal_info["email"])
    textbox(c,form, 450, 500, 100, 24,personal_info['gender'], app_text_personal_info["gender"]["label"])
    textbox(c,form, 50, 450, 500, 24, personal_info['address'], app_text_personal_info["address"])
    textbox(c,form, 50, 400, 250, 24, personal_info['emergency_contact_name'], app_text_personal_info["emergency_contact_name"])
    textbox(c,form, 450, 400, 100, 24,personal_info['emergency_contact_phone'], app_text_personal_info["emergency_contact_phone"])

def create_multichoice_questionnaire(c: Canvas, form:Canvas.acroForm, multiplechoice_answer:dict, multiplechoice_question:dict,options:list, y:int):
    y_start = y
    for key in multiplechoice_question.keys():
        if y_start < 50:
            c.showPage()
            y_start = 700

        create_radio_group(c,form, key, multiplechoice_question[key], 
                          multiplechoice_answer[key], 50, y_start, options)
        y_start -= 40
        
    #edge case in case it the last iter goes below 50 to start fresh on a new page
    if y_start < 50:
        c.showPage()
        y_start = 700
        
    return y_start

def create_fillin_questionnaire(c: Canvas, form:Canvas.acroForm, fillin_answer:dict, fillin_question:dict, y:int):
    y_start = y-110
    for key in fillin_question.keys():
        if y_start < 50:
            c.showPage()
            y_start = 700
    
        text_area(c,form, 50, y_start , 500, 60, fillin_answer[key], key, fillin_question[key])    
        y_start -= 100
        
    #edge case in case it the last iter goes below 50 to start fresh on a new page
    if y_start < 250:
        c.showPage()
        y_start = 700
        
    return y_start
