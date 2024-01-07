import os
from tkinter import *
from tkinter.filedialog import askopenfilename
import time
from PIL import ImageTk,Image
from pymysql import *
from tkinter.ttk import Combobox, Treeview
from tkinter import messagebox


class upd_pat:

    def __init__(self, parent, a, b):

        self.update = parent

        self.f1 = Frame(self.update, height=600, width=1005, bg="gray95")
        self.f1.place(x=a, y=b)
        self.f1.focus()

        self.f2 = Frame(self.update, height=40, width=1000, bg="white")
        self.f2.place(x=20, y=-7)

        title = Label(self.f2, text="UPDATE PATIENT", font=("algerian", 20, "bold", "underline"), fg="dodger blue3"
                      , bg="white").place(x=350, y=0)
        # label to display image
        self.imglabel = Label(self.f1, borderwidth=2, text="", width=195, height=200)
        self.imglabel.place(x=800, y=300)
        # lets create photo adder:
        self.canvas2 = Canvas(self.f1, height=160, width=170, bg="gray95", highlightbackground="gray95")
        self.canvas2.place(x=800, y=300)
        self.canvas2.bind("<Button>", lambda e: self.imageupload())
        self.canvas2.create_oval(155, 155, 12, 12, fill="white", outline="black")

        self.img1 = PhotoImage(file="add_img.png").subsample(6, 6)

        self.canvas2.create_image(70, 60, image=self.img1)
        self.canvas2.create_text(85, 120, text="Click To Change\n    Image", font=("arial", 12, "italic", "bold"))

        self.canvas1 = Canvas(self.f1, bg="gray95", height=120, width=350)
        self.canvas1.create_rectangle(0, 0, 350, 120, outline="black")
        self.canvas1.place(x=1, y=1)

        self.v_1 = StringVar()
        self.v_1.set("Search By")
        self.c_1 = Combobox(self.canvas1, values=("ID", "NAME", "COMPANION'S NAME", "ROOM ALLOTTED"), textvariable=self.v_1,
                            state="readonly"
                            , font=("arial", 14, "italic"))
        self.c_1.place(x=2, y=5)
        self.c_1.bind("<<ComboboxSelected>>", lambda e: self.entryboxcreater())

        self.f3 = Frame(self.f1, bg="gray95")
        sc_x = Scrollbar(self.f3, orient=HORIZONTAL)
        sc_y = Scrollbar(self.f3, orient=VERTICAL)
        self.table = Treeview(self.f3, columns=("id", "name", "gender", "phonenumber", "address", "roomalloted", "cname","cphno")
                              , xscrollcommand=sc_x.set, yscrollcommand=sc_y.set)

        sc_x.config(command=self.table.xview)
        sc_x.pack(side=BOTTOM, fill=X)
        sc_y.config(command=self.table.yview)
        sc_y.pack(side=RIGHT, fill=Y)

        self.table.heading("id", text="ID")
        self.table.heading("name", text="NAME")
        self.table.heading("gender", text="GENDER")
        self.table.heading("phonenumber", text="PHONE NUMBER")
        self.table.heading("address", text="ADDRESS")
        self.table.heading("roomalloted", text="ROOM ALLOTTED")
        self.table.heading("cname", text="COMPANION'S NAME")
        self.table.heading("cphno", text="COMPANION'S PHONE NUMBER")
        self.table["show"] = "headings"

        self.table.column("#0", stretch=NO, minwidth=0, width=0)
        self.table.column("#1", stretch=NO, minwidth=20, width=20)
        self.table.column("#2", stretch=NO, minwidth=50, width=50)
        self.table.column("#3", stretch=NO, minwidth=60, width=60)
        self.table.column("#4", stretch=NO, minwidth=100, width=100)
        self.table.column("#5", stretch=NO, minwidth=60, width=60)
        self.table.column("#6", stretch=NO, minwidth=103, width=103)
        self.table.column("#7", stretch=NO, minwidth=127, width=127)
        self.table.column("#8", stretch=NO, minwidth=135, width=135)

        self.table.bind("<ButtonRelease>", lambda e: self.inserter())

        self.table.pack()
        self.f3.place(x=330, y=0)

        # Let's get some things straight
        l1 = Label(self.f1, text="Id", background="gray95", font=("arial", 16)).place(x=2, y=130)
        l2 = Label(self.f1, text="Name", background="gray95", font=("arial", 16)).place(x=2, y=180)
        l3 = Label(self.f1, text="Gender", background="gray95", font=("arial", 16)).place(x=2, y=230)
        l4 = Label(self.f1, text="Phone Number", background="gray95", font=("arial", 16)).place(x=2, y=280)
        l5 = Label(self.f1, text="Address", background="gray95", font=("arial", 16)).place(x=2, y=330)
        l6 = Label(self.f1, text="Room Allotted", background="gray95", font=("arial", 16)).place(x=2, y=420)
        l7 = Label(self.f1, text="Companion's Name", background="gray95", font=("arial", 16)).place(x=2, y=460)
        l8 = Label(self.f1, text="Companion's Phone Number", background="gray95", font=("arial", 16)).place(x=2, y=510)

        self.t1 = StringVar()
        self.t2 = StringVar()
        self.t3 = StringVar()
        self.t4 = StringVar()
        self.t5 = StringVar()
        self.t6 = StringVar()

        self.f1.bind("<Enter>", lambda e: self.showtext())

        self.e1 = Entry(self.f1, width=20, bg="white", font=("arial", 14, "italic"))
        self.e1.bind("<FocusIn>", lambda e: self.remtext("e1"))
        self.e1.bind("<FocusOut>", lambda e: self.deftext("e1"))
        self.e1.bind("<Down>", lambda e: self.lower("e1"))
        self.e1.bind("<Up>", lambda e: self.up("e1"))
        self.e1.place(x=100, y=130)

        self.e2 = Entry(self.f1, width=20, bg="white", font=("arial", 14, "italic"))
        self.e2.bind("<FocusIn>", lambda e: self.remtext("e2"))
        self.e2.bind("<FocusOut>", lambda e: self.deftext("e2"))
        self.e2.bind("<Down>", lambda e: self.lower("e2"))
        self.e2.bind("<Up>", lambda e: self.up("e2"))
        self.e2.place(x=100, y=180)

        self.e3 = Entry(self.f1, width=50, bg="white", font=("arial", 14, "italic"))
        self.e3.bind("<FocusIn>", lambda e: self.remtext("e3"))
        self.e3.bind("<FocusOut>", lambda e: self.deftext("e3"))
        self.e3.bind("<Down>", lambda e: self.lower("e3"))
        self.e3.bind("<Up>", lambda e: self.up("e3"))
        self.e3.place(x=200, y=280)

        self.e4 = Text(self.f1, width=20, height=3, bg="white", font=("arial", 14, "italic"))
        self.e4.bind("<FocusIn>", lambda e: self.remtext("e4"))
        self.e4.bind("<FocusOut>", lambda e: self.deftext("e4"))
        self.e4.bind("<Down>", lambda e: self.lower("e4"))
        self.e4.bind("<Up>", lambda e: self.up("e4"))
        self.e4.place(x=200, y=330)

        self.e5 = Entry(self.f1, width=50, bg="white", font=("arial", 14, "italic"))
        self.e5.bind("<FocusIn>", lambda e: self.remtext("e5"))
        self.e5.bind("<FocusOut>", lambda e: self.deftext("e5"))
        self.e5.bind("<Down>", lambda e: self.lower("e5"))
        self.e5.bind("<Up>", lambda e: self.up("e5"))
        self.e5.place(x=200, y=420)

        self.e6 = Entry(self.f1, width=50, bg="white", font=("arial", 14, "italic"))
        self.e6.bind("<FocusIn>", lambda e: self.remtext("e6"))
        self.e6.bind("<FocusOut>", lambda e: self.deftext("e6"))
        self.e6.bind("<Down>", lambda e: self.lower("e6"))
        self.e6.bind("<Up>", lambda e: self.up("e6"))
        self.e6.place(x=200, y=460)

        self.e7 = Entry(self.f1, width=43, bg="white", font=("arial", 14, "italic"))
        self.e7.bind("<FocusIn>", lambda e: self.remtext("e7"))
        self.e7.bind("<FocusOut>", lambda e: self.deftext("e7"))
        self.e7.bind("<Down>", lambda e: self.lower("e7"))
        self.e7.bind("<Up>", lambda e: self.up("e7"))
        self.e7.place(x=280, y=510)

        self.v1 = StringVar()
        self.v1.set(" ")

        self.r1 = Radiobutton(self.f1, text="Male", variable=self.v1, value="Male", font=("arial", 14))
        self.r1.place(x=100, y=230)
        self.r2 = Radiobutton(self.f1, text="Female", variable=self.v1, value="Female", font=("arial", 14))
        self.r2.place(x=200, y=230)

        self.btn1 = Button(self.f1, text="UPDATE", command=self.updatedata, font=("arial", 14, "bold"), bd=5)
        self.btn1.place(x=760, y=500)

        self.btn2 = Button(self.f1, text="REFRESH", command=lambda: upd_pat(self.update, 20, 40),
                           font=("arial", 14, "bold"), bd=5)
        self.btn2.place(x=880, y=500)

    def entryboxcreater(self):

        self.t_1 = StringVar()
        self.t_2 = StringVar()
        self.t_3 = StringVar()
        self.t_4 = StringVar()

        self.f1.bind("<Enter>", lambda e: self.showtext1())
        self.e_1 = Entry(self.canvas1, width=20, bg="white", font=("arial", 14, "italic"))
        self.e_2 = Entry(self.canvas1, width=20, bg="white", font=("arial", 14, "italic"))
        self.e_3 = Entry(self.canvas1, width=20, bg="white", font=("arial", 14, "italic"))
        self.e_4 = Entry(self.canvas1, width=16, bg="white", font=("arial", 14, "italic"))

        self.v_2 = StringVar()
        l1 = Label(self.canvas1, font=("arial", 16), textvariable=self.v_2)
        l1.place(x=2, y=40)

        if self.v_1.get() == "Search By":
            pass

        elif self.v_1.get() == "ID":
            self.v_2.set("Id                      ")
            self.e_1 = Entry(self.canvas1, width=20, bg="white", font=("arial", 14, "italic"))
            self.e_1.bind("<FocusIn>", lambda e: self.remtext1("e1"))
            self.e_1.bind("<FocusOut>", lambda e: self.deftext1("e1"))
            self.e_1.place(x=100, y=40)
            self.btn1 = Button(self.canvas1, text="Search", font=("arial", 12, "bold"), bd=3, command=self.searcher)
            self.btn1.place(x=100, y=80)
            self.btn2 = Button(self.canvas1, text="Fetch", font=("arial", 12, "bold"), bd=3, command=self.fetcher)
            self.btn2.place(x=200, y=80)
            self.f1.bind("<Enter>", lambda e: self.showtext1())
        elif self.v_1.get() == "NAME":
            self.v_2.set("Name                ")
            self.e_2 = Entry(self.canvas1, width=20, bg="white", font=("arial", 14, "italic"))
            self.e_2.bind("<FocusIn>", lambda e: self.remtext1("e2"))
            self.e_2.bind("<FocusOut>", lambda e: self.deftext1("e2"))
            self.e_2.place(x=100, y=40)
            self.btn1 = Button(self.canvas1, text="Search", font=("arial", 12, "bold"), bd=3, command=self.searcher)
            self.btn1.place(x=100, y=80)
            self.btn2 = Button(self.canvas1, text="Fetch", font=("arial", 12, "bold"), bd=3, command=self.fetcher)
            self.btn2.place(x=200, y=80)
            self.f1.bind("<Enter>", lambda e: self.showtext1())
        elif self.v_1.get() == "COMPANION'S NAME":
            self.v_2.set("C's Name     ")
            self.e_3 = Entry(self.canvas1, width=20, bg="white", font=("arial", 14, "italic"))
            self.e_3.bind("<FocusIn>", lambda e: self.remtext1("e3"))
            self.e_3.bind("<FocusOut>", lambda e: self.deftext1("e3"))
            self.e_3.place(x=100, y=40)
            self.btn1 = Button(self.canvas1, text="Search", font=("arial", 12, "bold"), bd=3, command=self.searcher)
            self.btn1.place(x=100, y=80)
            self.btn2 = Button(self.canvas1, text="Fetch", font=("arial", 12, "bold"), bd=3, command=self.fetcher)
            self.btn2.place(x=200, y=80)
            self.f1.bind("<Enter>", lambda e: self.showtext1())
        elif self.v_1.get() == "ROOM ALLOTTED":
            self.v_2.set("Room Allotted           ")
            self.e_4 = Entry(self.canvas1, width=16, bg="white", font=("arial", 14, "italic"))
            self.e_4.bind("<FocusIn>", lambda e: self.remtext1("e4"))
            self.e_4.bind("<FocusOut>", lambda e: self.deftext1("e4"))
            self.e_4.place(x=143, y=40)
            self.btn1 = Button(self.canvas1, text="Search", font=("arial", 12, "bold"), bd=3, command=self.searcher)
            self.btn1.place(x=100, y=80)
            self.btn2 = Button(self.canvas1, text="Fetch", font=("arial", 12, "bold"), bd=3, command=self.fetcher)
            self.btn2.place(x=200, y=80)
            self.f1.bind("<Enter>", lambda e: self.showtext1())

    def showtext1(self):
        if not self.t_1.get():
            self.f1.focus_set()
            self.t_1.set("Enter Unique Id")
            self.e_1.config(textvariable=self.t_1, fg="grey")
        if not self.t_2.get():
            self.f1.focus_set()
            self.t_2.set("Enter Patient's Name")
            self.e_2.config(textvariable=self.t_2, fg="grey")
        if not self.t_3.get():
            self.f1.focus_set()
            self.t_3.set("Enter Companion's Name")
            self.e_3.config(textvariable=self.t_3, fg="grey")
        if not self.t_4.get():
            self.f1.focus_set()
            self.t_4.set("Enter Room Allotted")
            self.e_4.config(textvariable=self.t_4, fg="grey")

    def remtext1(self, name):

        if name == "e1":
            if self.t_1.get() == "Enter Unique Id":
                self.t_1.set("")
            else:
                self.t_1.set(self.e_1.get())
            self.e_1.config(textvariable=self.t_1, fg="black", bg="yellow")
        elif name == "e2":
            if self.t_2.get() == "Enter Patient's Name":
                self.t_2.set("")
            else:
                self.t_2.set(self.e_2.get())
            self.e_2.config(textvariable=self.t_2, fg="black", bg="yellow")
        elif name == "e3":
            if self.t_3.get() == "Enter Companion's Name":
                self.t_3.set("")
            else:
                self.t_3.set(self.e_3.get())
            self.e_3.config(textvariable=self.t_3, fg="black", bg="yellow")
        elif name == "e4":
            if self.t_4.get() == "Enter Room Allotted":
                self.t_4.set("")
            else:
                self.t_4.set(self.e_4.get())
            self.e_4.config(textvariable=self.t_4, fg="black", bg="yellow")

    def deftext1(self, name):

        if name == "e1":
            self.e_1.config(bg="white")
        elif name == "e2":
            self.e_2.config(bg="white")
        elif name == "e3":
            self.e_3.config(bg="white")
        elif name == "e4":
            self.e_4.config(bg="white")

    def showtext(self):
        if not self.t1.get():
            self.f1.focus_set()
            self.t1.set("Enter Unique Id")
            self.e1.config(textvariable=self.t1, fg="grey")
        if not self.t2.get():
            self.f1.focus_set()
            self.t2.set("Enter Patient's Name")
            self.e2.config(textvariable=self.t2, fg="grey")
        if not self.t3.get():
            self.f1.focus_set()
            self.t3.set("Enter Patient's Phone Number")
            self.e3.config(textvariable=self.t3, fg="grey")
        if not self.t4.get():
            self.f1.focus_set()
            self.t4.set("Allot Room to Patient")
            self.e5.config(textvariable=self.t4, fg="grey")
        if not self.t5.get():
            self.f1.focus_set()
            self.t5.set("Enter Companion's Name")
            self.e6.config(textvariable=self.t5, fg="grey")
        if not self.t6.get():
            self.f1.focus_set()
            self.t6.set("Enter Companion's Phone Number")
            self.e7.config(textvariable=self.t6, fg="grey")

    def remtext(self, name):
        if name == "e1":
            if self.t1.get() == "Enter Unique Id":
                self.t1.set("")
            else:
                self.t1.set(self.e1.get())
            self.e1.config(textvariable=self.t1, fg="black", bg="yellow")
        elif name == "e2":
            if self.t2.get() == "Enter Patient's Name":
                self.t2.set("")
            else:
                self.t2.set(self.e2.get())
            self.e2.config(textvariable=self.t2, fg="black", bg="yellow")
        elif name == "e3":
            if self.t3.get() == "Enter Patient's Phone Number":
                self.t3.set("")
            else:
                self.t3.set(self.e3.get())
            self.e3.config(textvariable=self.t3, fg="black", bg="yellow")
        elif name == "e4":
            self.e4.config(fg="black", bg="yellow")
        elif name == "e5":
            if self.t4.get() == "Allot Room to Patient":
                self.t4.set("")
            else:
                self.t4.set(self.e5.get())
            self.e5.config(textvariable=self.t4, fg="black", bg="yellow")
        elif name == "e6":
            if self.t5.get() == "Enter Companion's Name":
                self.t5.set("")
            else:
                self.t5.set(self.e6.get())
            self.e6.config(textvariable=self.t5, fg="black", bg="yellow")
        elif name == "e7":
            if self.t6.get() == "Enter Companion's Phone Number":
                self.t6.set("")
            else:
                self.t6.set(self.e7.get())
            self.e7.config(textvariable=self.t6, fg="black", bg="yellow")

    def deftext(self, name):
        if name == "e1":
            self.e1.config(bg="white")
        elif name == "e2":
            self.e2.config(bg="white")
        elif name == "e3":
            self.e3.config(bg="white")
        elif name == "e4":
            self.e4.config(bg="white")
        elif name == "e5":
            self.e5.config(bg="white")
        elif name == "e6":
            self.e6.config(bg="white")
        elif name == "e7":
            self.e7.config(bg="white")

    def lower(self, name):
        if name == "e1":
            self.e2.focus_set()
        elif name == "e2":
            self.e3.focus_set()
        elif name == "e3":
            self.e5.focus_set()
        elif name == "e5":
            self.e6.focus_set()
        elif name == "e6":
            self.e7.focus_set()
        elif name == "e7":
            self.e1.focus_set()


    def up(self, name):
        if name == "e1":
            self.e7.focus_set()
        elif name == "e2":
            self.e1.focus_set()
        elif name == "e3":
            self.e2.focus_set()
        elif name == "e5":
            self.e3.focus_set()
        elif name == "e6":
            self.e5.focus_set()
        elif name == "e7":
            self.e6.focus_set()

    def searcher(self):
        try:
            d1 = Connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                if self.v_1.get() == "ID":
                    dc.execute("SELECT * FROM patient WHERE id=%s", (self.e_1.get()))
                elif self.v_1.get() == "NAME":
                    dc.execute("SELECT * FROM patient WHERE name like '%" + str(self.e_2.get()) + "%'")
                elif self.v_1.get() == "COMPANION'S NAME":
                    dc.execute("SELECT * FROM patient WHERE cname like '%" + str(self.e_3.get()) + "%'")
                elif self.v_1.get() == "ROOM ALLOTTED":
                    dc.execute("SELECT * FROM patient WHERE roomalloted like '%" + str(self.e_4.get()) + "%'")
                self.result = dc.fetchall()
                self.table.delete(*self.table.get_children())
                for row in self.result:
                    self.table.insert("", END, values=row)
                if not self.result:
                    messagebox.showinfo("INFO", "NO DATA FOUND", parent=self.update)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.update)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.update)

    def inserter(self):
        currentItem = self.table.focus()
        contents = self.table.item(currentItem)
        selectedRow = contents['values']
        id = selectedRow[0]
        name = selectedRow[1]
        companion = selectedRow[7]
        roomalloted = selectedRow[5]
        try:
            d1 = connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                if self.v_1.get() == "ID":
                    dc.execute("select * from patient where id=%s", id)
                elif self.v_1.get() == "NAME":
                    dc.execute("select * from patient where name=%s", name)
                elif self.v_1.get() == "COMPANION'S NAME":
                    dc.execute("select * from patient where cname=%s", companion)
                elif self.v_1.get() == "ROOM ALLOTTED":
                    dc.execute("select * from patient where roomalloted=%s", roomalloted)
                result = dc.fetchall()
                try:
                    for row in result:
                        self.e1.delete(0, END)
                        self.e1.config(fg="black")
                        self.e1.insert(0, row[0])

                        self.e2.delete(0, END)
                        self.e2.config(fg="black")
                        self.e2.insert(0, row[1])

                        self.v1.set(row[2])

                        self.e3.delete(0, END)
                        self.e3.config(fg="black")
                        self.e3.insert(0, row[3])

                        self.e4.delete("1.0", END)
                        self.e4.insert("1.0", row[4])

                        self.e5.delete(0, END)
                        self.e5.config(fg="black")
                        self.e5.insert(0, row[5])

                        self.e6.delete(0, END)
                        self.e6.config(fg="black")
                        self.e6.insert(0, row[6])

                        self.e7.delete(0, END)
                        self.e7.config(fg="black")
                        self.e7.insert(0, row[7])


                except Exception:
                    pass

            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.update)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.update)
        try:
            d1 = Connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                if self.v_1.get() == "ID":
                    dc.execute("SELECT img FROM patient WHERE id=%s", (self.e_1.get()))
                elif self.v_1.get() == "NAME":
                    dc.execute("SELECT img FROM patient WHERE name like '%" + str(self.e_2.get()) + "%'")
                elif self.v_1.get() == "SPECIALITY":
                    dc.execute("SELECT img FROM patient WHERE speciality like '%" + str(self.e_3.get()) + "%'")
                elif self.v_1.get() == "WING":
                    dc.execute("SELECT img FROM patient WHERE wing like '%" + str(self.e_4.get()) + "%'")
                res = dc.fetchone()
                for i in res:
                    self.del_img = i
                tkimage = PhotoImage(file="patimages//" + str(self.del_img))
                a = tkimage.height()
                b = tkimage.width()
                if a > 1000 and b > 1000:
                    p1 = tkimage.subsample(15, 15)
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
                    p4 = tkimage.subsample(2, 2)
                    self.imglabel.config(image=p4)
                    self.imglabel.image = p4
                else:
                    self.imglabel.config(image=tkimage)
                    self.imglabel.image = tkimage
                btn = Button(self.f1, text="Change", command=self.imageupload, font=("arial", 12, "bold"), bd=4,
                             bg="orange")
                btn.place(x=800, y=300)
                self.canvas2.destroy()
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.update)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.update)

    def fetcher(self):
        try:
            d1 = Connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                if self.v_1.get() == "ID":
                    dc.execute("SELECT * FROM patient WHERE id=%s", (self.e_1.get()))
                elif self.v_1.get() == "NAME":
                    dc.execute("SELECT * FROM patient WHERE name like '%" + str(self.e_2.get()) + "%'")
                elif self.v_1.get() == "COMPANION'S NAME":
                    dc.execute("SELECT * FROM patient WHERE cname like '%" + str(self.e_3.get()) + "%'")
                elif self.v_1.get() == "ROOM ALLOTTED":
                    dc.execute("SELECT * FROM patient WHERE roomalloted like '%" + str(self.e_4.get()) + "%'")
                result = dc.fetchall()
                self.table.delete(*self.table.get_children())
                for row in result:
                    self.table.insert("", END, values=row)
                for row in result:
                    self.e1.delete(0, END)
                    self.e1.config(fg="black")
                    self.e1.insert(0, row[0])

                    self.e2.delete(0, END)
                    self.e2.config(fg="black")
                    self.e2.insert(0, row[1])

                    self.v1.set(row[2])

                    self.e3.delete(0, END)
                    self.e3.config(fg="black")
                    self.e3.insert(0, row[3])

                    self.e4.delete("1.0", END)
                    self.e4.insert("1.0", row[4])

                    self.e5.delete(0, END)
                    self.e5.config(fg="black")
                    self.e5.insert(0, row[5])

                    self.e6.delete(0, END)
                    self.e6.config(fg="black")
                    self.e6.insert(0, row[6])

                    self.e7.delete(0, END)
                    self.e7.config(fg="black")
                    self.e7.insert(0, row[7])

                if not result:
                    messagebox.showinfo("INFO", "NO DATA FOUND", parent=self.update)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.update)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.update)
        try:
            d1 = Connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                if self.v_1.get() == "ID":
                    dc.execute("SELECT img FROM patient WHERE id=%s", (self.e_1.get()))
                elif self.v_1.get() == "NAME":
                    dc.execute("SELECT img FROM patient WHERE name like '%" + str(self.e_2.get()) + "%'")
                elif self.v_1.get() == "SPECIALITY":
                    dc.execute("SELECT img FROM patient WHERE speciality like '%" + str(self.e_3.get()) + "%'")
                elif self.v_1.get() == "WING":
                    dc.execute("SELECT img FROM patient WHERE wing like '%" + str(self.e_4.get()) + "%'")
                res = dc.fetchone()
                for i in res:
                    self.del_img = i
                tkimage = PhotoImage(file="patimages//" + str(self.del_img))
                a = tkimage.height()
                b = tkimage.width()
                if a > 1000 and b > 1000:
                    p1 = tkimage.subsample(15, 15)
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
                    p4 = tkimage.subsample(2, 2)
                    self.imglabel.config(image=p4)
                    self.imglabel.image = p4
                else:
                    self.imglabel.config(image=tkimage)
                    self.imglabel.image = tkimage
                btn = Button(self.f1, text="Change", command=self.imageupload, font=("arial", 12, "bold"), bd=4,
                             bg="orange")
                btn.place(x=800, y=300)
                self.canvas2.destroy()
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.update)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.update)

    def updatedata(self):
        try:
            path = os.path.join("patimages//", self.del_img)
            os.remove(path)
            d1 = Connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc.execute(
                    "UPDATE patient SET id=%s, name=%s, gender=%s, phonenumber=%s, address=%s, roomalloted=%s, cname=%s, cphno=%s, img=%s WHERE id=%s",
                    (self.e1.get(), self.e2.get(), self.v1.get(), self.e3.get(),
                     self.e4.get("1.0", END), self.e5.get(), self.e6.get(), self.e7.get(),self.finalname + ".png", self.e1.get()))
                d1.commit()
                messagebox.showinfo("SAVE", "Data Updated Successfully", parent=self.update)
                upd_pat(self.update, 20, 40)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.update)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.update)

    def imageupload(self):
        try:
            self.filename = askopenfilename(filetypes=[("Picture Files","*.png")])
            img = Image.open(self.filename)
            self.finalname = str(int(time.time()))
            img.save("patimages//" + self.finalname + ".png")
            tk_image = ImageTk.PhotoImage(img)
            a = tk_image.height()
            b = tk_image.width()
            tkimage = PhotoImage(file="patimages//" + self.finalname + ".png")
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
            btn.place(x=800,y=300)

            self.canvas2.destroy()
        except:
            pass


def main():
    pass


if __name__ == '__main__':
    main()