import smtplib  # Simple mail transfer protocol
import speech_recognition as sr
import pyttsx3
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
    server.login('emailexa.smartbot@gmail.com', 'Emailexaisasmartbot')
    email = EmailMessage()
    email['From'] = 'emailexaisasmartbot@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'abdul': 'abdulhussainjarif5262@gmail.com',
    'yukti': 'agarwaalyukti@gmail.com',
    'work': 'work.abdulhussainjarif@gmail.com',
    'salma': 'salmajarif5253@gmail.com'
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

    talk('Hey lazy ass. Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()
