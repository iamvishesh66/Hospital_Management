from pymysql import *
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename
from PIL import Image
from PIL import ImageTk
import time

class add_doc:

    def __init__(self,parent,a,b):

        self.doc_win1 = parent

        self.filename = ""
        
        self.f1 = Frame(self.doc_win1, height=600, width=1000, bg="gray95")
        self.f1.place(x=a, y=b)
        self.f1.focus()

        self.f2 = Frame(self.doc_win1, height=40, width=1000, bg="white")
        self.f2.place(x=20, y=-7)

        title = Label(self.f2, text="ADD DOCTOR", font=("algerian", 20, "bold", "underline"), fg="dodger blue3"
                      , bg="white").place(x=350, y=0)
        # label to display image
        self.imglabel = Label(self.f1, borderwidth=2, text="", width=195, height=200)
        self.imglabel.place(x=0, y=0)
        # lets create photo adder:
        self.canvas2 = Canvas(self.f1, height=160, width=170, bg="gray95", highlightbackground="gray95")
        self.canvas2.place(x=0, y=0)
        self.canvas2.bind("<Button>", lambda e: self.imageupload())
        self.canvas2.create_oval(155, 155, 12, 12, fill="white", outline="black")

        self.img1 = PhotoImage(file="add_img.png").subsample(6,6)

        self.canvas2.create_image(70,60,image=self.img1)
        self.canvas2.create_text(85,120,text="Click To Add\n    Image", font=("arial",14,"italic","bold"))

        l1 = Label(self.f1, text="Id", background="gray95", font=("arial",16)).place(x=200, y=5)
        l2 = Label(self.f1, text="Name", background="gray95", font=("arial",16)).place(x=200, y=70)
        l3 = Label(self.f1, text="Gender", background="gray95", font=("arial",16)).place(x=200, y=140)
        l4 = Label(self.f1, text="Phone Number", background="gray95", font=("arial",16)).place(x=0, y=210)
        l5 = Label(self.f1, text="Address", background="gray95", font=("arial",16)).place(x=0, y=280)
        l6 = Label(self.f1, text="Speciality", background="gray95", font=("arial",16)).place(x=0, y=370)
        l7 = Label(self.f1, text="Wing", background="gray95", font=("arial",16)).place(x=0, y=430)

        self.t1 = StringVar()
        self.t2 = StringVar()
        self.t3 = StringVar()

        self.f1.bind("<Enter>", lambda e: self.showtext())

        self.e1=Entry(self.f1, width=50, bg="white", font=("arial",14,"italic"))
        self.e1.bind("<FocusIn>", lambda e: self.remtext("e1"))
        self.e1.bind("<FocusOut>", lambda e: self.deftext("e1"))
        self.e1.bind("<Down>",lambda e:self.lower("e1"))
        self.e1.bind("<Up>", lambda e: self.up("e1"))
        self.e1.place(x=400, y=5)
        # calling onstart func
        self.onstart()

        self.e2=Entry(self.f1, width=50, bg="white", font=("arial",14,"italic"))
        self.e2.bind("<FocusIn>", lambda e: self.remtext("e2"))
        self.e2.bind("<FocusOut>", lambda e: self.deftext("e2"))
        self.e2.bind("<Down>",lambda e:self.lower("e2"))
        self.e2.bind("<Up>",lambda e:self.up("e2"))
        self.e2.place(x=400, y=70)

        self.e3=Entry(self.f1, width=50, bg="white", font=("arial",14,"italic"))
        self.e3.bind("<FocusIn>", lambda e: self.remtext("e3"))
        self.e3.bind("<FocusOut>", lambda e: self.deftext("e3"))
        self.e3.bind("<Down>", lambda e: self.lower("e3"))
        self.e3.bind("<Up>", lambda e: self.up("e3"))
        self.e3.place(x=200, y=210)

        self.e4 = Text(self.f1,width=20,height=3, bg="white", font=("arial",14,"italic"))
        self.e4.bind("<FocusIn>", lambda e: self.remtext("e4"))
        self.e4.bind("<FocusOut>", lambda e: self.deftext("e4"))
        self.e4.bind("<Down>", lambda e: self.lower("e4"))
        self.e4.bind("<Up>", lambda e: self.up("e4"))
        self.e4.place(x=200, y=280)

        self.v1=StringVar()
        self.v1.set(" ")

        self.r1=Radiobutton(self.f1, text="Male", variable=self.v1, value="Male", font=("arial",14))
        self.r1.place(x=400, y=140)
        self.r2=Radiobutton(self.f1, text="Female", variable=self.v1, value="Female", font=("arial",14))
        self.r2.place(x=600, y=140)

        self.v2=StringVar()
        self.v2.set("Choose Speciality")

        self.c1=Combobox(self.f1,
                         value=("Psychiatrists","Eye","Heart","Skin","Ent","Physician",
                         "Dental","Ortho","Gyno","Uro","Gystro","Neuro"),
                         textvariable=self.v2, state="readonly", font=("arial",14))
        self.c1.place(x=200, y=370)

        self.v3 = StringVar()
        self.v3.set("Choose Ward")

        self.c2 = Combobox(self.f1, value=("Opd", "Surgery Ward",
                                            "Medicine Ward", "Ortho Ward", "Gyno Ward","Pedetrician Ward",
                                            "Psychiatrists Ward"), textvariable=self.v3, state="readonly",
                                            font=("arial",14))
        self.c2.place(x=200, y=430)

        self.btn1=Button(self.f1, text="SAVE", command=self.savedata, font=("arial",14,"bold"), bd=5)
        self.btn1.place(x=700, y=500)

        self.btn2 = Button(self.f1, text="REFRESH", command=lambda: add_doc(self.doc_win1, 20, 40),
                           font=("arial", 14, "bold"), bd=5)
        self.btn2.place(x=850, y=500)

        self.f1.mainloop()

    def showtext(self):

        # if not self.t1.get():
        #     self.f1.focus_set()
        #     self.t1.set("Enter Unique Id")
        #     self.e1.config(textvariable=self.t1, fg="grey")
        if not self.t2.get():
            self.f1.focus_set()
            self.t2.set("Enter Doctor's Name")
            self.e2.config(textvariable=self.t2, fg="grey")
        if not self.t3.get():
            self.f1.focus_set()
            self.t3.set("Enter Doctor's Phone Number")
            self.e3.config(textvariable=self.t3, fg="grey")

    def remtext(self, name):

        # if name == "e1":
        #     if self.t1.get() == "Enter Unique Id":
        #         self.t1.set("")
        #     else:
        #         self.t1.set(self.e1.get())
        #     self.e1.config(textvariable=self.t1, fg="black", bg="yellow")
        if name == "e2":
            if self.t2.get() == "Enter Doctor's Name":
                self.t2.set("Dr.")
            else:
                self.t2.set(self.e2.get())
            self.e2.config(textvariable=self.t2, fg="black", bg="yellow")
        elif name == "e3":
            if self.t3.get() == "Enter Doctor's Phone Number":
                self.t3.set("")
            else:
                self.t3.set(self.e3.get())
            self.e3.config(textvariable=self.t3, fg="black", bg="yellow")
        elif name == "e4":
            self.e4.config( fg="black", bg="yellow")

    def deftext(self, name):

        if name == "e1":
            self.e1.config(bg="white")
        elif name == "e2":
            self.e2.config(bg="white")
        elif name == "e3":
            self.e3.config(bg="white")
        elif name == "e4":
            self.e4.config(bg="white")

    def lower(self,name):

        if name == "e1":
            self.e2.focus_set()
        elif name == "e2":
            self.e3.focus_set()
        elif name == "e3":
            self.e4.focus_set()
        elif name == "e4":
            self.e1.focus_set()

    def up(self,name):

        if name == "e1":
            self.e4.focus_set()
        elif name == "e2":
            self.e1.focus_set()
        elif name == "e3":
            self.e2.focus_set()
        elif name == "e4":
            self.e3.focus_set()

    def imageupload(self):
        try:
            self.filename = askopenfilename(filetypes=[("Picture Files","*.png")])
            img = Image.open(self.filename)
            self.finalname = str(int(time.time()))
            img.save("docimages//" + self.finalname + ".png")
            tk_image = ImageTk.PhotoImage(img)
            a = tk_image.height()
            b = tk_image.width()
            tkimage = PhotoImage(file="docimages//" + self.finalname + ".png")
            if a > 1000 and b > 1000:
                p1 = tkimage.subsample(15,15)
                self.imglabel.config(image=p1)
                self.imglabel.image = p1
            elif (a > 1000 and b < 1000) or (a < 1000 and b > 1000):
                p2 = tkimage.subsample(10, 10)
                self.imglabel.config(image=p2)
                self.imglabel.image = p2
            elif (a > 500 and a < 1000) and (b > 500 and b < 1000):
                p3 = tkimage.subsample(5, 5)
                self.imglabel.config(image=p3)
                self.imglabel.image = p3
            elif a < 500 and b < 500:
                p4 = tkimage.subsample(2,2)
                self.imglabel.config(image=p4)
                self.imglabel.image = p4
            else:
                self.imglabel.config(image=tkimage)
                self.imglabel.image = tkimage
            btn = Button(self.f1,text="Change",command=self.imageupload, font=("arial",12,"bold"), bd=4, bg="orange")
            btn.place(x=0,y=0)

            self.canvas2.destroy()
        except:
            pass


    def savedata(self):
        try:
            d1=Connect(host="localhost", user="root", password="", db="hospital")
            try:
                # backup image inserting for no image inserted
                if self.filename == "":
                    img = Image.open("C:/Users/vishesh/PycharmProjects/Project/Hospital_Management/default_img1.png")
                    self.finalname = str(int(time.time()))
                    img.save("docimages//"+ self.finalname + ".png")

                dc=d1.cursor()
                dc.execute("insert into doctor values(%s,%s,%s,%s,%s,%s,%s,%s)",
                           (self.e1.get(),self.e2.get(),self.v1.get(),self.e3.get(),
                            self.e4.get("1.0",END),self.v2.get(),self.v3.get(), self.finalname+".png"))

                d1.commit()
                messagebox.showinfo("SAVE","Data Saved Successfully", parent=self.doc_win1)
                add_doc(self.doc_win1,20,40)
            except Exception as e:
                messagebox.showerror("ERROR","Error in creation"+str(e), parent=self.doc_win1)
        except Exception as e:
            messagebox.showerror("ERROR","Error in Connection"+str(e), parent=self.doc_win1)

    def onstart(self):
        try:
            current_id = 0
            var = IntVar()
            d1 = connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc.execute("SELECT id FROM doctor")
                f = dc.fetchall()
                for i in f:
                    for j in i:
                        current_id = j
                current_id += 1
                self.e1.config(textvariable=var, state="disabled")
                var.set(current_id)
            except Exception:
                self.e1.config(textvariable=var, state="disabled")
                var.set(1)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.doc_win1)



def main():
    pass

if __name__ == '__main__':
    main()