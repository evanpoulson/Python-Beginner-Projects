
import qrcode
#from pyzbar.pyzbar import decode
from PIL import Image

#function which encodes a qrcode with the data that a user specifies
def encode_qr():
    print('\nQR Encoder\n----------')
    code_name = input('What is the name of the QR Code?: ')
    code_data = input('What is the data to be encoded?: ')
    code = qrcode.make(code_data)
    code.save(code_name)

#function which decodes a qrcode
def decode_qr():
    file_location = input('What is the file path of the QR Code?: ')
    qr_code = Image.open(file_location)
    result = decode(qr_code)
    print(result)

print('\n\n')
print('QR Code Encoder/Decoder')
print('-----------------------')
print('\n')

choice = input('Would you like to the the Encoder or the Decoder? (E/N): ')
if choice == 'E' or choice == 'e':
    encode_qr()
elif choice == 'D' or choice == 'd':
    decode_qr()
else:
    print('Invalid Input, please restart program!')