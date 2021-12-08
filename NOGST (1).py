from tkinter import*
import math,random,os 
from tkinter import messagebox
class Bill_App:

   def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing software")
        bg_color="#074463",
        title=Label(self.root,text="NON GST INVOICE",bd=10,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        F1=LabelFrame(self.root,text="custmer details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        self.soap=IntVar()
        self.face_cream=IntVar()
        self.spray=IntVar()

        self.rice=IntVar()
        self.food_oil=IntVar()
        self.dal=IntVar()
        self.turmeric=IntVar()

        self.sprite=IntVar()
        self.Maaza=IntVar()
        self.limca=IntVar()
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cool_drink_price=StringVar()

        self.C_name=StringVar()
        self.C_phone=StringVar()

        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(X))

        self.search_bill=StringVar()



        cname_lbl=Label(F1,text="customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.C_name,font="arial 10",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        cphn_lbl=Label(F1,text="Customer mobile no",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.C_phone,font="arial 10",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,pady=20,padx=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.bill_no,font="arial 10",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=6,pady=10)

        bill_btn=Button(F1,text="search",width=15,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="COSMETICS",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=170,width=325,height=380)

        bath_soap_lbl=Label(F2,text="bath soap",bg=bg_color,fg="green",font=("times new roman",16,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_soap_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        face_cream_lbl=Label(F2,text="face cream",bg=bg_color,fg="green",font=("times new roman",16,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)


        hair_s_lbl=Label(F2,text="hair spray",bg=bg_color,fg="green",font=("times new roman",16,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="groceries",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=180,width=325,height=380)

        g1_lbl=Label(F3,text="rice",bg=bg_color,fg="green",font=("times new roman",16,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        g2_lbl=Label(F3,text="food oil",bg=bg_color,fg="green",font=("times new roman",16,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        g3_lbl=Label(F3,text="dal",bg=bg_color,fg="green",font=("times new roman",16,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=10,textvariable=self.dal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        g4_lbl=Label(F3,text="turmeric",bg=bg_color,fg="green",font=("times new roman",16,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.turmeric,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="COol drink",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=670,y=180,width=325,height=380)

        c1_lbl=Label(F4,text="sprite",bg=bg_color,fg="green",font=("times new roman",16,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)
        
        c2_lbl=Label(F4,text="Maaza",bg=bg_color,fg="green",font=("times new roman",16,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=10,textvariable=self.Maaza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        c3_lbl=Label(F4,text="limca",bg=bg_color,fg="green",font=("times new roman",16,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)


        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=350,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="BILL MENU",font=("times of new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)

        m1_lbl=Label(F6,text=" total cosmetic price",bg=bg_color,fg="green",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total grocery price",bg=bg_color,fg="green",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=10,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="total cool drink price ",bg=bg_color,fg="green",font=("times new roman",16,"bold")).grid(row=3,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cool_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=585,height=105)


        total_btn=Button(btn_F,text="Total",bg="cadetblue",fg="white",bd=2,pady=10,width=5,font="arial 15 bold").grid(row=1,column=1,padx=5,pady=5)
        Gbill_btn=Button(btn_F,text="Generate bill",bg="cadetblue",fg="white",bd=2,pady=10,width=10,font="arial 15 bold").grid(row=1,column=2,padx=5,pady=5)
        clear_btn=Button(btn_F,text="Clear",bg="cadetblue",fg="white",bd=2,pady=10,width=5,font="arial 15 bold").grid(row=1,column=3,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Exit",bg="cadetblue",fg="white",bd=2,pady=10,width=5,font="arial 15 bold").grid(row=1,column=4,padx=5,pady=5)
        
def total(self):
   self.c_s_p=self.soap.get()*40
   self.c_fc_p=self.face_cream.get()*60
   self.c_hs_p=self.hair_spray.get()*150

   self.total_cosmetic_price=float(
                self.c_s_p+
                self.c_fc_p+
                self.c_hs_p
                            )
                         
   self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
   self.c_tax=round((self.total_cosmetic_price*0.05),2)
   self.cosmetic_tax.set("Rs. "+str(self.c_tax))


   self.g_r_p=self.rice.get()*40

   self.g_f_p=self.food_oil.get()*120
   self.g_d_p=self.dal.get()*180
   self.g_t_p=self.turmeric.get()*70

   self.total_grocery_price=float(
                                self.g_r_p+
                                self.g_f_p+
                                self.g_d_p+
                                self.g_t_p
                               ) 
   self.grocery_price.set("Rs. "+str(self.total_grocery_price))
   self.g_tax=round((self.total_grocery_price*0.01),2)
   self.grocery_tax.set("Rs. "+str(self.g_tax))####################3


   self.d_s_p=self.sprite.get()*75        
   self.d_m_p=self.Maaza.get()*80
   self.d_f_p=self.fruty.get()*80
   self.total_drink_price=float(
                                (self.d_sprite.get()*40)+
                                self.d_m_p+
                                self.d_f_p
   
                               )
   self.cool_drink_price.set("Rs. "+str(self.total_drink_price)) 
   self.d_tax=round((self.total_cooldrink_price*0.05),2)                           

   self.Total_bill=float(  self.total_cosmetic_price+
                            self.total_grocery_price+
                            self.total_drink_price+
                            self.c_tax+
                            self.g_tax+
                            self.d_tax
                               )
def welcome_bill (self):
       self.txtarea.delete('1.0',END)   
       self.txtarea.insert(END,"\twelcome webcode retail")
       self.txtarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
       self.txtarea.insert(END,f"\n Custmer name:{self.c_name.get()}")
       self.txtarea.insert(END,f"\n phone Number:{self.c_phone.get()}")
       self.txtarea.insert(END,f"\n =================================")
       self.txtarea.insert(END,f"\n products\t\tqty\tprice")
       self.txtarea.insert(END,f"\n =================================")


def bill_area(self):
       if self.c_name.get()==""or self.c_phn.get()==" ":
            messagebox.showerror("Error","Customer details are must")
       elif self.total_cosmetic_price.get()==" Rs. 0.0" or self.total_grocery_price.get()==" Rs. 0.0" or  self.total_cool_drink_price.get()==" Rs. 0.0": 
        messagebox.showerror("Error","no product purchased" )
       else:
         self.welcome_bill() 

         self.welcome_bill()
         if self.soap.get()!=0:
                   self.txtarea.insert(END,f"\n bath soap\t\t{self.soap.get()}\t\t{self.c_s_p}")

         if self.face_cream.get()!=0:
                   self.txtarea.insert(END,f"\n face_cream\t\t{self.soap.get()}\t\t{self.c_fc_p}")
         if self.hair_gell.get()!=0:
                   self.txtarea.insert(END,f"\n hair_gell\t\t{self.soap.get()}\t\t{self.c_hg_p}")

         if self.rice.get()!=0:
                  self.txtarea.insert(END,f"\n rice \t\t{self.rice.get()}\t\t{self.g_r_p}")
         if self.oil_food.get()!=0:
                    self.txtarea.insert(END,f"\n food_oil\t\t{self.soap.get()}\t\t{self.g_of_p}")
       if self.turmeric.get()!=0:
                   self.txtarea.insert(END,f"\n turmeric \t\t{self.soap.get()}\t\t{self.g_of_p}")
       if self.sprite.get()!=0:
               self.txtarea.insert(END,f"\n sprite \t\t{self.soap.get()}\t\t{self.d_s_p}")
       if self.Maaza.get()!=0:
                self.txtarea.insert(END,f"\n Maaza \t\t{self.soap.get()}\t\t{self.d_m_p}")
       if self.pulpy.get()!=0:
                self.txtarea.insert(END,f"\n pulpy \t\t{self.soap.get()}\t\t{self.d_p_p}")
                self.txtarea.insert(END,f"\n =================================")
       if self.cosmetic_tax.get()!="Rs. 0.0":
               self.txtarea.insert(END,f"\n cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")

       if self.Grocery_tax.get()!="Rs. 0.0":
              self.txtarea.insert(END,f"\n Grocery Tax\t\t\t{self.Grocery_tax.get()}")

       if self.cool_drink_tax.get()!="Rs. 0.0":
             self.txtarea.insert(END,f"\n cool drink Tax\t\t\t{self.cool_drink__tax.get()}")
  


             self.txtarea.insert(END,f"\n Total bill \t\t\t Rs.{self.total_bill})")
             self.txtarea.insert(END,f"\n =================================")

root=Tk()
obj =Bill_App(root)
root.mainloop()
