#this turns a link or text into a qr code
#i will save the qr code as an image
import qrcode


def generate_qr(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size= 10, #styling the size of the box
        border= 1 #border around the code
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color = 'black' , back_color = 'white')

    img.save('qr.png')

inputs = input("Enter the url: \n")
generate_qr(inputs) 






















