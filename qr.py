import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)


def qrgen(s):
    # qr.add_data(s)
    # qr.make(fit=True)
    #
    # img = qr.make_image(fill_color="black", back_color="white")

    qr = qrcode.QRCode()
    img = qr
    qr.add_data('Какие-то данные или URL-адрес')

    return img