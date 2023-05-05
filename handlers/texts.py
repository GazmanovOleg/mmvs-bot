from aiogram.utils.markdown import hlink
START_TEXT = """
Hello there👋👋👋\n
We are a team of experienced and passionate developers\nspecializing in video services development. We provide cutting-\nedge solutions that exceed our clients' expectations.\n
Our team develops applications, video services and streaming\nplatforms.\n
With our bot, you can learn more about our company, choose a\nconvenient way to contact us, or leave us a request.\n
Please use the buttons below to select commands
"""


SERVICE_TEXT = """Our team has in-depth technical knowledge of video technology,
enabling us to develop software solutions of any complexity.
Please select the service you require
"""
ABOUT_US_TEXT = """<b>4Key Development</b> is a group of IT specialists consisting of
developers, analysts, QA engineers and project managers. We
have over 10 years experience in video and network
technologies.

Our experienced team delivers cutting edge technology to meet
your needs. We are committed to achieving customer goals and
strive to provide timely and cost effective solutions.\n 
What makes our services unique:
⏰The time and materials model
📈Fast time-to-market (low time-to-market)
🛠Ongoing monitoring of the development process 
💪Hard-to-find skills in video technology
"""
text = hlink('WhatsApp', 'https://wa.me/+79236586084')
GET_IN_TOUCH_TEXT = f"Get in touch\n{text}\nor E-mail us\n4keyteam@gmail.com"





APPLICATION_TEXT = """We develop mobile and web applications for any task, especially\nthose related to video technology.\n
We can develop:
✅Video conference application
✅Video players
✅Video editors
"""

DEVELOPMENT_TEXT = """Our development team will analyze, develop, test and implement
the service for your needs. 
We have expertise in working with databases, front-end and back-
end development, which enables us to produce high quality
software products in any direction."""

VIDEO_SERVICES_TEXT = """Our team can develop an online or offline video service for you.
We have extensive experience with video hosting, online players,
and video editors.
We can also integrate a video service on your website or blog.
"""
                            
BROADCASTING_TEXT = """We specialize in video streaming technology and can add
streaming functionality to anything.
Our services include developing a streaming platform for you,
adding live video feeds to your website, creating online video chat
systems and providing remote camera connection services.

With the experience of our team, anything is possible!"""

def what_is_this_text(text):
    answer = ''
    text = ("<b>"+text+"</b>").split()
    if text == BROADCASTING_TEXT.split():
        answer = "Видео стриминг"
    if text == VIDEO_SERVICES_TEXT.split():
        answer = "Видео сервис"
    if text == DEVELOPMENT_TEXT.split():
        answer = "Разработка"
    if text == APPLICATION_TEXT.split():
        answer = "Приложение"


































        
    
    return answer
