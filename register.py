
# from multiprocessing.sharedctypes import Value
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk 
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("regester")
        self.root.geometry("1300x800+0+0")
        

        #================== variables==============
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        #**************bg img*****************
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\HP\Desktop\minner2\bg2.jpg")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        

        # *************left image****************
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\HP\Desktop\minner2\images\bg.jpg")
        
        left_bg1=Label(self.root,image=self.bg1)
        left_bg1.place(x=50,y=100, width=400,height=450)

       #****************main frame***************
        frame=Frame(self.root,bg="white")
        frame.place(x=450,y=100,width=750,height=450)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="dark green",bg="white")
        register_lbl.place(x=20,y=20)


        #******************lables and entry********************
        #*****************row1************************

        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=70)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=100,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=70)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=100,width=250)

        #************row2****************
        contact=Label(frame,text="contact no",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=140)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=170,width=250)


        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=140)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=170,width=250)
        

        #************row3****************
        security_Q=Label(frame,text="select security quetions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=210)

        self.txt_combosecurity_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15),state="ReadOnly")
        self.txt_combosecurity_Q["values"]=("select","your Birth place","your country")

        self.txt_combosecurity_Q.place(x=50,y=240,width=250)
        self.txt_combosecurity_Q.current(0)


        security_A=Label(frame,text="security_Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=210)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=240,width=250)

        #************row4****************
        pswd=Label(frame,text="password ",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=280)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=310,width=250)


        confirm_pswd=Label(frame,text="confirm password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=280)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=310,width=250)

        #******************chechbutton********************

        self.var_check=IntVar()
        Checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the term and conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        Checkbtn.place(x=50,y=350)

        #**************buttons**************
        img4=Image.open(r"C:\Users\HP\Desktop\minner2\images\button_regester.jpeg")
        img4=img4.resize((100,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img4)

        b1=Button(frame, image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=100,y=390,width=100)
    
        
        # img5=Image.open("C:/Users/HP/Desktop/minner2/images/b88.png")
        # img5=img5.resize((100,50),Image.ANTIALIAS)
        # self.photoimage=ImageTk.PhotoImage(img5)
        # b1=Button(frame,image=self.photoimage,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        # b1.place(x=420,y=390,width=100)

    # =========== function decleration============

    def register_data(self):
        if self.var_fname.get()==""or self.var_email.get()==""or self.var_securityQ.get()=="select":
            messagebox.showerror("Error","All field are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & conformpassword must be same")

        elif self.var_check.get()==0:
            messagebox.showerror("Error","please agree all terms and condition")
        else:
            # messagebox.showinfo("success","welcome friends")
            messagebox.showinfo("success","welcome")
            c=mysql.connector.connect(host="localhost",username="root",password="SHpatel@9893",database="face_recognizer")
            my_cursor=c.cursor()
            messagebox.showinfo("success","welcome2")
            query=("select * from register where email=%s")
            Value=(self.var_email.get(),)
            my_cursor.execute(query,Value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","user already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",[
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()

                                                                                    ])
            messagebox.showinfo("success","welcome3")                                                                        
            c.commit()
            c.close()
            messagebox.showerror("success","regester successfully")



if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
