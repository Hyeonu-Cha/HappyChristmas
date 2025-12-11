import qrcode

# Simple generation
img = qrcode.make('https://hyeonu-cha.github.io/HappyChristmas/')
img.save("qr.png")

# Advanced generation (controlling size and error correction)
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://hyeonu-cha.github.io/HappyChristmas/')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("advanced_qr.png")