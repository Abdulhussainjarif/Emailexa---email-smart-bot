import smtplib                      # Simple mail transfer protocol
import speech_recognition as sr
import pyttsx3                      # python text to speech module
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    # Creating a server and opening a port '587'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # start Transport layer security
    # Provided Login credentials
    server.login('Enter your Email address here', 'Enter email password here')
    email = EmailMessage()
    email['From'] = 'Enter your Email address here'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'nickname1': 'nickname1@gmail.com',
    'nickname2': 'nickname2@gmail.com',
    'nickname3': 'nickname3@gmail.com',
    'nickname4': 'nickname4@gmail.com',
    'nickname5': 'nickname5@gmail.com'
}


def get_email_info():
    talk('To Whom you want to send email:')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the message in your email?')
    message = get_info()
    send_email(receiver, subject, message)

    talk('Email Automation Complete!')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()
