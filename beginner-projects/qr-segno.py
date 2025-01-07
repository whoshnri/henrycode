import segno

url = 'www.google.com'

qr = segno.make(url , micro=False , mode='byte')

qr.save("segno-png.png" , border = 1, scale = 2, dark = 'black' , data_dark = 'blue')

#segno is way easier


import pytube