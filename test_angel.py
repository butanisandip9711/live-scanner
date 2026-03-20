from SmartApi import SmartConnect

api_key = "8gD0Iflz"

obj = SmartConnect(api_key=api_key)

data = obj.generateSession("S54936548","9030","HY5MERGF2HABP7KYB43AH2SSMU")

print(data)
