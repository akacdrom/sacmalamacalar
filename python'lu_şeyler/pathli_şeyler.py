import os
from os import path
import sys

x = 1
a = 1
if path.exists("denenme_klasör1"):
    os.system("rm -r denenme*")
    print("dosyolar bulundu silindi.")
    sys.exit()
else:
	print("süreç işleniyor, lütfen bekleyin")
while x <= 10: 
    x = x+1
    os.system('mkdir denenme_klasör' + str(a))
    a = a + 1

