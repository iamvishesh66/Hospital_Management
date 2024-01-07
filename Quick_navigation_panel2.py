from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import askquestion

from Home_page_mainframe import MainFrame
from add_appointment import add_app
from add_patient import add_pat
from calculator import calculator
from delete_appointment import del_app
from delete_patient import del_pat
from payments import bill_desk
from upd_app import upd_app
from upd_pat import upd_pat
from vei_app import vei_app
from vei_doc import vei_doc
from vei_nur import vei_nur
from vei_pat import vei_pat


class navigator:

    def __init__(self, parent,a,b):

        self.a = a
        self.home = b
        self.navigate = parent

        # default img
        default_img1 = PhotoImage(file="default_img1.png").subsample(6,6)
        # widget pics
        widget1 = PhotoImage(file="dashboard.png").subsample(5,5)
        widget2 = PhotoImage(file="doctor_widget.png").subsample(6,6)
        widget3 = PhotoImage(file="nurse_widget.png").subsample(9,9)
        widget4 = PhotoImage(file="patient_widget.png").subsample(5,5)
        widget5 = PhotoImage(file="appointment_widget.png").subsample(30,30)
        widget6 = PhotoImage(file="bill.png").subsample(10,10)
        widget7 = PhotoImage(file="back_widget.png").subsample(15,15)
        widget8 = PhotoImage(file="logout.png").subsample(3,3)

        self.canvas1 = Canvas(self.navigate, width=300, height=70, bg="dark orange", highlightbackground="dark orange")
        self.canvas1.place(x=0,y=0)
        self.canvas1.bind("<Enter>", lambda e:self.highlight("canvas1"))
        self.canvas1.bind("<Leave>", lambda e:self.normal("canvas1"))
        self.canvas1.create_text(160, 20, text="Super User", font=("Sitka Heading", 16), fill="yellow")
        self.canvas1.create_text(140, 50, text="USER", font=("Sitka Heading", 12, "bold"), fill="white")
        l1 = Label(self.canvas1, image=default_img1, bg="dodger blue3", height=43, width=43)
        l1.place(x=12, y=11)
        l1.image = default_img1
        self.canvas1.create_oval(70,70,2,2,fill="dodger blue3", outline="")

        # starting adding main widgets
        # 1
        self.canvas2 = Canvas(self.navigate, width=300, height=70, bg="dodger blue3", highlightbackground="dodger blue3")
        self.canvas2.place(x=0, y=72)
        self.canvas2.bind("<Enter>", lambda e: self.highlight("canvas2"))
        self.canvas2.bind("<Leave>", lambda e: self.normal("canvas2"))
        self.canvas2.bind("<Button>", lambda e: MainFrame(a, 20, 40))
        self.canvas2.create_text(150, 40, text="Dashboard", font=("Sitka Heading", 14), fill="white")
        self.canvas2.create_image(30, 30, image=widget1)
        self.canvas2.image = widget1

        #2
        self.canvas3 = Canvas(self.navigate, width=300, height=70, bg="dodger blue3",
                              highlightbackground="dodger blue3")
        self.canvas3.place(x=0, y=142)
        self.canvas3.bind("<Enter>", lambda e: self.highlight("canvas3"))
        self.canvas3.bind("<Leave>", lambda e: self.normal("canvas3"))
        self.canvas3.create_text(150, 40, text="Doctor", font=("Sitka Heading", 14), fill="white")
        self.canvas3.create_image(30, 30, image=widget2)
        self.canvas3.image = widget2
        #3
        self.canvas4 = Canvas(self.navigate, width=300, height=70, bg="dodger blue3",
                              highlightbackground="dodger blue3")
        self.canvas4.place(x=0, y=212)
        self.canvas4.bind("<Enter>", lambda e: self.highlight("canvas4"))
        self.canvas4.bind("<Leave>", lambda e: self.normal("canvas4"))
        self.canvas4.create_text(150, 40, text="Nurse", font=("Sitka Heading", 14), fill="white")
        self.canvas4.create_image(30, 30, image=widget3)
        self.canvas4.image = widget3
        #4
        self.canvas5 = Canvas(self.navigate, width=300, height=70, bg="dodger blue3",
                              highlightbackground="dodger blue3")
        self.canvas5.place(x=0, y=282)
        self.canvas5.bind("<Enter>", lambda e: self.highlight("canvas5"))
        self.canvas5.bind("<Leave>", lambda e: self.normal("canvas5"))
        self.canvas5.create_text(150, 40, text="Patient", font=("Sitka Heading", 14), fill="white")
        self.canvas5.create_image(30, 30, image=widget4)
        self.canvas5.image = widget4
        #5
        self.canvas6 = Canvas(self.navigate, width=300, height=70, bg="dodger blue3",
                              highlightbackground="dodger blue3")
        self.canvas6.place(x=0, y=352)
        self.canvas6.bind("<Enter>", lambda e: self.highlight("canvas6"))
        self.canvas6.bind("<Leave>", lambda e: self.normal("canvas6"))
        self.canvas6.create_text(150, 40, text="Appointment", font=("Sitka Heading", 14), fill="white")
        self.canvas6.create_image(30, 35, image=widget5)
        self.canvas6.image = widget5
        #6
        self.canvas7 = Canvas(self.navigate, width=300, height=70, bg="dodger blue3",
                              highlightbackground="dodger blue3")
        self.canvas7.place(x=0, y=422)
        self.canvas7.bind("<Enter>", lambda e: self.highlight("canvas7"))
        self.canvas7.bind("<Leave>", lambda e: self.normal("canvas7"))
        self.canvas7.create_text(150, 40, text="Payment", font=("Sitka Heading", 14), fill="white")
        self.canvas7.create_image(30, 35, image=widget6)
        self.canvas7.image = widget6
        #7
        self.canvas8 = Canvas(self.navigate, width=300, height=70, bg="dodger blue3",
                              highlightbackground="dodger blue3")
        self.canvas8.place(x=0, y=492)
        self.canvas8.bind("<Enter>", lambda e: self.highlight("canvas8"))
        self.canvas8.bind("<Leave>", lambda e: self.normal("canvas8"))
        self.canvas8.bind("<Button>", lambda e: self.previous())
        self.canvas8.create_text(150, 40, text="Previous Page", font=("Sitka Heading", 14), fill="white")
        self.canvas8.create_image(30, 35, image=widget7)
        self.canvas8.image = widget7
        #8
        self.canvas9 = Canvas(self.navigate, width=300, height=70, bg="dodger blue3",
                              highlightbackground="dodger blue3")
        self.canvas9.place(x=0, y=562)
        self.canvas9.bind("<Enter>", lambda e: self.highlight("canvas9"))
        self.canvas9.bind("<Leave>", lambda e: self.normal("canvas9"))
        self.canvas9.bind("<Button>", lambda e:self.sign_out())
        self.canvas9.create_text(150, 25, text="Log Out", font=("Sitka Heading", 14), fill="white")
        self.canvas9.create_image(30, 25, image=widget8)
        self.canvas9.image = widget8

        # some images which a essential
        self.img_1 = PhotoImage(file="add.png").subsample(20, 20)
        self.img_2 = PhotoImage(file="update.png").subsample(100, 100)
        self.img_3 = PhotoImage(file="delete.png").subsample(20, 20)
        self.img_4 = PhotoImage(file="cal.png").subsample(6, 6)
        self.img_5 = PhotoImage(file="bill.png").subsample(15, 15)
        self.img_6 = PhotoImage(file="view.png").subsample(10, 10)

        self.datastorage = []


    def highlight(self,name):
        if name == "canvas1":
            self.canvas1.config(bg="orange", highlightbackground="orange")
        elif name == "canvas2":
            self.canvas2.config(bg="dark orange", highlightbackground="dark orange")
            self.canvas1.config(bg="dodger blue3", highlightbackground="dodger blue3")
        elif name == "canvas3":
            self.canvas3.config(bg="dark orange", highlightbackground="dark orange")
            self.canvas1.config(bg="dodger blue3", highlightbackground="dodger blue3")
            # lets create some buttons
            self.b4 = Button(self.canvas3, image=self.img_6, height=65, width=65, bg="dark orange",command=lambda : vei_doc(self.a, 20, 40))
            self.b4.place(x=230, y=0)
            self.b4.bind("<Button>", lambda e: self.datastorage.append("vei_doc"))
        elif name == "canvas4":
            self.canvas4.config(bg="dark orange", highlightbackground="dark orange")
            self.canvas1.config(bg="dodger blue3", highlightbackground="dodger blue3")
            # lets create some buttons
            self.b4 = Button(self.canvas4, image=self.img_6, height=65, width=65, bg="dark orange",command=lambda : vei_nur(self.a, 20, 40))
            self.b4.place(x=230, y=0)
            self.b4.bind("<Button>", lambda e: self.datastorage.append("vei_nur"))
        elif name == "canvas5":
            self.canvas5.config(bg="dark orange", highlightbackground="dark orange")
            self.canvas1.config(bg="dodger blue3", highlightbackground="dodger blue3")
            # lets create some buttons
            self.b1 = Button(self.canvas5, image=self.img_1, height=30, width=30, bg="dark orange",command=lambda :add_pat(self.a,20,40))
            self.b1.place(x=230, y=0)
            self.b1.bind("<Button>", lambda e: self.datastorage.append("add_pat"))
            self.b2 = Button(self.canvas5, image=self.img_3, height=30, width=30, bg="dark orange",command=lambda :del_pat(self.a,20,40))
            self.b2.place(x=230, y=35)
            self.b2.bind("<Button>", lambda e: self.datastorage.append("del_pat"))
            self.b3 = Button(self.canvas5, image=self.img_2, height=30, width=30, bg="dark orange",command=lambda :upd_pat(self.a,20, 40))
            self.b3.place(x=265, y=0)
            self.b3.bind("<Button>", lambda e: self.datastorage.append("upd_pat"))
            self.b4 = Button(self.canvas5, image=self.img_6, height=30, width=30, bg="dark orange",command=lambda : vei_pat(self.a, 20, 40))
            self.b4.place(x=265, y=35)
            self.b4.bind("<Button>", lambda e: self.datastorage.append("vei_pat"))
        elif name == "canvas6":
            self.canvas6.config(bg="dark orange", highlightbackground="dark orange")
            self.canvas1.config(bg="dodger blue3", highlightbackground="dodger blue3")
            # lets create some buttons
            self.b1 = Button(self.canvas6, image=self.img_1, height=30, width=30, bg="dark orange",command=lambda :add_app(self.a,20,40))
            self.b1.place(x=230, y=0)
            self.b1.bind("<Button>", lambda e: self.datastorage.append("add_app"))
            self.b2 = Button(self.canvas6, image=self.img_3, height=30, width=30, bg="dark orange",command=lambda :del_app(self.a,20,40))
            self.b2.place(x=230, y=35)
            self.b2.bind("<Button>", lambda e: self.datastorage.append("del_app"))
            self.b3 = Button(self.canvas6, image=self.img_2, height=30, width=30, bg="dark orange",command=lambda :upd_app(self.a,20,40))
            self.b3.place(x=265, y=0)
            self.b3.bind("<Button>", lambda e: self.datastorage.append("upd_app"))
            self.b4 = Button(self.canvas6, image=self.img_6, height=30, width=30, bg="dark orange",command=lambda :vei_app(self.a, 20, 40))
            self.b4.place(x=265, y=35)
            self.b4.bind("<Button>", lambda e: self.datastorage.append("vei_app"))
        elif name == "canvas7":
            self.canvas7.config(bg="dark orange", highlightbackground="dark orange")
            self.canvas1.config(bg="dodger blue3", highlightbackground="dodger blue3")
            # lets create some buttons
            self.b1 = Button(self.canvas7, image=self.img_4, height=65, width=40, bg="dark orange",command=lambda :calculator(self.a,20,40))
            self.b1.place(x=210, y=0)
            self.b1.bind("<Button>", lambda e: self.datastorage.append("bill_des"))
            self.b2 = Button(self.canvas7, image=self.img_5, height=65, width=40, bg="dark orange",command=lambda :bill_desk(self.a, 20, 40))
            self.b2.place(x=255, y=0)
            self.b2.bind("<Button>", lambda e: self.datastorage.append("calculator"))
        elif name == "canvas8":
            self.canvas8.config(bg="dark orange", highlightbackground="dark orange")
            self.canvas1.config(bg="dodger blue3", highlightbackground="dodger blue3")
        elif name == "canvas9":
            self.canvas9.config(bg="dark orange", highlightbackground="dark orange")
            self.canvas1.config(bg="dodger blue3", highlightbackground="dodger blue3")
    def normal(self,name):
        if name == "canvas1":
            self.canvas1.config(bg="dark orange", highlightbackground="dark orange")
        elif name == "canvas2":
            self.canvas2.config(bg="dodger blue3", highlightbackground="dodger blue3")
            self.canvas1.config(bg="dark orange", highlightbackground="dark orange")
        elif name == "canvas3":
            self.canvas3.config(bg="dodger blue3", highlightbackground="dodger blue3")
            self.canvas1.config(bg="dark orange", highlightbackground="dark orange")
            #lets destroy some buttons
            self.b4.destroy()
        elif name == "canvas4":
            self.canvas4.config(bg="dodger blue3", highlightbackground="dodger blue3")
            self.canvas1.config(bg="dark orange", highlightbackground="dark orange")
            # lets destroy some buttons
            self.b4.destroy()
        elif name == "canvas5":
            self.canvas5.config(bg="dodger blue3", highlightbackground="dodger blue3")
            self.canvas1.config(bg="dark orange", highlightbackground="dark orange")
            # lets destroy some buttons
            self.b1.destroy()
            self.b2.destroy()
            self.b3.destroy()
            self.b4.destroy()
        elif name == "canvas6":
            self.canvas6.config(bg="dodger blue3", highlightbackground="dodger blue3")
            self.canvas1.config(bg="dark orange", highlightbackground="dark orange")
            # lets destroy some buttons
            self.b1.destroy()
            self.b2.destroy()
            self.b3.destroy()
            self.b4.destroy()
        elif name == "canvas7":
            self.canvas7.config(bg="dodger blue3", highlightbackground="dodger blue3")
            self.canvas1.config(bg="dark orange", highlightbackground="dark orange")
            # lets destroy some buttons
            self.b1.destroy()
            self.b2.destroy()
        elif name == "canvas8":
            self.canvas8.config(bg="dodger blue3", highlightbackground="dodger blue3")
            self.canvas1.config(bg="dark orange", highlightbackground="dark orange")
        elif name == "canvas9":
            self.canvas9.config(bg="dodger blue3", highlightbackground="dodger blue3")
            self.canvas1.config(bg="dark orange", highlightbackground="dark orange")

    def sign_out(self):
        a = askquestion("SIGN OUT", "ARE YOU SURE YOU WANT TO SIGN OUT")
        if a == 'yes':
            self.home.destroy()
            self.home.tk_focusPrev()
        else:
            self.home.focus_force()

    def previous(self):
        if self.datastorage:
            if not len(self.datastorage) == 1:
                a1 = len(self.datastorage)-2
                a = self.datastorage[a1]
                if a == "vei_doc":
                    self.datastorage.pop(a1)
                    vei_doc(self.a,20,40)
                elif a == "vei_nur":
                    self.datastorage.pop(a1)
                    vei_nur(self.a,20,40)
                elif a == "add_pat":
                    self.datastorage.pop(a1)
                    add_pat(self.a,20,40)
                elif a == "del_pat":
                    self.datastorage.pop(a1)
                    del_pat(self.a,20,40)
                elif a == "upd_pat":
                    self.datastorage.pop(a1)
                    upd_pat(self.a,20,40)
                elif a == "vei_pat":
                    self.datastorage.pop(a1)
                    vei_pat(self.a,20,40)
                elif a == "add_app":
                    self.datastorage.pop(a1)
                    add_app(self.a,20,40)
                elif a == "del_app":
                    self.datastorage.pop(a1)
                    del_app(self.a,20,40)
                elif a == "upd_app":
                    self.datastorage.pop(a1)
                    upd_app(self.a,20,40)
                elif a == "vei_app":
                    self.datastorage.pop(a1)
                    vei_app(self.a,20,40)
                elif a == "bill_des":
                    self.datastorage.pop(a1)
                    bill_desk(self.a,20,40)
                elif a == "calculator":
                    self.datastorage.pop(a1)
                    calculator(self.a,20,40)
            else:
                messagebox.showinfo("LAST", "Can't Go Back\nNo Window Left")
        else:
            messagebox.showinfo("LAST","Can't Go Back\nNo Window Left")


def main():
    pass

if __name__ == '__main__':
    main()
