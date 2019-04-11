import sys
dir(sys)
while True:
    def toplama(a,b):
        return a + b
    def carpma(a,b):
        return a * b
    def cikarma(a,b):
        return a - b
    def bolme(a,b):
        return a / b

    print("--------- HESAP MAKINESI ---------")
    print("Toplama Icın 1")
    print("Carpma Icın 2")
    print("Cikarma Icın 3")
    print("Bolme Icın 4")

    secim = int(input("Hangi Islem Yapilacak :"))
    if secim == 5:
        sys.exit('Cikis yaptiniz ....')
    a = int(input("Birinci Sayi :"))
    b = int(input("Ikinci Sayi :"))

    if secim == 1:
        print(a,"+",b,"=",toplama(a,b))
    elif secim == 2:
        print(a, "*", b, "=", carpma(a, b))
    elif secim == 3:
        print(a, "-", b, "=", cikarma(a, b))
    elif secim == 4:
        print(a, "/", b, "=", bolme(a, b))
    else :
        print("Gecersiz Islem !")
