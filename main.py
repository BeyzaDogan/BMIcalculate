import tkinter
from tkinter import *

window=Tk()
window.title("Vücut Kitle İndeksi Hesaplama")
window.minsize(width=300,height=300)

label1=Label(text="Vücut ağırlığınızı giriniz(kg)")
label1.config(padx=10, pady=10)
label1.pack()

kilo=Entry(width=30)
kilo.pack()

label2=Label(text="Boy uzunluğunuzu giriniz(cm)")
label2.config(padx=20, pady=20)
label2.pack()

uzunluk=Entry(width=30)
uzunluk.pack()

sonuc_ekranı=tkinter.Label()
sonuc_ekranı.pack()

def hesaplama():
   ağırlık= float(kilo.get())
   boy=float(uzunluk.get())/100
   sonuc=ağırlık/pow(boy,2)

   str_sonuc=sonucyazdırma(sonuc)
   sonuc_ekranı.config(text=str_sonuc)


button=Button(text="Hesapla",command=hesaplama)
button.config(padx=10,pady=10)
button.pack()
def sonucyazdırma(sonuc):
    str_sonuc= f"BMI : {sonuc} ve  "
    if sonuc<18.5:
       str_sonuc+="zayıfsınız"
    elif 18.5<=sonuc<=24.9 :
       str_sonuc+="normalsiniz"
    elif 25<=sonuc<=29.9:
       str_sonuc+="kilolusunuz"
    elif sonuc>29.9:
       str_sonuc+="obezsiniz,sağlığınız için bir doktor görüşmesi yapmanızı önemle tavsiye ederiz"
    return str_sonuc

window.mainloop()