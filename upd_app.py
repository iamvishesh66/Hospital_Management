import time
from tkinter import *
from pymysql import *
from tkinter.ttk import Combobox, Treeview
from tkinter import messagebox

from tkcalendar import DateEntry


class upd_app:

    def __init__(self, parent, a, b):

        # revisiting list
        self.revisit = []

        # starting

        self.update = parent

        self.f1 = Frame(self.update, height=600, width=1005, bg="gray95")
        self.f1.place(x=a, y=b)
        self.f1.focus()

        self.f2 = Frame(self.update, height=40, width=1000, bg="white")
        self.f2.place(x=20, y=-7)

        title = Label(self.f2, text="UPDATE APPOINTMENT", font=("algerian", 20, "bold", "underline"), fg="dodger blue3"
                      , bg="white").place(x=350, y=0)

        self.canvas1 = Canvas(self.f1, bg="gray95", height=120, width=350)
        self.canvas1.create_rectangle(0, 0, 350, 120, outline="black")
        self.canvas1.place(x=1, y=1)

        self.v_1 = StringVar()
        self.v_1.set("Search By")
        self.c_1 = Combobox(self.canvas1, values=("ID", "NAME", "DOCTOR", "DATE"), textvariable=self.v_1,
                            state="readonly"
                            , font=("arial", 14, "italic"))
        self.c_1.place(x=2, y=5)
        self.c_1.bind("<<ComboboxSelected>>", self.entryboxcreater)

        self.f3 = Frame(self.f1, bg="gray95")
        sc_x = Scrollbar(self.f3, orient=HORIZONTAL)
        sc_y = Scrollbar(self.f3, orient=VERTICAL)
        self.table = Treeview(self.f3, columns=("id", "name", "gender", "phonenumber", "reasonforvisit", "doctorprovided", "date","time")
                              , xscrollcommand=sc_x.set, yscrollcommand=sc_y.set)

        sc_x.config(command=self.table.xview)
        sc_x.pack(side=BOTTOM, fill=X)
        sc_y.config(command=self.table.yview)
        sc_y.pack(side=RIGHT, fill=Y)

        self.table.heading("id", text="ID")
        self.table.heading("name", text="NAME")
        self.table.heading("gender", text="GENDER")
        self.table.heading("phonenumber", text="PHONE NUMBER")
        self.table.heading("reasonforvisit", text="REASON FOR VISIT")
        self.table.heading("doctorprovided", text="DOCTOR PROVIDED")
        self.table.heading("date", text="DATE")
        self.table.heading("time", text="TIME")
        self.table["show"] = "headings"

        self.table.column("#0", stretch=NO, minwidth=0, width=0)
        self.table.column("#1", stretch=NO, minwidth=22, width=22)
        self.table.column("#2", stretch=NO, minwidth=60, width=60)
        self.table.column("#3", stretch=NO, minwidth=60, width=60)
        self.table.column("#4", stretch=NO, minwidth=100, width=100)
        self.table.column("#5", stretch=NO, minwidth=110, width=110)
        self.table.column("#6", stretch=NO, minwidth=115, width=115)
        self.table.column("#7", stretch=NO, minwidth=70, width=70)
        self.table.column("#8", stretch=NO, minwidth=115, width=115)

        self.table.bind("<ButtonRelease>", lambda e: self.inserter())

        self.table.pack()
        self.f3.place(x=330, y=0)

        # Let's get some things straight
        l1 = Label(self.f1, text="Id", background="gray95", font=("arial", 16)).place(x=2, y=130)
        l2 = Label(self.f1, text="Name", background="gray95", font=("arial", 16)).place(x=2, y=180)
        l3 = Label(self.f1, text="Gender", background="gray95", font=("arial", 16)).place(x=2, y=230)
        l4 = Label(self.f1, text="Phone Number", background="gray95", font=("arial", 16)).place(x=2, y=280)
        l5 = Label(self.f1, text="Reason For Visit", background="gray95", font=("arial", 16)).place(x=2, y=370)
        l6 = Label(self.f1, text="Date", background="gray95", font=("arial", 16)).place(x=2, y=330)
        l7 = Label(self.f1, text="Time", background="gray95", font=("arial", 16)).place(x=2, y=460)
        l8 = Label(self.f1, text="Doctor Provided", background="gray95", font=("arial", 16)).place(x=2, y=510)

        self.t1 = StringVar()
        self.t2 = StringVar()
        self.t3 = StringVar()
        self.t4 = StringVar()
        self.t5 = StringVar()

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
        self.e4.place(x=200, y=370)

        self.e5 = DateEntry(self.f1, width=50, font=("arial", 12, "italic"), normalbackground="white"
                            , normalforeground="dodger blue3", background="dodger blue3", foreground="white")
        self.e5.bind("<Down>", lambda e: self.lower("e5"))
        self.e5.bind("<Up>", lambda e: self.up("e5"))
        self.e5.place(x=200, y=330)

        self.e6 = Entry(self.f1, width=50, bg="white", font=("arial", 14, "italic"))
        self.e6.bind("<FocusIn>", lambda e: self.remtext("e6"))
        self.e6.bind("<FocusOut>", lambda e: self.deftext("e6"))
        self.e6.bind("<Down>", lambda e: self.lower("e6"))
        self.e6.bind("<Up>", lambda e: self.up("e6"))
        self.e6.place(x=200, y=460)

        self.v1 = StringVar()
        self.v1.set(" ")

        self.r1 = Radiobutton(self.f1, text="Male", variable=self.v1, value="Male", font=("arial", 14))
        self.r1.place(x=200, y=230)
        self.r2 = Radiobutton(self.f1, text="Female", variable=self.v1, value="Female", font=("arial", 14))
        self.r2.place(x=300, y=230)

        self.v2 = StringVar()
        self.v2.set("Choose Doctor")

        self.doc_list = []
        self.fetching("c1")

        self.c1 = Combobox(self.f1, value=self.doc_list, textvariable=self.v2, state="readonly",
                           font=("arial", 14, "italic"))
        self.c1.place(x=200, y=510)

        self.btn1 = Button(self.f1, text="UPDATE", command=self.updatedata, font=("arial", 14, "bold"), bd=5)
        self.btn1.place(x=700, y=500)

        self.btn2 = Button(self.f1, text="REFRESH", command=lambda: upd_app(self.update, 20, 40),
                           font=("arial", 14, "bold"), bd=5)
        self.btn2.place(x=850, y=500)

    def entryboxcreater(self,e):

        self.t_1 = StringVar()
        self.t_2 = StringVar()
        self.t_3 = StringVar()

        self.f1.bind("<Enter>", lambda e: self.showtext1())
        # sorting
        self.e_1 = Entry(self.canvas1, width=20, bg="white", font=("arial", 14, "italic"))
        self.e_2 = Entry(self.canvas1, width=20, bg="white", font=("arial", 14, "italic"))
        self.v = StringVar()
        self.v.set("Choose Doctor")
        self.doc_list1 = []
        self.fetching("c2")
        self.e_3 = Combobox(self.canvas1, value=self.doc_list, textvariable=self.v, state="readonly",
                            font=("arial", 14, "italic"))
        self.e_4 = DateEntry(self.f1, width=20, font=("arial", 14, "italic"), normalbackground="white"
                             , normalforeground="dodger blue3", background="dodger blue3", foreground="white")
        # sorting ends
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
            if self.e_4:
                self.e_4.destroy()
                self.e_3.destroy()
            if self.e_3:
                self.e_3.destroy()
                self.e_4.destroy()
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
            if self.e_4:
                self.e_4.destroy()
                self.e_3.destroy()
            if self.e_3:
                self.e_3.destroy()
                self.e_4.destroy()
        elif self.v_1.get() == "DOCTOR":
            self.v_2.set("Doctor     ")
            self.v = StringVar()
            self.v.set("Choose Doctor")
            self.doc_list1 = []
            self.fetching("c2")
            self.e_3 = Combobox(self.canvas1, value=self.doc_list, textvariable=self.v, state="readonly",
                                font=("arial", 14, "italic"))
            self.e_3.place(x=80, y=40)
            self.btn1 = Button(self.canvas1, text="Search", font=("arial", 12, "bold"), bd=3, command=self.searcher)
            self.btn1.place(x=100, y=80)
            self.btn2 = Button(self.canvas1, text="Fetch", font=("arial", 12, "bold"), bd=3, command=self.fetcher)
            self.btn2.place(x=200, y=80)
            self.f1.bind("<Enter>", lambda e: self.showtext1())
            if self.e_4:
                self.e_4.destroy()
        elif self.v_1.get() == "DATE":
            self.v_2.set("Date           ")
            self.e_4 = DateEntry(self.f1, width=20, font=("arial", 14,"italic"), normalbackground="white"
                            , normalforeground="dodger blue3", background="dodger blue3", foreground="white")
            self.e_4.bind("<FocusIn>", lambda e: self.remtext1("e4"))
            self.e_4.bind("<FocusOut>", lambda e: self.deftext1("e4"))
            self.e_4.place(x=80, y=40)
            self.btn1 = Button(self.canvas1, text="Search", font=("arial", 12, "bold"), bd=3, command=self.searcher)
            self.btn1.place(x=100, y=80)
            self.btn2 = Button(self.canvas1, text="Fetch", font=("arial", 12, "bold"), bd=3, command=self.fetcher)
            self.btn2.place(x=200, y=80)
            self.f1.bind("<Enter>", lambda e: self.showtext1())
            if self.e_3:
                self.e_3.destroy()

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
            # self.t_3.set("Select Date")
            # self.e_4.config(textvariable=self.t_3)

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

    def deftext1(self, name):

        if name == "e1":
            self.e_1.config(bg="white")
        elif name == "e2":
            self.e_2.config(bg="white")

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
            self.t4.set("Select Date")
            self.e5.config(textvariable=self.t4)
        if not self.t5.get():
            self.f1.focus_set()
            self.t5.set(str(time.ctime()))
            self.e6.config(textvariable=self.t5, fg="grey")

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
            # self.e4.config(fg="black", bg="yellow")
            pass
        elif name == "e6":
            if self.t5.get() == str(time.ctime()):
                self.t5.set("")
            else:
                self.t5.set(self.e6.get())
            self.e6.config(textvariable=self.t5, fg="black", bg="yellow")

    def deftext(self, name):
        if name == "e1":
            self.e1.config(bg="white")
        elif name == "e2":
            self.e2.config(bg="white")
        elif name == "e3":
            self.e3.config(bg="white")
        elif name == "e4":
            # self.e4.config(bg="white")
            pass
        elif name == "e6":
            self.e6.config(bg="white")

    def lower(self, name):
        if name == "e1":
            self.e2.focus_set()
        elif name == "e2":
            self.e3.focus_set()
        elif name == "e3":
            self.e4.focus_set()
        elif name == "e4":
            self.e5.focus_set()
        elif name == "e5":
            self.e6.focus_set()
        elif name == "e6":
            self.e1.focus_set()

    def up(self, name):
        if name == "e1":
            self.e6.focus_set()
        elif name == "e2":
            self.e1.focus_set()
        elif name == "e3":
            self.e2.focus_set()
        elif name == "e4":
            self.e3.focus_set()
        elif name == "e5":
            self.e4.focus_set()
        elif name == "e6":
            self.e5.focus_set()

    def searcher(self):
        try:
            d1 = Connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                if self.v_1.get() == "ID":
                    dc.execute("SELECT * FROM appointment WHERE id=%s", (self.e_1.get()))
                elif self.v_1.get() == "NAME":
                    dc.execute("SELECT * FROM appointment WHERE name like '%" + str(self.e_2.get()) + "%'")
                elif self.v_1.get() == "DOCTOR":
                    dc.execute("SELECT * FROM appointment WHERE doctorprovided=%s", (self.v.get()))
                elif self.v_1.get() == "DATE":
                    dc.execute("SELECT * FROM appointment WHERE date=%s", (self.e_4.get_date()))
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
        doctor = selectedRow[6]
        date = selectedRow[7]
        try:
            d1 = connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                if self.v_1.get() == "ID":
                    dc.execute("select * from appointment where id=%s", id)
                elif self.v_1.get() == "NAME":
                    dc.execute("select * from appointment where name=%s", name)
                elif self.v_1.get() == "DOCTOR":
                    dc.execute("select * from appointment where doctorprovided=%s", doctor)
                elif self.v_1.get() == "DATE":
                    dc.execute("select * from appointment where date=%s", date)
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
                        self.e5.insert(0, row[6])

                        self.v2.set(row[5])

                        self.e6.delete(0, END)
                        self.e6.config(fg="black")
                        self.e6.insert(0, row[7])


                except Exception:
                    pass

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
                    dc.execute("SELECT * FROM appointment WHERE id=%s", (self.e_1.get()))
                elif self.v_1.get() == "NAME":
                    dc.execute("SELECT * FROM appointment WHERE name like '%" + str(self.e_2.get()) + "%'")
                elif self.v_1.get() == "DOCTOR":
                    dc.execute("SELECT * FROM appointment WHERE doctorprovided=%s", (self.v.get()))
                elif self.v_1.get() == "DATE":
                    dc.execute("SELECT * FROM appointment WHERE date=%s", (self.e_4.get_date()))
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
                    self.e5.insert(0, row[6])

                    self.v2.set(row[5])

                    self.e6.delete(0, END)
                    self.e6.config(fg="black")
                    self.e6.insert(0, row[7])

                if not result:
                    messagebox.showinfo("INFO", "NO DATA FOUND", parent=self.update)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.update)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.update)

    def fetching(self,e):
        try:
            d1 = Connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc.execute("SELECT name FROM doctor")
                f = dc.fetchall()
                if e == "c1":
                    for i in f:
                        for j in i:
                            self.doc_list.append(j)
                elif e == "c2":
                    for i in f:
                        for j in i:
                            self.doc_list1.append(j)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.update)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.update)
    
    def updatedata(self):
        a = messagebox.askquestion("REVISIT","IF Rescheduling For Patient's Next Visit\nClick YES")
        if a == "yes":
            try:
                d1 = Connect(host="localhost", user="root", password="", db="hospital")
                try:
                    dc = d1.cursor()
                    dc1 = d1.cursor()
                    dc2 = d1.cursor()
                    dc3 = d1.cursor()
                    dc2.execute("SELECT list FROM revisit WHERE id=%s", self.e1.get())
                    data = dc2.fetchone()
                    for x in data:
                        self.revisit.append(x)
                    self.revisit.append(self.e5.get())
                    print(self.revisit)
                    dc3.execute("DELETE FROM revisit WHERE id=%s",self.e1.get())
                    d1.commit()
                    dc.execute(
                        "UPDATE appointment SET id=%s, name=%s, gender=%s, phonenumber=%s,"
                        " reasonforvisit=%s, doctorprovided=%s, date=%s, time=%s WHERE id=%s",
                        (self.e1.get(), self.e2.get(), self.v1.get(), self.e3.get(),
                         self.e4.get("1.0", END), self.v2.get(), self.e5.get_date(), self.e6.get(), self.e1.get()))
                    d1.commit()
                    dc1.execute("INSERT INTO revisit VALUES(%s,%s,%s)",(self.e1.get(),self.e2.get(), str(self.revisit)))
                    d1.commit()
                    messagebox.showinfo("SAVE", "Data Updated Successfully", parent=self.update)
                    upd_app(self.update, 20, 40)
                except Exception as e:
                    messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.update)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.update)
        elif a == "no":
            try:
                d1 = Connect(host="localhost", user="root", password="", db="hospital")
                try:
                    dc = d1.cursor()
                    dc.execute(
                        "UPDATE appointment SET id=%s, name=%s, gender=%s, phonenumber=%s, reasonforvisit=%s, doctorprovided=%s, date=%s, time=%s WHERE id=%s",
                        (self.e1.get(), self.e2.get(), self.v1.get(), self.e3.get(),
                         self.e4.get("1.0", END), self.v2.get(), self.e5.get_date(), self.e6.get(), self.e1.get()))
                    d1.commit()
                    messagebox.showinfo("SAVE", "Data Updated Successfully", parent=self.update)
                    upd_app(self.update, 20, 40)
                except Exception as e:
                    messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.update)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.update)


def main():
    pass


if __name__ == '__main__':
    main()