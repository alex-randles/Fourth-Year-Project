import smtplib
# import configuration
import os
import sys
import difflib
import subprocess
import json


# custom modules
import translate_speech
import speak
import hotword

login_file = "/home/pi/2019-ca400-randlea2/src/command_scripts/emails/login_details.json"

def main(spoken_words):
    recipient = find_recipient(spoken_words)
    if recipient is not None:
        speak.speak_to_user("sending email to {}".format(recipient))
        speak.speak_to_user("what is the subject matter")
        subject = translate_speech.start_translator() 
        # subject = "this is a test"
        speak.speak_to_user("what is main body")
        message_content = translate_speech.start_translator()
        # message_content = "testing"
        send_email(recipient, subject, message_content)
    else:
        speak.speak_to_user("email address not found")
    # start hotword detection after email sent
    hotword.detect_hotword()

def get_login_details():
    login_details_file = open(login_file)
    login_details = json.load(login_details_file)
    email_address = login_details["email_address"]
    password = login_details["password"]
    return email_address, password

def send_email(receiver_email, subject, message_content):
    try:
        # connect to gmail smtp server
        gmail_server = smtplib.SMTP("smtp.gmail.com:587")
        gmail_server.ehlo()
        # start connection
        gmail_server.starttls()
        # login to server
        email_address, password = get_login_details()
        gmail_server.login(email_address, password)
        # create the email
        message = "subject: {}\n\n{}".format(subject, message_content)
        # send email
        gmail_server.sendmail(email_address, receiver_email, message)
        # close the connection
        gmail_server.quit()
        speak.speak_to_user("email sent successfully")
        print("email sent successfully")
    except:
        speak.speak_to_user("problem sending email, check your internet connection")


def find_recipient(spoken_words):
    json_file = open('/home/pi/2019-ca400-randlea2/src/command_scripts/emails/contacts.json')
    data = json.load(json_file)
    for word in spoken_words:
        # check if exact words are a contact
        if word in data:
            return data[word]["email"]
    # dont match send an email as they wont be a possible contact
    excluded_words = ["send","email","a", "an", "to"]
    spoken_words = " ".join([word for word in spoken_words if word not in excluded_words])
    # find closest match otherwise
    contact_names = [name for name in data]
    closest_match = difflib.get_close_matches(spoken_words, contact_names)
    if closest_match:
        return data[closest_match[0]]["email"]
    else:
        # no email found
        return None




if __name__ == "__main__":
    main(sys.argv[1:])
