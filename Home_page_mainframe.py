from tkinter import *

from add_appointment import add_app
from add_doctor import add_doc
from add_nurse import add_nur
from add_patient import add_pat
from calculator import calculator
from delete_appointment import del_app
from delete_doctor import del_doc
from delete_nurse import del_nur
from delete_patient import del_pat
from payments import bill_desk
from upd_app import upd_app
from upd_doc import upd_doc
from upd_nur import upd_nur
from upd_pat import upd_pat
from vei_app import vei_app
from vei_doc import vei_doc
from vei_nur import vei_nur
from vei_pat import vei_pat


class MainFrame:

    def __init__(self, parent, a, b):

        self.main_frame = parent

        self.f1 = Frame(self.main_frame, height=600, width=1000, bg="white")
        self.f1.place(x=a, y=b)

        self.f2 = Frame(self.main_frame, height=40, width=1000, bg="white")
        self.f2.place(x=20, y=-7)

        title = Label(self.f2, text="DASHBOARD", font=("algerian", 20, "bold", "underline")
                      , fg="dodger blue3", bg="white").place(x=350, y=0)

        # bg images
        img1 = PhotoImage(file="doctor_background.png").subsample(4,4)
        img2 = PhotoImage(file="patient_background.png").subsample(4,4)
        img3 = PhotoImage(file="nurse_background.png").subsample(2,2)
        img4 = PhotoImage(file="appointment_background.png").subsample(3,3)
        img5 = PhotoImage(file="bill1.png").subsample(2,2)
        img6 = PhotoImage(file="Payment.png").subsample(3,3)


        self.canvas1 = Canvas(self.f1, height=250, width=300, bg="navajo white", highlightbackground="black")
        self.canvas1.place(x=15, y=25)
        self.canvas1.create_text(60, 45, text="DOCTOR", fill="black", font=("arial", 15, "bold", "italic"))
        self.canvas1.create_image(150,130, image=img1)
        self.canvas1.image = img1
        self.canvas1.bind("<Enter>", lambda e: self.showwidgets("self.canvas1"))
        self.canvas1.bind("<Leave>", lambda e: self.hidewidgets("self.canvas1"))


        self.canvas2 = Canvas(self.f1, height=250, width=300, bg="gold", highlightbackground="black")
        self.canvas2.place(x=675, y=25)
        self.canvas2.create_text(60, 45, text="PATIENT", fill="black", font=("arial", 15, "bold", "italic"))
        self.canvas2.create_image(150,130, image=img2)
        self.canvas2.image = img2
        self.canvas2.bind("<Enter>", lambda e: self.showwidgets("self.canvas2"))
        self.canvas2.bind("<Leave>", lambda e: self.hidewidgets("self.canvas2"))


        self.canvas3 = Canvas(self.f1, height=515, width=330, bg="sandy brown", highlightbackground="black")
        self.canvas3.place(x=330, y=25)
        self.canvas3.create_text(60, 45, text="PAYMENT", fill="black", font=("arial", 15, "bold", "italic"))
        self.canvas3.create_image(230, 100, image=img5)
        self.canvas3.image = img5
        self.canvas3.create_image(170, 350, image=img6)
        self.canvas3.image1 = img6
        self.canvas3.bind("<Enter>", lambda e: self.showwidgets("self.canvas3"))
        self.canvas3.bind("<Leave>", lambda e: self.hidewidgets("self.canvas3"))


        self.canvas4 = Canvas(self.f1, height=250, width=300, bg="orange", highlightbackground="black")
        self.canvas4.place(x=675, y=290)
        self.canvas4.create_text(90, 45, text="APPOINTMENT", fill="black", font=("arial", 15, "bold", "italic"))
        self.canvas4.create_image(140, 150, image=img4)
        self.canvas4.image = img4
        self.canvas4.bind("<Enter>", lambda e: self.showwidgets("self.canvas4"))
        self.canvas4.bind("<Leave>", lambda e: self.hidewidgets("self.canvas4"))

        self.canvas5 = Canvas(self.f1, height=250, width=300, bg="dark goldenrod1", highlightbackground="black")
        self.canvas5.place(x=15, y=290)
        self.canvas5.create_text(60, 45, text="NURSE", fill="black", font=("arial", 15, "bold", "italic"))
        self.canvas5.create_image(200, 130, image=img3)
        self.canvas5.image = img3
        self.canvas5.bind("<Enter>", lambda e: self.showwidgets("self.canvas5"))
        self.canvas5.bind("<Leave>", lambda e: self.hidewidgets("self.canvas5"))

        #     widget images
        self.img_1 = PhotoImage(file="add.png").subsample(9, 9)
        self.img_2 = PhotoImage(file="update.png").subsample(50, 50)
        self.img_3 = PhotoImage(file="delete.png").subsample(10, 10)
        self.img_4 = PhotoImage(file="cal.png").subsample(3, 3)
        self.img_5 = PhotoImage(file="bill.png").subsample(9, 9)
        self.img_6 = PhotoImage(file="view.png").subsample(5, 5)

    def showwidgets(self,name):
        if name == "self.canvas1":
            self.kid1 = Button(self.canvas1, bg="navajo white", height=120, width=143
                               , image=self.img_1, text="ADD\nDOCTOR",font=("segoe",15,"italic")
                               , compound="top", command=lambda: add_doc(self.main_frame, 20, 40))
            self.kid1.grid(row=0, column=0)

            self.kid2 = Button(self.canvas1, bg="navajo white", height=120, width=143, image=self.img_2
                               , text="UPDATE\nDOCTOR", font=("segoe",15,"italic"), compound="top"
                               , command=lambda: upd_doc(self.main_frame,20, 40))
            self.kid2.grid(row=0, column=1)

            self.kid3 = Button(self.canvas1, bg="navajo white", height=120, width=143, image=self.img_3
                               , text="REMOVE\nDOCTOR", font=("segoe",15,"italic"), compound="top"
                               , command=lambda: del_doc(self.main_frame, 20, 40))
            self.kid3.grid(row=1, column=0)

            self.kid4 = Button(self.canvas1, bg="navajo white", height=120, width=143, image=self.img_6
                               , text="VIEW\nDOCTOR", font=("segoe",15,"italic"), compound="top"
                               , command=lambda: vei_doc(self.main_frame, 20, 40))
            self.kid4.grid(row=1, column=1)
        elif name == "self.canvas2":
            self.kid1 = Button(self.canvas2, bg="gold", height=120, width=143 , image=self.img_1
                               , text="ADD\nPATIENT", font=("segoe",15,"italic"), compound="top"
                               , command=lambda: add_pat(self.main_frame, 20, 40))
            self.kid1.grid(row=0, column=0)

            self.kid2 = Button(self.canvas2, bg="gold", height=120, width=143, image=self.img_2
                               , text="UPDATE\nPATIENT", font=("segoe",15,"italic"), compound="top"
                               , command=lambda: upd_pat(self.main_frame, 20, 40))
            self.kid2.grid(row=0, column=1)

            self.kid3 = Button(self.canvas2, bg="gold", height=120, width=143, image=self.img_3
                               , text="REMOVE\nPATIENT", font=("segoe",15,"italic"), compound="top"
                               , command=lambda: del_pat(self.main_frame, 20, 40))
            self.kid3.grid(row=1, column=0)

            self.kid4 = Button(self.canvas2, bg="gold", height=120, width=143, image=self.img_6
                               , text="VIEW\nPATIENT", font=("segoe",15,"italic"), compound="top"
                               , command=lambda: vei_pat(self.main_frame, 20, 40))
            self.kid4.grid(row=1, column=1)
        elif name == "self.canvas3":
            self.kid1 = Button(self.canvas3, bg="sandy brown", height=250, width=330, image=self.img_4
                               , text="CALCULATOR", font=("segoe", 18, "italic"), compound="top"
                               , command=lambda: calculator(self.main_frame, 20, 40))
            self.kid1.pack(side=TOP)

            self.kid2 = Button(self.canvas3, bg="sandy brown", height=250, width=330, image=self.img_5
                               , text="BILLING\n  DESK", font=("segoe", 18, "italic"), compound="top"
                               , command=lambda: bill_desk(self.main_frame, 20, 40))
            self.kid2.pack(side=BOTTOM)
        elif name == "self.canvas4":
            self.kid1 = Button(self.canvas4, bg="gold", height=120, width=143, image=self.img_1
                               , text="ADD\nAPPOINTMENT", font=("segoe", 15, "italic"), compound="top"
                               , command=lambda: add_app(self.main_frame, 20, 40))
            self.kid1.grid(row=0, column=0)

            self.kid2 = Button(self.canvas4, bg="gold", height=120, width=143, image=self.img_2
                               , text="UPDATE\nAPPOINTMENT", font=("segoe", 15, "italic"), compound="top"
                               , command=lambda: upd_app(self.main_frame, 20, 40))
            self.kid2.grid(row=0, column=1)

            self.kid3 = Button(self.canvas4, bg="gold", height=120, width=143, image=self.img_3
                               , text="REMOVE\nAPPOINTMENT", font=("segoe", 15, "italic"), compound="top"
                               , command=lambda: del_app(self.main_frame, 20, 40))
            self.kid3.grid(row=1, column=0)

            self.kid4 = Button(self.canvas4, bg="gold", height=120, width=143, image=self.img_6
                               , text="VIEW\nAPPOINTMENT", font=("segoe", 15, "italic"), compound="top"
                               , command=lambda: vei_app(self.main_frame, 20, 40))
            self.kid4.grid(row=1, column=1)
        elif name == "self.canvas5":
            self.kid1 = Button(self.canvas5, bg="gold", height=120, width=143, image=self.img_1
                               , text="ADD\nNURSE", font=("segoe", 15, "italic"), compound="top"
                               , command=lambda: add_nur(self.main_frame, 20, 40))
            self.kid1.grid(row=0, column=0)

            self.kid2 = Button(self.canvas5, bg="gold", height=120, width=143, image=self.img_2
                               , text="UPDATE\nNURSE", font=("segoe", 15, "italic"), compound="top"
                               , command=lambda: upd_nur(self.main_frame, 20, 40))
            self.kid2.grid(row=0, column=1)

            self.kid3 = Button(self.canvas5, bg="gold", height=120, width=143, image=self.img_3
                               , text="REMOVE\nNURSE", font=("segoe", 15, "italic"), compound="top"
                               , command=lambda: del_nur(self.main_frame, 20, 40))
            self.kid3.grid(row=1, column=0)

            self.kid4 = Button(self.canvas5, bg="gold", height=120, width=143, image=self.img_6
                               , text="VIEW\nNURSE", font=("segoe", 15, "italic"), compound="top"
                               , command=lambda: vei_nur(self.main_frame, 20, 40))
            self.kid4.grid(row=1, column=1)

    def hidewidgets(self,name):
        if name == "self.canvas1":
            self.kid1.destroy()
            self.kid2.destroy()
            self.kid3.destroy()
            self.kid4.destroy()
        elif name == "self.canvas2":
            self.kid1.destroy()
            self.kid2.destroy()
            self.kid3.destroy()
            self.kid4.destroy()
        elif name == "self.canvas3":
            self.kid1.destroy()
            self.kid2.destroy()
        elif name == "self.canvas4":
            self.kid1.destroy()
            self.kid2.destroy()
            self.kid3.destroy()
            self.kid4.destroy()
        elif name == "self.canvas5":
            self.kid1.destroy()
            self.kid2.destroy()
            self.kid3.destroy()
            self.kid4.destroy()

def main():
    pass


if __name__ == '__main__':
    main()