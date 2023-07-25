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

def textbox(c: Canvas, form: Canvas.acroForm, x: int, y: int, width: int, height: int, data: str, name: str, header: str) -> None:
    # c.setFont("Helvetica", 12)
    c.setFont("Times-Roman", 12)
    c.drawString(x, y+30, header)
    form.textfield(name=name,  x=x, y=y, width=width, height=height,
                   value=data, textColor=black, fillColor=HexColor("#EDEDED"), 
                   fieldFlags='readOnly', fontName="Times-Roman")

def create_radio_group(c: Canvas, form:Canvas.acroForm, group_name: str, question: str, data: str, x: int, y: int) -> None:
    """
    Function to create a 2 radio button group in a PDF.
    """
    # draw the question
    c.setFont("Times-Roman", 12)
    chunck_text(c, x, y, question)
    # c.drawString(x, y, question)

    # draw the 'No' radio button
    form.radio(name=group_name, value='No', selected=(data == 'No'), x=x, y=y-20, buttonStyle='circle',
        shape='circle',size=15, fieldFlags='readOnly')

    # draw the 'Yes' radio button
    form.radio(name=group_name,value='Yes', selected=(data == 'Yes'),x=x+50, y=y-20, buttonStyle='circle',
        shape='circle',size=15, fieldFlags='readOnly')

    # draw the 'No' and 'Yes' labels
    c.drawString(x+20, y-20, 'No')
    c.drawString(x+70, y-20, 'Yes')
    
def text_area(c: Canvas, form:Canvas.acroForm, x: int, y: int, width: int, height: int, data: str, name: str, question: str) -> None:
    """
    Function to create a text area in a PDF.
    """
    # draw the question
    c.setFont("Times-Roman", 12)
    chunck_text(c, x, y+80, question)
   

    # draw the text area
    form.textfield(name=name, x=x, y=y, width=width, height=height, 
                   value=data, textColor=black, fillColor=HexColor("#EDEDED"), 
                   fieldFlags='readOnly', fontName="Times-Roman")

def chunck_text(c: Canvas,x: int,y:int, data_str: str) -> None:
    c.setFont("Times-Roman", 12)
    str_width = stringWidth(data_str, "Times-Roman", 12)
    # check if the question string is longer than 550
    if str_width > 500:
        # split the question into multiple lines
        lines = textwrap.wrap(data_str, width=103)  # adjust width as necessary
        for i, line in enumerate(lines):
            c.drawString(x, y - i*14, line)  # adjust 14 (line height) as necessary
    else:
        c.drawString(x, y, data_str)

def client_signature(c: Canvas, x: int, y:int, data_bytes:BytesIO ) -> None:
    # c.setFont("Helvetica", 12)
    c.drawString(x, y, "Client Signature")
    c.line(x+90, y, x+250, y)
    # Now, you can add this "file-like" object to your PDF using reportlab
    c.drawImage(ImageReader(data_bytes), x+130, y= y , width=60, height=60, mask='auto')
    c.drawString(x+350, y, "Date")
    c.line(x+380, y, x+500, y)
    c.drawString(x+400, y+5, gets_todays_date())
    

def create_pdf(data):
    c = canvas.Canvas("form_output.pdf", pagesize=letter)
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
    session_header(c, 50, 610, "Personal Information")
    textbox(c,form, 50, 550, 200, 24, data['personal_info']['name'], 'name', 'Name:')
    textbox(c,form, 350, 550, 200, 24, data['personal_info']['phone'], 'phone', 'Phone:')
    textbox(c,form, 50, 500, 250, 24, data['personal_info']['email'], 'email', 'Email:')
    textbox(c,form, 350, 500, 100, 24, data['personal_info']['gender'], 'gender', 'Gender:')

    # Multiple Choice Question
    session_header(c, 50, 450, "Skin History")
    create_radio_group(c,form, 'aha_usage', 'Have you used any Alpha Hydroxy Acid (AHA) or glycolic products in the past 48-72 hours?', 
                       data['multiple_choice_answers']['aha_usage'], 50, 420)
    create_radio_group(c,form, 'retin_a_usage', 'Are you using Retin-a, Renova or Accutane (an oral form of Retin-a)?', 
                       data['multiple_choice_answers']['retin_a_usage'], 50, 380)
    create_radio_group(c,form, 'skin_thinning_products_usage', 'Are you using any other skin thinning products and/or drugs?', 
                       data['multiple_choice_answers']['skin_thinning_products_usage'], 50, 340)
    create_radio_group(c,form, 'sun_exposure', 'Are you exposed to the sun on a daily basis or are you considering spending more time in the sun soon?', 
                       data['multiple_choice_answers']['sun_exposure'], 50, 300)
    create_radio_group(c,form, 'tanning_bed_usage', 'Do you use a tanning bed?', 
                       data['multiple_choice_answers']['tanning_bed_usage'], 50, 260)
    create_radio_group(c,form, 'is_diabetic', 'Are you diabetic?', 
                       data['multiple_choice_answers']['is_diabetic'], 50, 220)
    
    ###################### Additional Information ######################
    session_header(c, 50, 170, "Additional Information")
    text_area(c, form, 50, 70, 500, 60, data['answers']['medication'], 'medication', 'Are you currently taking medications? If so, please list all (including over the counter drugs/herbal supplements):')
    
   # continue with the rest of the questions on a new page
    c.showPage()
    text_area(c, form, 50, 650, 500, 60, data['answers']['skin_products'], 'skin_products', 'What skin products do you regularly use on your skin?')
    text_area(c, form, 50, 550, 500, 60, data['answers']['cancer_history'], 'cancer_history', 'Have you ever been treated for cancer? If yes, when and what types of therapies were used?')
    text_area(c, form, 50, 450, 500, 60, data['answers']['other_conditions'], 'other_conditions', 'Please list any other illness/condition you are currently being treated for by a medical professional')
    text_area(c, form, 50, 350, 500, 60, data['answers']['menstrual_cycle'], 'menstrual_cycle', '(Female clients) When is your next menstrual cycle due to begin?')

    session_header(c, 50, 300, "Informed Consent Release")
    chunck_text(c, 50, 280, f"I {data['personal_info']['name']} , do fully understand all the questions above and have answered them all correctly and honestly. I understand that the services offered are not a substitute for medical care. I understand that the skin care professional will completely inform me of what to expect in the course of treatment and will recommend adjustments to my regimen if deemed necessary. I also am aware that individual results are dependent upon my age, skin condition, and lifestyle. I agree to actively participate in following appointment schedules and home care procedures to the best of my ability, so that I may obtain maximum effectiveness. In the event that I may have additional questions or concerns regarding my treatment or suggested home product routine, I will inform my skin care professional immediately. I release and hold harmless the skin care professional Laura Lopez, SKIN by Laura Lo, and the staff harmless from any liability for adverse reactions that may result from this treatment.")
    client_signature(c, 50, 80, data["signature_img"])

    c.save()
