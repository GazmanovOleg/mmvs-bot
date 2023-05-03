from aiogram.utils.markdown import hlink
START_TEXT = """
<b>
Hello there</b> \n
We are a team of experienced and passionate developers who specialize in video service developers. We offer cutting-edge solutions that exceed our customers' expectations.\n
Our team develops applications, video services and streaming platforms.\n
With our bot you can learn more about our company, choose a convenient way to contact us or leave a request for us.\n
Please use the buttons below to select commands

"""


SERVICE_TEXT = """<b>Our team has in-depth technical knowledge of video technology, which allows us to develop a software solution of any complexity. Please choose which service you require.</b>"""
ABOUT_US_TEXT = """<b>4Key Development is a group of IT specialists consisting of developers, analysts, QA engineers and project managers. We have over 10 years experience in video and network technologies.\n 
Our experienced team delivers cutting edge technology to meet your needs. We are committed to achieving customer goals and strive to provide timely and cost effective solutions.\n 
What makes our services unique:
    - The time and materials model
    - Fast time-to-market (low time-to-market)
    - Ongoing monitoring of the development process 
    - Hard-to-find skills in video technology</b>

"""
text = hlink('WhatsApp', 'https://wa.me/+79236586084')
GET_IN_TOUCH_TEXT = f"<b>Get in touch</b> \n {text} \n or E-mail us\n 4keyteam@gmail.com"





APPLICATION_TEXT = """<b>We develop mobile and web applications for any task, especially those related to video technology.\n
We can develop:\n
    -  Video conference application
    -  Video players
    -  Video editors</b>
"""

DEVELOPMENT_TEXT = """<b>Our development team will analyze, develop, test and implement the service for your needs. We have expertise in working with databases, front-end and back-end development, which enables us to produce high quality software products in any direction.</b>"""

VIDEO_SERVICES_TEXT = """<b>Our team can develop an online or offline video service for you.\n
We have extensive experience with video hosting, online players, and video editors.\n
 We can also integrate a video service on your website or blog.</b>\n
"""

BROADCASTING_TEXT = """<b>We specialize in video streaming technology and can add streaming functionality to anything. \n Our services include developing a streaming platform for you, adding live video feeds to your website, creating online video chat systems and providing remote camera connection services.
With the experience of our team, anything is possible!</b>

"""

def what_is_this_text(text):
    answer = ''
    text = ("<b>"+text+"</b>").split()
    if text == BROADCASTING_TEXT.split():
        print("Текст зашел в трансляции")
        answer = "Видео стриминг"
    if text == VIDEO_SERVICES_TEXT.split():
        answer = "Видео сервис"
    if text == DEVELOPMENT_TEXT.split():
        answer = "Разработка"
    if text == APPLICATION_TEXT.split():
        answer = "Приложение"
    
    return answer
