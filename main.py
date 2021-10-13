import qrcode
from PIL import Image
import os

# generate general QRCode image
def make_qr(str,save):
    qr=qrcode.QRCode(
        version=4,  #size of QRCode image 1-40  1:21*21（21+(n-1)*4）
        error_correction=qrcode.constants.ERROR_CORRECT_M, #L:7% M:15% Q:25% H:30%
        box_size=10, # pixel size of every box
        border=2, # border width size
    )
    qr.add_data(str)
    qr.make(fit=True)

    img=qr.make_image()
    img.save(save)


# generate QRCode with logo image
def make_logo_qr(str,logo,save):
    qr=qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=8,
        border=2
    )

    # add string to transform
    qr.add_data(str)

    qr.make(fit=True)
    # generate QRCode
    img=qr.make_image()

    img=img.convert("RGBA")

    # add logo
    if logo and os.path.exists(logo):
      pass

    # save QRCode image
    img.save(save)


if __name__=='__main__':
    save_path='theqrcode.png' # saved to this file
    logo='logo.jpg'  # load logo image from local directory

    str=input('Please input your string：')
    # for python2, you can use `raw_input` to replace `input`

    #make_qr(str)

    make_logo_qr(str,logo,save_path)
