# Send Mail
# step - 1: goto google account manage
# step - 2: goto privacy > Less secure app access > on (ON होना चाहिए)

import sys
import requests
from datetime import datetime

from send_mail import send_mail

msg_template = """Hello {name},
Thank you for joining {website}. We are very
happy to have you with us.
"""

def format_msg(my_name="User", my_website="cfe.sh"):
    my_msg = msg_template.format(name=my_name, website=my_website)
    return my_msg


def send(name, website=None, to_email=None, verbose=False):
    if to_email == None:
        raise AssertionError
    if website != None:
        msg = format_msg(my_name=name, my_website=website)
    else:
        msg = format_msg(my_name=name)
    if verbose:
        print(name, website, to_email)
    # send the message
    try:
        send_mail(text=msg, to_emails=[to_email], html=None)
        sent = True
    except:
        sent = False
    return sent

if __name__ == "__main__":
    print(sys.argv)
    name = "Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    email = None
    if len(sys.argv) > 2:
        email = sys.argv[2]
    response = send(name, to_email=email, verbose=True)
    print(response)

# run
# $ python send.py Chandra reciever@gmail.com
