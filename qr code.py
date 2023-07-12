import qrcode

img = qrcode.make('https://sugarrats.github.io/gamelle-servie/')

img.save('soiréeQR.jpg')