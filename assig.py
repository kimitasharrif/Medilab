# Write a function to generate 6n random numbers
# Functionn to check if phone number is in the correct format
import random

def gen_random():
    import string
    import random



    N=6
    
    # using random.choices()
    # generating random strings
    res = ''.join(random.choices(string.digits , k=N))
    # print result
    print("The generated random string : " + str(res))
    # return str(res)
gen_random()
    

# 2. check if phone number is valid
#
import re
# its a module which provides support for workinf with regular expression
def check_phone(phone):
    # the function takes one argument phone
    regex= "^\+254\d{9}"
    # ^ asserts the start of the string,
    # \+254 it matches the literalstring +254
    # \d{9} matches exactly nine digits
    if not re.match(regex, phone) or len(phone) != 13:
          print("Phone is not valid")
          return False
    else:
          print("Phone is valid, OK")
          return True
check_phone("+254797278326")
check_phone("797278326+254")



# 22 assigment imagine third day

# 1. Write a function to encrypt data usingFernrt in flask
# 2. Write a function to decrypt data using Fernet in flask

# generates Encryption Key
from cryptography.fernet import  Fernet
def gen_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
# Test
#gen_key()
def load_key():
    return open("key.key", "rb").read()

def encrypt(data):
    key = load_key()
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    print("Plain ", data)
    print("Encrypted ", encrypted_data.decode())
    return encrypted_data.decode()
# Test
#encrypt("+254729225710")
#gAAAAABkfZo0aTwxI1m5QSF3go_Vsfjb8IL3lAV4c3qn7DyI2wb3z7XIMOR34AWyPOaJ7jvswTQuTZxBdLCjZsw0AojM4R5s9w==

def decrypt(encrypted_data):
    key = load_key()
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data.encode())
    print("Decrypted data ", decrypted_data.decode())
    return decrypted_data.decode()
# Test - Provide the Encrypted
#decrypt("gAAAAABkfZo0aTwxI1m5QSF3go_Vsfjb8IL3lAV4c3qn7DyI2wb3z7XIMOR34AWyPOaJ7jvswTQuTZxBdLCjZsw0AojM4R5s9w==")
# Symetric and Asymetric Encryption
# Asymetric Encryption - Research using Python. 
# Pending ******


def send_email(email, message):
    import smtplib
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login("modcomlearning2@gmail.com", "")
    # sending the mail
    s.sendmail("modcomlearning@gmail.com", email, message)
    # terminating the session
    s.quit()
    
# Test
#send_email("johndoe@gmail.com", "Test Email")
import requests
import base64
import datetime
from requests.auth import HTTPBasicAuth

# In this fucntion we provide phone(used to pay), amount to be paid and invoice no being paid for.
def mpesa_payment(amount, phone, invoice_no):
        # GENERATING THE ACCESS TOKEN
        consumer_key = "oAN7tFvWXa4qJ6XWAqcjG3RZoMGsSOXA"
        consumer_secret = "J2TFUVbsnM5CEvvr"

        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        data = r.json()
        access_token = "Bearer" + ' ' + data['access_token']
        print(access_token)

        #  GETTING THE PASSWORD
        timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
        business_short_code = "174379"
        data = business_short_code + passkey + timestamp
        encoded = base64.b64encode(data.encode())
        password = encoded.decode('utf-8')
        print(password)

        # BODY OR PAYLOAD
        payload = {
            "BusinessShortCode": "174379",
            "Password": "{}".format(password),
            "Timestamp": "{}".format(timestamp),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,  # use 1 when testing
            "PartyA": phone,  # change to your number
            "PartyB": "174379",
            "PhoneNumber": phone,
            "CallBackURL": "https://modcom.co.ke/job/confirmation.php",
            "AccountReference": "Lab Account",
            "TransactionDesc": "account"
        }

        # POPULAING THE HTTP HEADER
        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json"
        }

        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  # C2B URL

        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
# Test
# mpesa_payment("2", "254729225710", "NCV003")

def gen_pdf():
    # Python program to create
    # a pdf file
    from fpdf import FPDF
    # save FPDF() class into a
    # variable pdf
    pdf = FPDF()
    # Add a page
    pdf.add_page()
    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size=15)
    # create a cell
    pdf.cell(200, 10, txt="ModcomInstitute of tech",
             ln=1, align='L')
    # add another cell
    pdf.cell(200, 10, txt="A Computer Science portal for geeks.",
             ln=2, align='C')
    
    pdf.cell(200, 10, txt="Welcome.",
             ln=2, align='C')
    # save the pdf with name .pdf
    pdf.output("cv.pdf")

# Test
#gen_pdf()
    
    # we codingis somehow difficult to learn  it require practising and understanding and practising
