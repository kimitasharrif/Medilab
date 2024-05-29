# 1. generate random numbers
# function defination, take no argument
def gen_random():
    import random
    # random is used to gfenerate random numbers and make random selection
    import string
    # provide a collection of string constants including digits,letters
    # initialize the size of string
    N = 6
    # N IS SET TO6, SPECIFIES THE LENGHT OF THE STRING
    # generate random strings
    res = ''.join(random.choices(string.digits, k=N))
    # ''.join() it contactinates the random strings to single string
    # print the function
    print("The generated string is: " + str(res))
    return str(res)

# gen_random()


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
# check_phone("+254797278326")
# check_phone("797278326+254")
          
# check password validity

def passwordvalidity(password):
     if len (password)< 8:
          return("Your password is to short")
     elif not re.search ("[A-Z]",password):
          return("Password must atleast have an uppercase")
     elif not re.search ("[a-z]",password):
          return("Password must atleast have an lowercase")      
     elif not re.search ("[A-Z]",password):
          return("Password must atleast have an uppercase")
     elif not re.search("[0-9]", password):
          return("You must have at least a Number")   
     elif not re.search("[_@$]", password):
          return("You must have at least a symbol") 

     else: 
          return True    

# passwordvalidity(input("Enter your password: "))    


# sending a sms
     
import africastalking
africastalking.initialize(
username="joe2022",
api_key="aab3047eb9ccfb3973f928d4ebdead9e60beb936b4d2838f7725c9cc165f0c8a"
#justpaste.it/1nua8
)
sms = africastalking.SMS
def send_sms(phone, message):
    recipients =[phone]
    sender ="AFRICASTALKING"
    try:
          rensponse = sms.send(message, recipients)
          print(rensponse)
    except Exception as error:
          print("Error is", error) 
# send_sms("+254746096499","This is my message")   

import bcrypt
# hash password
def hash_password(password):
     
     # bcrypt is a module for hashing and checking passwords
     # itr is very secure
     bytes = password.encode("utf-8")
     # password is encoded into bytes
     # it is necessary because bcrypt library works well with byte data
    #  print(bytes)
     salt = bcrypt.gensalt()
     # using a unique salt for each password ensure even if two of their hased password will be different
    #  print(salt)
     hash = bcrypt.hashpw(bytes, salt)
    #  print(hash)
     return hash.decode()
# hash_password(input("Enter your passsword: "))    



# verify password
def hash_verify(password, hashed_password):
     bytes = password.encode("utf-8")
     result = bcrypt.checkpw(bytes,hashed_password.encode())
     print(result)
     return result

# hash_verify("12345","$2b$12$gkcS5tEZ5nuNakrrs65iLuExunAhw1IQHFde3/5aBNlQOyyRASt.i")


# encrypt data
from cryptography.fernet import Fernet
# we import Fernet class
# the module is used for encryption and decryption
def gen_key():
# function used to generate an new encryption key
     key = Fernet.generate_key()
     # print(key)
     with open("key.key", "wb") as key_file:
     # with open it opens a new file if it exists
     # creates a new file if it doesnt exist
     # wb- write binary ensures the file is properly closed after writing on it
      key_file.write(key)


# gen_key()
# load key
def load_key():
     return open("key.key", "rb").read()
# it reads the entire content of the file

# load_key()

# encrypt data
def encrypt(data):
     key = load_key()
     f = Fernet(key)
     # print(f)
     # this creates a fernet object 4 encryption
     encrypt_data = f.encrypt(data.encode())
     print(encrypt_data.decode())

# encrypt("1234")

 
# decrypt data
def decrypt(encrypted_data):
     key = load_key()
     f = Fernet(key)
     decrypted_data = f.decrypt(encrypted_data.encode())
     print(decrypted_data.decode())

# decrypt("gAAAAABmUEKLyoQfQCEd_Tns1oPpWFt2nFQABB0VxuUiahophFWcgLSQoHv1FAJpIeaH-HkGyX7kyLh-Gsk-M7uiFtXVcT950g==")


import requests
import base64
import datetime
from requests.auth import HTTPBasicAuth
def mpesa_payment(amount, phone, invoice_no):
        # GENERATING THE ACCESS TOKEN
        consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
        consumer_secret = "amFbAoUByPV2rM5A"

        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        data = r.json()
        access_token = "Bearer" + ' ' + data['access_token']

        #  GETTING THE PASSWORD
        timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
        business_short_code = "174379"
        data = business_short_code + passkey + timestamp
        encoded = base64.b64encode(data.encode())
        password = encoded.decode('utf-8')

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
            "AccountReference": "account",
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
