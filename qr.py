import qrcode


data = "https://www.instagram.com/tayel.ourlife/" # example link for ig account 

# إنشاء QR Code
qr = qrcode.QRCode(
    version=1,  
    box_size=10,  
    border=2    )
qr.add_data(data)
qr.make(fit=True)

# covert to img
img_qr = qr.make_image(fill='black', back_color='white')
img_qr.show()  # open window 