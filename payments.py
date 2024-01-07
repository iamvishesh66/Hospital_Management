import time

from calculator import calculator
from pymysql import *
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview

from tkcalendar import DateEntry
from vei_pay import search_window


class bill_desk:

    def __init__(self, parent, a, b):

        self.pay_win1 = parent

        self.f1 = Frame(self.pay_win1, height=600, width=1000, bg="gray95")
        self.f1.place(x=a, y=b)
        self.f1.focus()

        self.f2 = Frame(self.pay_win1, height=40, width=1000, bg="white")
        self.f2.place(x=20, y=-7)

        title = Label(self.f2, text="MANAGE PAYMENTS", font=("algerian", 20, "bold", "underline"), fg="dodger blue3"
                      , bg="white").place(x=350, y=0)
        # Primary heads
        h1l = Label(self.f1, text="Payment Information:", background="gray95"
                   , font=("arial", 10, "bold", "italic", "underline")).place(x=10, y=5)
        h2l = Label(self.f1, text="Previous Payments:", background="gray95"
                    , font=("arial", 10, "bold", "italic", "underline")).place(x=10, y=200)
        # Secondary heads
        l1 = Label(self.f1, text="Amount", background="gray95",fg="gray", font=("arial", 12)).place(x=50, y=30)
        s1 = Label(self.f1, text="*", fg="red", bg="gray95", font=("arial", 12)).place(x=40,y=27)

        l2 = Label(self.f1, text="Refrence", background="gray95", fg="gray", font=("arial", 12)).place(x=40, y=60)

        l3 = Label(self.f1, text="Type", background="gray95", fg="gray", font=("arial", 12)).place(x=70, y=90)
        s2 = Label(self.f1, text="*", fg="red", bg="gray95", font=("arial", 12)).place(x=60, y=87)

        l4 = Label(self.f1, text="Status", background="gray95", fg="gray", font=("arial", 12)).place(x=60, y=120)
        s3 = Label(self.f1, text="*", fg="red", bg="gray95", font=("arial", 12)).place(x=50, y=117)

        l5 = Label(self.f1, text="Date", background="gray95", fg="gray", font=("arial", 12)).place(x=70, y=150)

        # parallel list
        l6 = Label(self.f1, text="Invoice", background="gray95", fg="gray", font=("arial", 12)).place(x=460, y=30)
        s4 = Label(self.f1, text="*", fg="red", bg="gray95", font=("arial", 12)).place(x=450, y=27)

        l7 = Label(self.f1, text="Assigned To", background="gray95", fg="gray", font=("arial", 12)).place(x=420, y=60)
        s5 = Label(self.f1, text="*", fg="red", bg="gray95", font=("arial", 12)).place(x=410, y=57)

        l8 = Label(self.f1, text="Patient Id", background="gray95", fg="gray", font=("arial", 12)).place(x=443, y=90)
        s6 = Label(self.f1, text="*", fg="red", bg="gray95", font=("arial", 12)).place(x=430, y=87)

        l9 = Label(self.f1, text="Paid By", background="gray95", fg="gray", font=("arial", 12)).place(x=453, y=120)

        l10 = Label(self.f1, text="Description", background="gray95", fg="gray", font=("arial", 12)).place(x=430, y=150)
        # images
        i1 = PhotoImage(file="cal.png").subsample(5,5)
        i2 = PhotoImage(file="search.png").subsample(32,32)

        # ons
        self.f1.bind("<Enter>", lambda e: self.showtext())

        # defining vars for display
        self.t1 = StringVar()
        self.t2 = StringVar()
        self.t3 = StringVar()

        # lets create some entry boxes
        self.e1 = Entry(self.f1, width=20, bg="white",fg="grey", font=("arial", 11, "italic"))
        self.e1.bind("<FocusIn>", lambda e: self.remtext("e1"))
        self.e1.bind("<FocusOut>", lambda e: self.deftext("e1"))
        self.e1.place(x=120, y=30)
        il = Label(self.f1,image=i1,bg="gray95")
        il.place(x=285, y=16)
        il.image = i1
        il.bind("<Button>", lambda e: calculator(self.pay_win1, 20, 40))

        self.e2 = Entry(self.f1, width=25, bg="white", fg="grey", font=("arial", 11, "italic"), state="disabled")
        self.e2.place(x=120, y=60)
        self.e2.config(textvariable=self.t3)
        t_stamp = time.time()
        self.t3.set("%d"%(t_stamp))


        self.v1 = StringVar()
        self.v1.set("Choose Payment Method")
        self.c1 = Combobox(self.f1,textvariable=self.v1, state="readonly", width=30,
                           value=("Cheque", "Credit Card", "Debit card", "Cash", "Demand Draft", "UPI",
                                  "NEFT", "RTGS"))
        self.c1.textvariable = self.v1
        self.c1.place(x=120, y=90)

        self.v2 = StringVar()
        self.v2.set("Choose Status")
        self.c2 = Combobox(self.f1, textvariable=self.v2, state="readonly", width=30,
                           value=("Paid","*Pending"))
        self.c2.textvariable = self.v2
        self.c2.place(x=120, y=120)

        self.d1 = DateEntry(self.f1, width=30, normalbackground="white"
                            , normalforeground="dodger blue3", background="dodger blue3", foreground="white")
        self.d1.place(x=120, y=150)
        # parallel entry box lists
        self.e3 = Entry(self.f1, width=25, bg="white", fg="grey", font=("arial", 11, "italic"), state="disabled")
        self.e3.place(x=525, y=30)
        # calling onstart func
        self.onstart()

        # list of patient names
        self.patient_names = []
        self.v3 = StringVar()
        self.v3.set("Enter Patient's Name")
        self.c3 = Combobox(self.f1, textvariable=self.v3, width=27,
                           value=self.patient_names)
        self.c3.textvariable = self.v3
        self.c3.bind("<<ComboboxSelected>>", lambda e:self.search_2())
        self.c3.place(x=525, y=60)
        b1 = Button(self.f1, relief="groove", image=i2, command=self.search_1)
        b1.place(x=710, y=60)
        b1.image = i2

        # patient ids list
        self.patient_ids = []
        self.v4 = StringVar()
        self.v4.set("Choose Patient's id")
        self.c4 = Combobox(self.f1, textvariable=self.v4,state="readonly", width=30,
                           value=self.patient_ids)
        self.c4.bind("<<ComboboxSelected>>", lambda e: self.search_3())
        self.c4.textvariable = self.v4
        self.c4.place(x=525, y=90)

        # cname list
        self.patient_cname = ["Anonymous"]
        self.v5 = StringVar()
        self.v5.set("Enter Payee's Name")
        self.c5 = Combobox(self.f1, textvariable=self.v5, width=30,
                           value=self.patient_cname)
        self.c5.textvariable = self.v5
        self.c5.place(x=525, y=120)

        self.e4 = Entry(self.f1, width=25, bg="white", fg="grey", font=("arial", 11, "italic"))
        self.e4.bind("<FocusIn>", lambda e: self.remtext("e4"))
        self.e4.bind("<FocusOut>", lambda e: self.deftext("e4"))
        self.e4.place(x=525, y=150)

        #btns for main part
        self.btn1 = Button(self.f1, font=("Palatino Linotype",12), bg="lawn green",bd=5
                      , text="Record Payment", command=self.save)
        self.btn1.place(x=800,y=10)

        self.btn2 = Button(self.f1, font=("Palatino Linotype",12),bd=5, text="Search Records..."
                      , bg="dodger blue")
        self.btn2.place(x=800,y=130)

        self.btn3 = Button(self.f1, font=("Palatino Linotype", 12), bg="red", bd=5
                      , text="Clear Records...", command=self.delete_all_records)
        self.btn3.place(x=800, y=70)

        btn4 = Button(self.f1, font=("arial", 12,"bold"), bd=5
                      , text="REFRESH", command=lambda :bill_desk(self.pay_win1,20,40)).place(x=20, y=500)


        # previous payments table
        self.f3 = Frame(self.f1, bg="gray95")
        sc_x = Scrollbar(self.f3, orient=HORIZONTAL)
        sc_y = Scrollbar(self.f3, orient=VERTICAL)
        self.table = Treeview(self.f3, columns=(
        "id", "name", "refrence", "date", "status", "paid", "type", "description","amount")
                              , xscrollcommand=sc_x.set, yscrollcommand=sc_y.set, height=10)

        sc_x.config(command=self.table.xview)
        sc_x.pack(side=BOTTOM, fill=X)
        sc_y.config(command=self.table.yview)
        sc_y.pack(side=RIGHT, fill=Y)

        self.table.heading("id", text="ID")
        self.table.heading("name", text="NAME")
        self.table.heading("refrence", text="REFRENCE")
        self.table.heading("date", text="DATE")
        self.table.heading("status", text="STATUS")
        self.table.heading("paid", text="PAID BY")
        self.table.heading("type", text="TYPE")
        self.table.heading("description", text="DESCRIPTION")
        self.table.heading("amount", text="AMOUNT")
        self.table["show"] = "headings"

        self.table.column("#0", stretch=NO, minwidth=0, width=0)
        # originals
        self.table.column("#1", stretch=NO, minwidth=30, width=30)
        self.table.column("#2", stretch=NO, minwidth=100, width=100)
        self.table.column("#3", stretch=NO, minwidth=120, width=120)
        self.table.column("#4", stretch=NO, minwidth=120, width=120)
        self.table.column("#5", stretch=NO, minwidth=120, width=120)
        self.table.column("#6", stretch=NO, minwidth=120, width=120)
        self.table.column("#7", stretch=NO, minwidth=100, width=100)
        self.table.column("#8", stretch=NO, minwidth=150, width=150)
        self.table.column("#9", stretch=NO, minwidth=120, width=120)

        self.table.pack()
        self.f3.place(x=0, y=230)
        # calling onstart func
        self.onstart_fetch()
        self.received = 0
        self.balance = 0
        self.total = self.received + self.balance
        self.sl1 = Label(self.f1,text="Recieved:\t\t" + "₹" + str(self.received),font=("arial",12),bg="gray95",
                    fg="green")
        self.sl1.place(x=750, y=470)
        self.sl2 = Label(self.f1, text="Balance:\t\t" + "₹" + str(self.balance), font=("arial", 12), bg="gray95",
                    fg="black")
        self.sl2.place(x=750, y=500)
        self.sl3 = Label(self.f1, text="Invoice Total:\t" + "₹" + str(self.total), font=("arial", 12), bg="gray95",
                    fg="red")
        self.sl3.place(x=750, y=530)
        # func calling to calculate
        self.fetch_1()
        self.fetch_2()


    def showtext(self):

        if not self.t1.get():
            self.f1.focus_set()
            self.t1.set("Enter Amount")
            self.e1.config(textvariable=self.t1, fg="grey")
        if self.t1.get() == "₹":
            self.f1.focus_set()
            self.t1.set("Enter Amount")
            self.e1.config(textvariable=self.t1, fg="grey")
        if not self.t2.get():
            self.f1.focus_set()
            self.t2.set("Enter Description")
            self.e4.config(textvariable=self.t2, fg="grey")
        if self.t2.get() == "0% Payment Done":
            self.f1.focus_set()
            self.t2.set("Enter Description")
            self.e4.config(textvariable=self.t2, fg="grey")

    def remtext(self, name):

        if name == "e1":
            if self.t1.get() == "Enter Amount":
                self.t1.set("₹")
            else:
                self.t1.set(self.e1.get())
            self.e1.config(textvariable=self.t1, fg="black", bg="yellow")
        elif name == "e4":
            if self.t2.get() == "Enter Description":
                self.t2.set("0% Payment Done")
            else:
                self.t2.set(self.e4.get())
            self.e4.config(textvariable=self.t2, fg="black", bg="yellow")

    def deftext(self, name):

        if name == "e1":
            self.e1.config(bg="white")
        elif name == "e4":
            self.e4.config(bg="white")

    def onstart(self):
        try:
            current_id = 0
            var = IntVar()
            d1 = connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc.execute("SELECT id FROM invoicecounter")
                f = dc.fetchall()
                for i in f:
                    for j in i:
                        current_id = j
                current_id += 1
                self.e3.config(textvariable=var, state="disabled")
                var.set("Invoice%d" % (current_id))
            except Exception:
                self.e3.config(textvariable=var, state="disabled")
                var.set("Invoice%d" % (1))
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.pay_win1)

    def onstart_fetch(self):
        try:
            d1 = connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc.execute("SELECT * FROM payments")
                result = dc.fetchall()
                self.table.delete(*self.table.get_children())
                for row in result:
                    self.table.insert("", END, values=row)
                self.btn2.bind("<Button>", lambda e: search_window(self.pay_win1, 20, 40))
                if not result:
                    messagebox.showinfo("INFO", "NO DATA FOUND", parent=self.pay_win1)
                    self.btn1.place(x=800, y=30)
                    self.btn2.destroy()
                    self.btn3.place(x=800, y=90)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in Query" + str(e), parent=self.pay_win1)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in connection" + str(e), parent=self.pay_win1)

    def search_1(self):
        try:
            d1 = connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc.execute("SELECT name FROM patient WHERE name like '%" + str(self.v3.get()) + "%'")
                result = dc.fetchall()
                self.patient_names.clear()
                for i in result:
                    for j in i:
                        self.patient_names.append(j)
                self.c3.config(value=self.patient_names)
                if not result:
                    messagebox.showinfo("INFO", "NO DATA FOUND", parent=self.pay_win1)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in Query" + str(e), parent=self.pay_win1)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in connection" + str(e), parent=self.pay_win1)

    def search_2(self):
        try:
            d1 = connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc.execute("SELECT id FROM patient WHERE name=%s", self.v3.get())
                self.patient_ids.clear()
                result = dc.fetchall()
                for i in result:
                    for j in i:
                        self.patient_ids.append(j)
                self.c4.config(value=self.patient_ids)
                if not result:
                    messagebox.showinfo("INFO", "NO DATA FOUND", parent=self.pay_win1)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in Query" + str(e), parent=self.pay_win1)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in connection" + str(e), parent=self.pay_win1)

    def search_3(self):
        try:
            d1 = connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc.execute("SELECT cname FROM patient WHERE id=%s", self.v4.get())
                self.patient_cname.clear()
                self.patient_cname.append("Anonymous")
                result = dc.fetchall()
                for i in result:
                        self.patient_cname.append(i)
                self.c5.config(value=self.patient_cname)
                if not result:
                    messagebox.showinfo("INFO", "NO DATA FOUND", parent=self.pay_win1)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in Query" + str(e), parent=self.pay_win1)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in connection" + str(e), parent=self.pay_win1)

    def save(self):
        try:
            d1 = connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                aba = self.e1.get()
                dc.execute("INSERT INTO payments VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.v4.get()
                           ,self.v3.get(),self.e2.get(),self.d1.get_date(),self.v2.get(),self.v5.get()
                           ,self.v1.get(),self.e4.get(),aba[1::1]))
                d1.commit()
                ama = self.e3.get()
                dc.execute("INSERT INTO invoicecounter VALUES(%s)",ama[-1])
                d1.commit()
                messagebox.showinfo("SAVE", "Data Saved Successfully", parent=self.pay_win1)
                bill_desk(self.pay_win1, 20, 40)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in Query" + str(e), parent=self.pay_win1)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in connection" + str(e), parent=self.pay_win1)

    def fetch_1(self):
        try:
            d1 = connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc.execute("SELECT amount FROM payments WHERE status='paid'")
                result = dc.fetchall()
                for i in result:
                    for j in i:
                        self.received+=int(j)
                self.total = self.received + self.balance
                self.sl1.config(text="Recieved:\t\t" + "₹" + str(self.received))
                self.sl3.config(text="Invoice Total:\t" + "₹" + str(self.total))
                if not result:
                    pass
            except Exception as e:
                messagebox.showerror("ERROR", "Error in Query" + str(e), parent=self.pay_win1)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in connection" + str(e), parent=self.pay_win1)

    def fetch_2(self):
        try:
            d1 = connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc.execute("SELECT amount FROM payments WHERE status='*pending'")
                result = dc.fetchall()
                for i in result:
                    for j in i:
                        self.balance+=int(j)
                self.total = self.received + self.balance
                self.sl2.config(text="Balance:\t\t" + "₹" + str(self.balance))
                self.sl3.config(text="Invoice Total:\t" + "₹" + str(self.total))
                if not result:
                    pass
            except Exception as e:
                messagebox.showerror("ERROR", "Error in Query" + str(e), parent=self.pay_win1)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in connection" + str(e), parent=self.pay_win1)

    def delete_all_records(self):
        a = messagebox.showwarning("ARE YOU SURE","Your All Payment Records Will Be Deleted\n\nYOU CANNOT UNDO THIS ACTION")
        if a == "ok" or a == "OK" or a == "Ok":
            try:
                d1 = Connect(host="localhost", user="root", password="", db="hospital")
                try:
                    dc = d1.cursor()
                    dc.execute("DELETE FROM payments")
                    d1.commit()
                    dc.execute("DELETE FROM invoicecounter")
                    d1.commit()
                    messagebox.showinfo("SAVE", "Data Deleted Successfully", parent=self.pay_win1)
                    bill_desk(self.pay_win1,20,40)
                except Exception as e:
                    messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.pay_win1)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.pay_win1)
        else:
            pass

def main():
    pass

if __name__ == '__main__':
    main()