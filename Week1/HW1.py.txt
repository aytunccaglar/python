for i in range(0,3) :
    sayi1 = int(input("Birinci sayiyi giriniz:"))
    sayi2 = int(input("ikinci sayiyi giriniz:"))
    islem = input("Yapacaginiz islemi seciniz(+,-,/,*,exit):")
    if islem == "+" :
        print (sayi1+sayi2)
    elif islem == "-" :
        print (sayi1-sayi2)
    elif islem == "*" :
        print (sayi1*sayi2)
    elif islem =="/" :
        print (sayi1/sayi2)
    elif islem == "exit":
        break
    else:
        print("Lutfen belirtilen operatorlerden birini giriniz")