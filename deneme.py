from getpass import getpass
import sys
denkullanici = input("bir kullanıcı adı girin: ")
denparola = getpass("şifrenizi giriniz: ")
if (denparola == denkullanici):
    print("kullanıcı adı ve şifre aynı olamıyor maalesef")
    sys.exit()

kullanici = input("kullanıcı adınız: ")
parola = getpass("parolanız: ")

if (kullanici == denkullanici) and (parola == denparola):
    print("hoşgeldinisss efendimissss")
elif (kullanici != denkullanici):
    print("yanlış kullanıcı adı")
    sys.exit()
elif (parola != denparola):
    print("yanlış parola şifreyi yenilemek için 2 kere aynı şeyi yazın ")
    sifre = getpass("Şifrenis: ")
    sifre2 = getpass("Şifreniss: ")
    if (sifre == sifre2):

        denparola = getpass("bir parola girin: ")
        parola = getpass("parolanız: ")
        if (parola == denparola):
            print("hoşgeldinisss efendimissss")
        else:
            print("böyle hiç olmaz reis")
            sys.exit()
    else:
        print("böyle olmaz reis")
        sys.exit()
else:
    print("bi sıkıntı var. bende çözemedim")
    sys.exit()