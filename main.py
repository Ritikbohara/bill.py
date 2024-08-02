from tkinter import *
import random
import os
import sys
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#0A7CFF")
        self.root.title("Resturent Billing System - CodeWithCurious.com")
        title=Label(self.root,text="Resturent Billing System",bd=12,relief=RIDGE,font=("Arial Black",20),bg="#A569BD",fg="white").pack(fill=X)
        #===================================variables=======================================================================================
        self.Samosa=IntVar()
        self.noodles=IntVar()
        self.PaneerTikka=IntVar()
        self.VegetablePakora=IntVar()
        self.PapdiChaat=IntVar()
        self.TomatoSoup=IntVar()
        self.MasalaPapad=IntVar()
        self.Soup=IntVar()
        self.pasta=IntVar()
        self.ButterChicken=IntVar()
        self.PaneerMasala=IntVar()
        self.BasmathiRice=IntVar()
        self.dal=IntVar()
        self.PalakPaneer=IntVar()
        self.CholeBhuture=IntVar()
        self.AlooTikkiChaa=IntVar()
        self.DahiVada=IntVar()
        self.PavBhaji=IntVar()
        self.BhelPuri=IntVar()
        self.Pokara=IntVar()
        self.ChickenTikka=IntVar()
        self.total_sna=StringVar()
        self.total_gro=StringVar()
        self.total_hyg=StringVar()
        self.a=StringVar()
        self.b=StringVar()
        self.c=StringVar()
        self.c_name=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.phone=StringVar()
        #==========================================customer details label frame=================================================
        details=LabelFrame(self.root,text="Customer Details",font=("Arial Black",12),bg="#A569BD",fg="white",relief=GROOVE,bd=10)
        details.place(x=0,y=80,relwidth=1)
        cust_name=Label(details,text="Customer Name",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=0,padx=15)

        cust_entry=Entry(details,borderwidth=4,width=30,textvariable=self.c_name).grid(row=0,column=1,padx=8)

        contact_name=Label(details,text="Contact No.",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=2,padx=10)

        contact_entry=Entry(details,borderwidth=4,width=30,textvariable=self.phone).grid(row=0,column=3,padx=8)

        bill_name=Label(details,text="Bill.No.",font=("Arial Black",14),bg="#A569BD",fg="white").grid(row=0,column=4,padx=10)

        bill_entry=Entry(details,borderwidth=4,width=30,textvariable=self.bill_no).grid(row=0,column=5,padx=8)
        #=======================================Resturant Menu=================================================================
        snacks=LabelFrame(self.root,text="Starter",font=("Arial Black",12),bg="#E5B4F3",fg="#6C3483",relief=GROOVE,bd=10)
        snacks.place(x=5,y=180,height=380,width=325)

        item1=Label(snacks,text="Samosa",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item1_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.Samosa).grid(row=0,column=1,padx=10)

        item2=Label(snacks,text="Paneer Tikka",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item2_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.PaneerTikka).grid(row=1,column=1,padx=10)

        item3=Label(snacks,text="Chicken Tikka",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item3_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.ChickenTikka).grid(row=2,column=1,padx=10)

        item4=Label(snacks,text="Vegetable Pakora",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item4_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.VegetablePakora).grid(row=3,column=1,padx=10)

        item5=Label(snacks,text="Papdi Chaat",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item5_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.PapdiChaat).grid(row=4,column=1,padx=10)

        item6=Label(snacks,text="Tomato Soup",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item6_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.TomatoSoup).grid(row=5,column=1,padx=10)

        item7=Label(snacks,text="Masala Papad",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item7_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.MasalaPapad).grid(row=6,column=1,padx=10)
        #=================================== Main Course =====================================================================================
        Starter=LabelFrame(self.root,text="Main Course",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        Starter.place(x=340,y=180,height=380,width=325)

        item8=Label(Starter,text="Butter Chicken",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item8_entry=Entry(Starter,borderwidth=2,width=15,textvariable=self.ButterChicken).grid(row=0,column=1,padx=10)

        item9=Label(Starter,text="Pasta",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item9_entry=Entry(Starter,borderwidth=2,width=15,textvariable=self.pasta).grid(row=1,column=1,padx=10)

        item10=Label(Starter,text="Basmathi Rice",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item10_entry=Entry(Starter,borderwidth=2,width=15,textvariable=self.BasmathiRice).grid(row=2,column=1,padx=10)

        item11=Label(Starter,text="Paneer Masala",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item11_entry=Entry(Starter,borderwidth=2,width=15,textvariable=self.PaneerMasala).grid(row=3,column=1,padx=10)

        item12=Label(Starter,text="Palak Paneer",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item12_entry=Entry(Starter,borderwidth=2,width=15,textvariable=self.PalakPaneer).grid(row=4,column=1,padx=10)

        item13=Label(Starter,text="Daal",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item13_entry=Entry(Starter,borderwidth=2,width=15,textvariable=self.dal).grid(row=5,column=1,padx=10)

        item14=Label(Starter,text="Chole Bhuture",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item14_entry=Entry(Starter,borderwidth=2,width=15,textvariable=self.CholeBhuture).grid(row=6,column=1,padx=10)
        #========================================Snacks===============================================================================
        hygine=LabelFrame(self.root,text="Snacks",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#E5B4F3",fg="#6C3483")
        hygine.place(x=677,y=180,height=380,width=325)

        item15=Label(hygine,text="Noodles",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=0,column=0,pady=11)
        item15_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.noodles).grid(row=0,column=1,padx=10)

        item16=Label(hygine,text="Aloo Tikki Chaat",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=1,column=0,pady=11)
        item16_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.AlooTikkiChaa).grid(row=1,column=1,padx=10)

        item17=Label(hygine,text="Dahi Vada",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=2,column=0,pady=11)
        item17_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.DahiVada).grid(row=2,column=1,padx=10)

        item18=Label(hygine,text="Pav Bhaji",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=3,column=0,pady=11)
        item18_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.PavBhaji).grid(row=3,column=1,padx=10)

        item19=Label(hygine,text="Bhel Puri",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=4,column=0,pady=11)
        item19_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.BhelPuri).grid(row=4,column=1,padx=10)

        item20=Label(hygine,text="Soup",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=5,column=0,pady=11)
        item20_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.Soup).grid(row=5,column=1,padx=10)

        item21=Label(hygine,text="Pokara",font=("Arial Black",11),bg="#E5B4F3",fg="#6C3483").grid(row=6,column=0,pady=11)
        item21_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.Pokara).grid(row=6,column=1,padx=10)
        #=====================================================billarea==============================================================================
        billarea=Frame(self.root,bd=10,relief=GROOVE,bg="#E5B4F3")
        billarea.place(x=1010,y=188,width=330,height=372)

        bill_title=Label(billarea,text="Bill Area",font=("Arial Black",17),bd=7,relief=GROOVE,bg="#E5B4F3",fg="#6C3483").pack(fill=X)

        scrol_y=Scrollbar(billarea,orient=VERTICAL)
        self.txtarea=Text(billarea,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        #=================================================billing menu=========================================================================================
        billing_menu=LabelFrame(self.root,text="Billing Summery- 202300819010065-89",font=("Arial Black",12),relief=GROOVE,bd=10,bg="#A569BD",fg="white")
        billing_menu.place(x=0,y=560,relwidth=1,height=137)

        total_snacks=Label(billing_menu,text="Total Snacks Price",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=0,column=0)
        total_snacks_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_sna).grid(row=0,column=1,padx=10,pady=7)

        total_Starter=Label(billing_menu,text="Total Starter Price",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=1,column=0)
        total_Starter_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_gro).grid(row=1,column=1,padx=10,pady=7)


        total_hygine=Label(billing_menu,text="Total Main Course Price",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=2,column=0)
        total_hygine_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_hyg).grid(row=2,column=1,padx=10,pady=7)

        tax_snacks=Label(billing_menu,text="Snacks Tax",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=0,column=2)
        tax_snacks_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.a).grid(row=0,column=3,padx=10,pady=7)

        tax_Starter=Label(billing_menu,text="Starter Tax",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=1,column=2)
        tax_Starter_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.b).grid(row=1,column=3,padx=10,pady=7)


        tax_hygine=Label(billing_menu,text=" Main Course Tax",font=("Arial Black",11),bg="#A569BD",fg="white").grid(row=2,column=2)
        tax_hygine_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.c).grid(row=2,column=3,padx=10,pady=7)

        button_frame=Frame(billing_menu,bd=7,relief=GROOVE,bg="#6C3483")
        button_frame.place(x=830,width=500,height=95)

        button_total=Button(button_frame,text="Total Bill",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=lambda:total(self)).grid(row=0,column=0,padx=12)
        button_clear=Button(button_frame,text="Clear Field",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=lambda:clear(self)).grid(row=0,column=1,padx=10,pady=6)
        button_exit=Button(button_frame,text="Exit",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",width=8,command=lambda:exit1(self)).grid(row=0,column=2,padx=10,pady=6)
        intro(self)


def total(self):
    
    if (self.c_name.get=="" or self.phone.get()==""):
        messagebox.showerror("Error", "Fill the complete Customer Details!!")
    self.Sa=self.Samosa.get()*20
    self.no=self.noodles.get()*40
    self.PT=self.PaneerTikka.get()*120
    self.PB=self.PavBhaji.get()*100
    self.CB=self.CholeBhuture.get()*30
    self.BP=self.BhelPuri.get()*30
    self.PO=self.Pokara.get()*15
    total_snacks_price=(
                self.Sa+
                self.no+
                self.PT+
                self.PB+
                self.CB+
                self.BP+
                self.PO)
    self.total_sna.set(str(total_snacks_price)+" Rs")
    self.a.set(str(round(total_snacks_price*0.05,3))+" Rs")

    self.pa=self.pasta.get()*90
    self.Sp=self.Soup.get()*40
    self.DV=self.DahiVada.get()*60
    self.ATc=self.AlooTikkiChaa.get()*55
    self.PP=self.PalakPaneer.get()*80
    self.da=self.dal.get()*76
    total_Starter_price=(
        
        self.pa+
        self.Sp+
        self.DV+
        self.ATc+
        self.PP+
        self.da)

    self.total_gro.set(str(total_Starter_price)+" Rs")
    self.b.set(str(round(total_Starter_price*0.01,3))+" Rs")

    self.PM=self.PaneerMasala.get()*130
    self.BR=self.BasmathiRice.get()*80
    self.BC=self.ButterChicken.get()*130
    self.MP=self.MasalaPapad.get()*50
    self.VP=self.VegetablePakora.get()*85
    self.TS=self.TomatoSoup.get()*60
    self.CT=self.ChickenTikka.get()*20

    total_hygine_price=(
        self.PM+
        self.BR+
        self.BC+
        self.MP+
        self.VP+
        self.TS+
        self.CT)

    self.total_hyg.set(str(total_hygine_price)+" Rs")
    self.c.set(str(round(total_hygine_price*0.10,3))+" Rs")
    self.total_all_bill=(total_snacks_price+
                total_Starter_price+
                total_hygine_price+
                (round(total_Starter_price*0.01,3))+
                (round(total_hygine_price*0.10,3))+
                (round(total_snacks_price*0.05,3)))
    self.total_all_bil=str(self.total_all_bill)+" Rs"
    billarea(self)
def intro(self):
    self.txtarea.delete(1.0,END)
    self.txtarea.insert(END,"\tWELCOME TO SUPER MARKET\n\tPhone-No.739275410")
    self.txtarea.insert(END,f"\n\nBill no. : {self.bill_no.get()}")
    self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
    self.txtarea.insert(END,f"\nPhone No. : {self.phone.get()}")
    self.txtarea.insert(END,"\n====================================\n")
    self.txtarea.insert(END,"\nProduct\t\tQty\tPrice\n")
    self.txtarea.insert(END,"\n====================================\n")
def billarea(self):
    intro(self)
    if self.Samosa.get()!=0:
        self.txtarea.insert(END,f"Samosa\t\t {self.Samosa.get()}\t{self.Sa}\n")
    if self.noodles.get()!=0:
        self.txtarea.insert(END,f"Noodles\t\t {self.noodles.get()}\t{self.no}\n")
    if self.PaneerTikka.get()!=0:
        self.txtarea.insert(END,f"PaneerTikka\t\t {self.PaneerTikka.get()}\t{self.PT}\n")
    if self.PavBhaji.get()!=0:
        self.txtarea.insert(END,f"PavBhaji\t\t {self.PavBhaji.get()}\t{self.PB}\n")
    if self.CholeBhuture.get()!=0:
        self.txtarea.insert(END,f"CholeBhuture\t\t {self.CholeBhuture.get()}\t{self.CB}\n")
    if self.BhelPuri.get()!=0:
        self.txtarea.insert(END,f"BhelPuri\t\t {self.BhelPuri.get()}\t{self.BP}\n")
    if self.Pokara.get()!=0:
        self.txtarea.insert(END,f"Pokara\t\t {self.Pokara.get()}\t{self.PO}\n")
    # if self.atta.get()!=0:
    #     self.txtarea.insert(END,f"Atta\t\t {self.atta.get()}\t{self.at}\n")
    if self.pasta.get()!=0:
        self.txtarea.insert(END,f"Pasta\t\t {self.pasta.get()}\t{self.pa}\n")
    if self.Soup.get()!=0:
        self.txtarea.insert(END,f"Soup\t\t {self.Soup.get()}\t{self.Sp}\n")
    if self.DahiVada.get()!=0:
        self.txtarea.insert(END,f"DahiVada\t\t {self.DahiVada.get()}\t{self.DV}\n")
    if self.AlooTikkiChaa.get()!=0:
        self.txtarea.insert(END,f"AlooTikkiChaa\t\t {self.AlooTikkiChaa.get()}\t{self.ATc}\n")
    if self.dal.get()!=0:
        self.txtarea.insert(END,f"Daal\t\t {self.dal.get()}\t{self.da}\n")
    if self.PalakPaneer.get()!=0:
        self.txtarea.insert(END,f"PalakPaneer\t\t {self.PalakPaneer.get()}\t{self.PP}\n")
    if self.PaneerMasala.get()!=0:
        self.txtarea.insert(END,f"PaneerMasala\t\t {self.PaneerMasala.get()}\t{self.PM}\n")
    if self.BasmathiRice.get()!=0:
        self.txtarea.insert(END,f"BasmathiRice\t\t {self.BasmathiRice.get()}\t{self.BR}\n")
    if self.ButterChicken.get()!=0:
        self.txtarea.insert(END,f"ButterChicken\t\t {self.ButterChicken.get()}\t{self.BC}\n")
    if self.MasalaPapad.get()!=0:
        self.txtarea.insert(END,f"MasalaPapad\t\t {self.MasalaPapad.get()}\t{self.MP}\n")
    if self.VegetablePakora.get()!=0:
        self.txtarea.insert(END,f"VegetablePakora\t\t {self.VegetablePakora.get()}\t{self.VP}\n")
    if self.TomatoSoup.get()!=0:
        self.txtarea.insert(END,f"TomatoSoup\t\t {self.TomatoSoup.get()}\t{self.TS}\n")
    if self.ChickenTikka.get()!=0:
        self.txtarea.insert(END,f"ChickenTikka\t\t {self.ChickenTikka.get()}\t{self.CT}\n")

    self.txtarea.insert(END,f"------------------------------------\n")
    if self.a.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Snacks Tax : {self.a.get()}\n")
    if self.b.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Starter Tax : {self.b.get()}\n")
    if self.c.get()!="0.0 Rs":
        self.txtarea.insert(END,f"Total Main cours Tax : {self.c.get()}\n")
    self.txtarea.insert(END,f"Total Bill Amount : {self.total_all_bil}\n")
    self.txtarea.insert(END,f"------------------------------------\n")
def clear(self):
        self.txtarea.delete(1.0,END)
        self.Samosa.set(0)
        self.noodles.set(0)
        self.PaneerTikka.set(0)
        self.PavBhaji.set(0)
        self.CholeBhuture.set(0)
        self.BhelPuri.set(0)
        self.Pokara.set(0)
        self.atta.set(0)
        self.pasta.set(0)
        self.Soup.set(0)
        self.DahiVada.set(0)
        self.AlooTikkiChaa.set(0)
        self.dal.set(0)
        self.PalakPaneer.set(0)
        self.PaneerMasala.set(0)
        self.BasmathiRice.set(0)
        self.ButterChicken.set(0)
        self.MasalaPapad.set(0)
        self.VegetablePakora.set(0)
        self.TomatoSoup.set(0)
        self.ChickenTikka.set(0)
        self.total_sna.set(0)
        self.total_Sta.set(0)
        self.total_hyg.set(0)
        self.a.set(0)
        self.b.set(0)
        self.c.set(0)
        self.c_name.set(0)
        self.bill_no.set(0)
        self.bill_no.set(0)
        self.phone.set(0)
def exit1(self):
    self.root.destroy()

root=Tk()
obj=Bill_App(root)
root.mainloop()