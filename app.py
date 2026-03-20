from SmartApi import SmartConnect
import pyotp

api_key = "eCZzvAKp"
client_code = "S54936548"
password = "9030"
totp_secret = "HY5MERGF2HABP7KYB43AH2SSMU"

totp = pyotp.TOTP(totp_secret).now()

obj = SmartConnect(api_key=api_key)
session = obj.generateSession(client_code, password, totp)

print("Angel Login Success")
