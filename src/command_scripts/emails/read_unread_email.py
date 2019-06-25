# this will read the latest unread email
import imaplib
import email
import os
import json

# custom module
import speak
import hotword

login_file = "/home/pi/2019-ca400-randlea2/src/command_scripts/emails/login_details.json"

def get_login_details():
    try:
        login_details_file = open(login_file)
        login_details = json.load(login_details_file)
        email_address = login_details["email_address"]
        password = login_details["password"]
        return email_address, password
    except:
        speak.speak_to_user("problem connecting to g mail please try again")
        return None

def get_emails():
    try:
        gmail_url = "imap.gmail.com"
        connection = imaplib.IMAP4_SSL(gmail_url)
        email_address, password = get_login_details()
        connection.login(email_address, password)
        connection.select("INBOX")
        # retrieve all the unread email id's
        (return_code, emails) = connection.search(None, '(UNSEEN)')
        unread_email_numbers = emails[0].split()
        print(unread_email_numbers)
        # retrieve the latest unread email
        latest_unread_number = unread_email_numbers[-1]
        print(latest_unread_number)
        category, data = connection.fetch(latest_unread_number, "(RFC822)")
        for response_part in data:
            if isinstance(response_part, tuple):
                latest_unread = email.message_from_bytes(response_part[1])
        latest_unread_from = latest_unread['from'].split()[0]
        latest_unread_subject = latest_unread["subject"]
        latest_unread_body = get_email_body(latest_unread)
        # format these for speaking
        email_details = "the last un read email is from {} with the subject {} and main body {}".format(latest_unread_from,
                                                                                                       latest_unread_subject,
                                                                                                       latest_unread_body)
        print(email_details)
        return email_details
    except:
        speak.speak_to_user("your inbox is empty")
        return None


def get_email_body(email):
    # retrieve all parts of the email
    if email.is_multipart():
        for part in email.get_payload():
            body = part.get_payload()
            # more processing?
    else:
        body = email.get_payload()
    return body


def read_emails():
    unread_email = get_emails()
    if unread_email is None:
        speak.speak_to_user("there are no unread emails")
    else:
        print(unread_email)
        speak.speak_to_user(unread_email)
    hotword.detect_hotword()
    return None


def main():
    read_emails()

if __name__ == "__main__":
    main()
