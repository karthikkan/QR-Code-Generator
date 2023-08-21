import qrcode
import image
def generateqr(url):
    qr=qrcode.QRCode(
        version = 1, 
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black",back_color="white")
    img.save("qrimg001.png")
url=input("Enter URL:")
generateqr(url)