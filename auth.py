# length of OTP in digits
length = 6

# timestep or time-window for which the token is valid
step_in_seconds = 30 

import base64

# random key
key = b"123123123djwkdhawjdk"

token = base64.b32encode(key)

print(token.decode("utf-8"))








import hashlib 
import hmac 
import math 
import time

t = math.floor(time.time() // step_in_seconds)

hmac_object = hmac.new(key, t.to_bytes(length=8, byteorder="big"), hashlib.sha1)
hmac_sha1 = hmac_object.hexdigest()

# truncate to 6 digits
offset = int(hmac_sha1[-1], 16)
binary = int(hmac_sha1[(offset * 2):((offset * 2) + 8)], 16) & 0x7fffffff
totp = str(binary)[-length:]
print(totp)


# Generating QR Code
image_path = "/tmp/token_qr.png"

import qrcode

qr_string = "otpauth://totp/Example:my-email-address@gmail.com?secret=" + token.decode("utf-8") +"&issuer=Example&algorithm=SHA1&digits=6&period=30"
print(qr_string)
img = qrcode.make(qr_string)
img.save(image_path)