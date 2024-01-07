import os

from pymysql import *
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import  Treeview


class del_nur:

    def __init__(self, parent, a, b):

        self.doc_win1 = parent

        self.f1 = Frame(self.doc_win1, height=600, width=1000, bg="gray95")
        self.f1.place(x=a, y=b)
        self.f1.focus()

        self.f2 = Frame(self.doc_win1, height=40, width=1000, bg="white")
        self.f2.place(x=20, y=-7)

        title = Label(self.f2, text="REMOVE NURSE", font=("algerian", 20, "bold", "underline"), fg="dodger blue3"
                      , bg="white").place(x=350, y=0)

        l1 = Label(self.f1, text="Id Of Nurse", background="gray95", font=("arial", 16)).place(x=0, y=5)
        l2 = Label(self.f1, text="Name", bg="gray95", font=("arial", 16)).place(x=0, y=50)
        l3 = Label(self.f1, text="OR", bg="gray95", font=("arial", 14)).place(x=400, y=26)

        self.t1 = StringVar()
        self.t2 = StringVar()

        self.f1.bind("<Enter>", lambda e: self.showtext())

        self.e1 = Entry(self.f1, width=50, bg="white", font=("arial", 14, "italic"))
        self.e1.bind("<FocusIn>", lambda e: self.remtext("e1"))
        self.e1.bind("<FocusOut>", lambda e: self.deftext("e1"))
        self.e1.bind("<Up>", lambda e: self.prev("e1"))
        self.e1.bind("<Down>", lambda e: self.next("e1"))
        self.e1.place(x=200, y=5)

        self.e2 = Entry(self.f1, width=50, bg="white", font=("arial", 14, "italic"))
        self.e2.bind("<FocusIn>", lambda e: self.remtext("e2"))
        self.e2.bind("<FocusOut>", lambda e: self.deftext("e2"))
        self.e2.bind("<Up>", lambda e: self.prev("e2"))
        self.e2.bind("<Down>", lambda e: self.next("e2"))
        self.e2.place(x=200, y=50)

        self.btn1 = Button(self.f1, text="DELETE", command=self.savedata, font=("arial", 14, "bold"), bd=5)
        self.btn1.place(x=700, y=500)

        self.btn3 = Button(self.f1, text="REFRESH", command=lambda: del_nur(self.doc_win1, 20, 40),
                           font=("arial", 14, "bold"), bd=5)
        self.btn3.place(x=850, y=500)

        self.btn2 = Button(self.f1, text="FETCH RECORD", font=("arial", 11, "bold"), bd=5, command=self.fetcher)
        self.btn2.place(x=800, y=40)

        self.f3 = Frame(self.f1, bg="gray95")

        sc_x = Scrollbar(self.f3, orient=HORIZONTAL)
        sc_y = Scrollbar(self.f3, orient=VERTICAL)

        self.table = Treeview(self.f3, columns=("ID", "NAME", "GENDER", "PHONE NUMBER", "ADDRESS", "WING",
                                                "ROOM ALLOTED")
                         , xscrollcommand=sc_x.set, yscrollcommand=sc_y.set)

        sc_x.config(command=self.table.xview)
        sc_x.pack(side=BOTTOM, fill=X)
        sc_y.config(command=self.table.yview)
        sc_y.pack(side=RIGHT, fill=Y)

        self.table.heading("ID", text="ID")
        self.table.heading("NAME", text="NAME")
        self.table.heading("GENDER", text="GENDER")
        self.table.heading("PHONE NUMBER", text="PHONE NUMBER")
        self.table.heading("ADDRESS", text="ADDRESS")
        self.table.heading("WING", text="WING")
        self.table.heading("ROOM ALLOTED", text="ROOM ALLOTTED")
        self.table["show"] = "headings"

        self.table.column("#0", stretch=NO, minwidth=0, width=0)
        self.table.column("#1", stretch=NO, minwidth=50, width=50)
        self.table.column("#2", stretch=NO, minwidth=100, width=100)
        self.table.column("#3", stretch=NO, minwidth=100, width=100)
        self.table.column("#4", stretch=NO, minwidth=120, width=120)
        self.table.column("#5", stretch=NO, minwidth=100, width=100)
        self.table.column("#6", stretch=NO, minwidth=100, width=100)
        self.table.column("#7", stretch=NO, minwidth=120, width=120)

        self.table.bind("<ButtonRelease>", lambda e: self.inserter())

        self.table.pack()
        self.f3.place(x=50, y=150)


        self.f1.mainloop()

    def showtext(self):

        if not self.t1.get():
            self.f1.focus_set()
            self.t1.set("Enter Unique Id")
            self.e1.config(textvariable=self.t1, fg="grey")
        if not self.t2.get():
            self.f1.focus_set()
            self.t2.set("Enter Name To Fetch Record")
            self.e2.config(textvariable=self.t2, fg="grey")

    def remtext(self, name):

        if name == "e1":
            if self.t1.get() == "Enter Unique Id":
                self.t1.set("")
            else:
                self.t1.set(self.e1.get())
            self.e1.config(textvariable=self.t1, fg="black", bg="yellow")
        elif name == "e2":
            if self.t2.get() == "Enter Name To Fetch Record":
                self.t2.set("")
            else:
                self.t2.set(self.e2.get())
            self.e2.config(textvariable=self.t2, fg="black", bg="yellow")

    def deftext(self, name):

        if name == "e1":
            self.e1.config(bg="white")
        elif name == "e2":
            self.e2.config(bg="white")

    def prev(self, name):

        if name == "e1":
            self.e2.focus_set()
        elif name == "e2":
            self.e1.focus_set()

    def next(self, name):

        if name == "e1":
            self.e2.focus_set()
        elif name == "e2":
            self.e1.focus_set()

    def savedata(self):

        try:
            d1 = Connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc.execute("SELECT img FROM nurse WHERE id=%s", (self.e1.get()))
                res = dc.fetchone()
                for i in res:
                    self.del_img = i
                path = os.path.join("nurimages//", self.del_img)
                os.remove(path)
                dc.execute("DELETE FROM nurse WHERE ID =%s",
                           (self.e1.get()))
                d1.commit()
                messagebox.showinfo("SAVE", "Data Deleted Successfully", parent=self.doc_win1)
                del_nur(self.doc_win1,20,40)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.doc_win1)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.doc_win1)

    def fetcher(self):
        try:
            d1 = Connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc.execute("SELECT * FROM nurse WHERE name like '%"+str(self.e2.get())+"%'")
                self.result = dc.fetchall()
                self.table.delete(*self.table.get_children())
                for row in self.result:
                    self.table.insert("", END, values=row)
                if not self.result:
                    messagebox.showinfo("INFO", "NO DATA FOUND", parent=self.doc_win1)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.doc_win1)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.doc_win1)

    def inserter(self):
        currentItem = self.table.focus()
        contents = self.table.item(currentItem)
        selectedRow = contents['values']
        ID = selectedRow[0]
        try:
            d1 = connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc.execute("select * from doctor where ID=%s", (ID))
                result = dc.fetchall()
                for row in result:
                    self.e1.delete(0, END)
                    self.e1.insert(0, row[0])
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.doc_win1)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.doc_win1)

def main():
    pass


if __name__ == '__main__':
    main()