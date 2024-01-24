from tkinter import *
from tkinter import messagebox
import phonenumbers

root = Tk()
root.title("Phone Sim Ditector")
root.geometry("550x300")
root.resizable(0,0)

def search():
    num = var.get()
    l = len(num)
    if l == 10:
        from phonenumbers import timezone,geocoder,carrier
        phone = phonenumbers.parse('+91'+num)
        time = timezone.time_zones_for_number(phone)
        sim = carrier.name_for_number(phone,"en")
        reg = geocoder.description_for_number(phone, "en")
        tex1 = "your phone number is - "+"+91"+num
        txt2 = "your sim is - "+sim

        lba.config(text = tex1)
        lbas.config(text = txt2)
        

        

    else:
            messagebox.showerror("Sim Detector","Phone number must cotain 10 number")

var= StringVar()
lbl1 = Label(root,text = "Enter mobile number -  ",font = ("verdana 14 bold"),pady = 10,padx = 5).place(x = 10,y = 10)
ent1 = Entry(root,font = ("verdana 12 bold"),borderwidth=3,width=24,textvariable=var).place(x = 270,y =22)
btn = Button(root,text = "Search information",borderwidth=5,pady = 10,padx = 5,command=search).place(x = 200, y = 60)

lbaph = Label(root,text = "",font = ("verdana 14 bold")).place(x = 20, y = 150)
lbasim = Label(root,text = "",font = ("verdana 14 bold")).place(x = 20, y = 180)
lba = Label(root,text = "",font = ("verdana 14 bold"))
lba.place(x = 20, y = 150)
lbas = Label(root,text = "",font = ("verdana 14 bold"))
lbas.place(x = 20, y = 180)

root.mainloop()