a = []
s = input("Bir cümle ya da kelime giriniz : ")
s = s.lower()
a += s

Sıra =[ii for n , ii in enumerate(a) if ii not in a[:n]]

d= "".join(Sıra)
print(d)