from cryptography.fernet import Fernet


### I have already used Fernet.generate_key() and deleted it after that
#   Then I used  fernet.encrypt(API.encode()) to crypt the API key
#   The following code is the clean version because I only need the generated key
#   and to decrypt the API key  ###



with open("securitykeys-web/token.txt", "r") as file:
    key=file.read().encode()


fernet=Fernet(key)


with open("securitykeys-web/pass.txt", "r") as file:
    res=file.read()


with open("securitykeys-web/mail_pass.txt","r") as file:
    email_pass=file.read()


res=res.encode()
decKEY=fernet.decrypt(res).decode()
email_pass=email_pass.encode()
decPASS=fernet.decrypt(email_pass).decode()

