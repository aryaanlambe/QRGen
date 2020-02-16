import io
import pyqrcode
from base64 import b64encode
import eel

eel.init('web')

# Eel launch requirements.
@ eel.expose
def dummy (dummy_param):
    print("I got a parameter: ", dummy_param)
    return "string_value", 1, 1.2, True, [1, 2, 3, 4], {"name": "eel"}

# Full generate QR Code feature.
@ eel.expose
def generate_qr(data):
    img = pyqrcode.create(data)
    buffers = io.BytesIO()
    img.png(buffers, scale=8)
    encoded = b64encode(buffers.getvalue()).decode("ascii")
    print("QR Code successfully generated")
    return "data:image/png;base64, " + encoded

# Launch as app, with dimensions: 1000 x 600
eel.start('index.html', size = (1000, 600))
