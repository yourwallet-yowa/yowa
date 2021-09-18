#For runninng qrGenerate.py
#1- pip install qrcode
#2- python qrGenerate.py value ex:  python qrGenerate.py 5.3
#easy use:  open cmd ( terminal ) and enter " python qrGenerate.py 5.3 "

import qrcode
import sys

walletAddress = "your wallet address"

def generateQR(data):
    img = qrcode.make(str(data)+":"+str(walletAddress))
    img.show()

generateQR(sys.argv[1])
