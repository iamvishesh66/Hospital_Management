from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview, Combobox

from pymysql import *
class search_window:

    def __init__(self, parent, a, b):
        from payments import bill_desk

        self.pay_win2 = parent

        self.f1 = Frame(self.pay_win2, height=600, width=1000, bg="gray95")
        self.f1.place(x=a, y=b)
        self.f1.focus()

        self.f2 = Frame(self.pay_win2, height=40, width=1000, bg="white")
        self.f2.place(x=20, y=-7)

        title = Label(self.f2, text="SEARCH PAYMENT RECORDS", font=("algerian", 20, "bold", "underline"), fg="dodger blue3"
                      , bg="white").place(x=350, y=0)

        p = PhotoImage(file="search.png", master=self.pay_win2).subsample(4, 4)
        l = Label(self.pay_win2, image=p, bg="gray95")
        l.place(x=30, y=50)
        l.image = p

        self.f_1 = Frame(self.pay_win2)
        sc_x = Scrollbar(self.f_1, orient=HORIZONTAL)
        sc_y = Scrollbar(self.f_1, orient=VERTICAL)
        self.info = Treeview(self.f_1, columns=(
            "id", "name", "refrence", "date", "status", "paid", "type", "description", "amount")
                             , xscrollcommand=sc_x.set, yscrollcommand=sc_y.set, height=17)

        sc_x.config(command=self.info.xview)
        sc_x.pack(side=BOTTOM, fill=X)
        sc_y.config(command=self.info.yview)
        sc_y.pack(side=RIGHT, fill=Y)

        self.info.heading("id", text="ID")
        self.info.heading("name", text="NAME")
        self.info.heading("refrence", text="REFRENCE")
        self.info.heading("date", text="DATE")
        self.info.heading("status", text="STATUS")
        self.info.heading("paid", text="PAID BY")
        self.info.heading("type", text="TYPE")
        self.info.heading("description", text="DESCRIPTION")
        self.info.heading("amount", text="AMOUNT")
        self.info["show"] = "headings"

        self.info.column("#0", stretch=NO, minwidth=0, width=0)
        # originals
        self.info.column("#1", stretch=NO, minwidth=30, width=30)
        self.info.column("#2", stretch=NO, minwidth=100, width=100)
        self.info.column("#3", stretch=NO, minwidth=120, width=120)
        self.info.column("#4", stretch=NO, minwidth=120, width=120)
        self.info.column("#5", stretch=NO, minwidth=120, width=120)
        self.info.column("#6", stretch=NO, minwidth=120, width=120)
        self.info.column("#7", stretch=NO, minwidth=100, width=100)
        self.info.column("#8", stretch=NO, minwidth=150, width=150)
        self.info.column("#9", stretch=NO, minwidth=120, width=120)

        self.info.pack()
        self.f_1.place(x=20, y=190)
        # calling onstart func
        self.onstart()
        # defining main labels
        l_1 = Label(self.f1, text="Filters", font=("arial", 16), bg="gray95").place(x=200, y=5)
        # defining main entries
        self.t1 = StringVar()
        self.e1 = Entry(self.f1, bg="white", font=("arial", 14, "italic"))
        self.e1.bind("<FocusIn>", lambda e: self.remtext())
        self.e1.bind("<FocusOut>", lambda e: self.deftext())
        self.e1.place(x=600, y=5)
        self.f1.bind("<Enter>", lambda e: self.showtext())

        self.v1 = StringVar()
        self.v1.set("Sort By")
        self.c_1 = Combobox(self.f1, value=("Reference", "Name", "Ascending Order", "Descending Order")
                            , textvariable=self.v1, font=("arial", 14), state="readonly")
        self.c_1.textvariable = self.v1
        self.c_1.place(x=300, y=5)

        # Let's create some buttons
        btn1 = Button(self.f1, text="Apply", font=("arial", 12, "bold"), bd=3, command=self.applyer)
        btn1.place(x=300, y=50)

        btn2 = Button(self.f1, text="Remove", font=("arial", 12, "bold"), bd=3, command=self.onstart)
        btn2.place(x=430, y=50)

        btn3 = Button(self.f1, text="Search", font=("arial", 11, "bold"), bd=3, command=self.searcher)
        btn3.place(x=850, y=0)

        btn4 = Button(self.f1, text="Go Back", font=("arial", 11, "bold"), bd=3
                      , command=lambda: bill_desk(self.pay_win2, 20, 40), fg="red")
        btn4.place(x=910, y=115)

        btn4 = Button(self.f1, text="Refresh", font=("arial", 11, "bold"), bd=3
                      , command=lambda: search_window(self.pay_win2, 20, 40), fg="green")
        btn4.place(x=800, y=115)

    def showtext(self):
        if not self.t1.get():
            self.f1.focus_set()
            self.t1.set("Search in Name")
            self.e1.config(textvariable=self.t1, fg="grey")

    def remtext(self):
        if self.t1.get() == "Search in Name":
            self.t1.set("")
        else:
            self.t1.set(self.e1.get())
        self.e1.config(textvariable=self.t1, fg="black", bg="yellow")

    def deftext(self):
        self.e1.config(bg="white")


    def onstart(self):
        try:
            d1 = connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc.execute("SELECT * FROM payments")
                result = dc.fetchall()
                self.info.delete(*self.info.get_children())
                for row in result:
                    self.info.insert("", END, values=row)
                if not result:
                    self.pay_win2.destroy()
                    messagebox.showinfo("INFO", "NO DATA FOUND", parent=self.pay_win2)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.pay_win2)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.pay_win2)

    def applyer(self):
        try:
            d1 = Connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                if self.v1.get() == "Name":
                    dc.execute("SELECT * FROM payments")
                elif self.v1.get() == "Reference":
                    dc.execute("SELECT * FROM payments ORDER BY refrence")
                elif self.v1.get() == "Ascending Order":
                    dc.execute("SELECT * FROM payments ORDER BY id ASC")
                elif self.v1.get() == "Descending Order":
                    dc.execute("SELECT * FROM payments ORDER BY id DESC")
                result = dc.fetchall()
                self.info.delete(*self.info.get_children())
                for row in result:
                    self.info.insert("", END, values=row)
                if not result:
                    messagebox.showinfo("INFO", "NO DATA FOUND", parent=self.pay_win2)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.pay_win2)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.pay_win2)

    def searcher(self):
        try:
            d1 = Connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc.execute("SELECT * FROM payments WHERE name LIKE '%"+str(self.e1.get())+"%'")
                result = dc.fetchall()
                self.info.delete(*self.info.get_children())
                for row in result:
                    self.info.insert("", END, values=row)
                if not result:
                    messagebox.showinfo("INFO", "NO DATA FOUND", parent=self.pay_win2)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.pay_win2)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.pay_win2)