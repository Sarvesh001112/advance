from cProfile import label
from multiprocessing.sharedctypes import Value
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from Mpage import Security_System
from turtle import width
from PIL import Image,ImageTk 
from register import Register
import mysql.connector
import tkinter
from turtle import title
from PIL import Image,ImageTk
import os
#from os import startfile
from time import strftime
from datetime import datetime
from identifier import maincall 
#from face_recognization import Face_Recognition
from object_main import object_detection
from Pedestrian_Counter import counter
from fire import fire
from noice import noice_main
from inout import in_out
from motion import noise
from Record import record


def main():
    win=Tk()
    app=login_Window(win)
    win.mainloop()


class login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1300x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:/Users/HP/Desktop/minner2/images/ll.jpg")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=430,y=70,width=350,height=450)

        img1=Image.open(r"C:/Users/HP\Desktop/minner2/images/logo_transparent.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,borderwidth=0)
        lblimg1.place(x=555,y=70,width=100,height=100)


        get_str=Label(frame,text="Get started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=120,y=110)
        

        #lable
        self.username=StringVar()
        username=lbl=Label(frame, text="username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)
        
        self.txtuser=ttk.Entry(frame,textvariable=self.username, font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=190,width=270)

        self.password=StringVar()
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=230)
        
        self.txtpass=ttk.Entry(frame,textvariable=self.password, font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=265,width=270)

        #***********ICON Images***********
        img2=Image.open(r"C:/Users/HP\Desktop/minner2/images/app logo.jpeg")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=460,y=225,width=25,height=25)


        img3=Image.open(r"C:/Users/HP\Desktop/minner2/images/app logo.jpeg")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=460,y=300,width=25,height=25)

        #login button

        loginbtn=Button(frame,command=self.login, text="Login",font=("times new roman",15,"bold"),bd=3, relief=RIDGE, fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=320,width=120,height=30)
        
        #regester button
        regesterbtn=Button(frame,text="new user Regester",command=self.register_window, font=("times new roman",15,"bold"),borderwidth=0, fg="white",bg="black",activeforeground="white",activebackground="black")
        regesterbtn.place(x=20,y=400,width=160)
        

        #forget password
        forgetpasswordbtn=Button(frame,command=self.forgot_password_window,text="forget password",font=("times new roman",15,"bold"),borderwidth=0, fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetpasswordbtn.place(x=10,y=370,width=160)


    def login(self):
        if self.txtuser.get()=="" and self.txtpass.get()=="":
            messagebox.showerror("error", "all field required")
        elif self.txtuser.get()=="shubham" and self.txtpass.get()=="shub":
            messagebox.showinfo("success","welcome to the company ")
        else:
            # messagebox.showerror("Invalid","Invalid username and password")
            c=mysql.connector.connect(host="localhost",username="root",password="SHpatel@9893",database="face_recognizer")
            my_cursor=c.cursor()
            print("hello",self.txtuser.get())
            my_cursor.execute("select*from register where email='"+self.txtuser.get()+"' and password='"+self.txtpass.get()+"'")
            messagebox.showinfo("success","welcome to the company ")
        
            # ,[
            #                                                                            self.var_email.get(),
            #                                                                            self.var_pass.get()
            #                                                                         ])

            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","envalid usernamr and password")
            else:
                open_main=messagebox.askyesno("yesno","Access only admin")
                if open_main>0:
                    # self.new_window=Toplevel(self.new_window)
                    # self.app=main_page(self.new_window)
                    self.new_window=Toplevel(self.root)
                    self.app=Security_System(self.new_window) 

                else:
                    if not open_main:
                        return

            c.commit()
            c.close()

    #========= reset password =================
    def reset_pass(self):
        if self.txt_combosecurity_Q.get()=="select":
            messagebox.showerror("Error","select security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","please enter the answer",parent=self.root2)
        elif self.txtpass.get()=="":
            messagebox.showerror("Error","please enter the new password",parent=self.root2)
        else:
            c=mysql.connector.connect(host="localhost",username="root",password="SHpatel@9893",database="face_recognizer")
            my_cursor=c.cursor()  
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.txt_combosecurity_Q.get(),self.txt_security)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","please enter correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                c.commit()
                c.close()
                messagebox.showerror("Info","your password has been reset , please login new password",parent=self.root2)


   #=================== forgot passward =================         

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","please enter the email address to reset password")
        else:
            c=mysql.connector.connect(host="localhost",username="root",password="SHpatel@9893",database="face_recognizer")
            my_cursor=c.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)
            if row==None:
                messagebox.showerror("My Error","please enter the valied user name")
            else:
                c.close()
                self.root2=Toplevel()
                self.root2.title("forget password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="forgot password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=0,relwidth=1)


                security_Q=Label(self.root2,text="select security quetions",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.txt_combosecurity_Q=ttk.Combobox(self.root2,font=("times new roman",15),state="ReadOnly")
                self.txt_combosecurity_Q["values"]=("select","your Birth place","your country")

                self.txt_combosecurity_Q.place(x=50,y=120,width=240)
                self.txt_combosecurity_Q.current(0)


                security_A=Label(self.root2,text="security_Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=170)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=220,width=250)

                new_password=Label(self.root2,text="New password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=270)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=320,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),bg="green",fg="white")
                btn.place(x=150,y=370)



        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    # def chatbot(self):
    #  self.new_window=Toplevel(self.root)
    #  self.app=Register(self.new_window) 


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



    def return_login(self):
        self.root.destroy()

class Security_System:

   def __init__(self,root):
    self.root=root
    self.root.geometry("1400x660+0+0")
    self.root.title("Advance Security Management System")
    
# bg image
    img4=Image.open(r"C:\Users\HP\Desktop\minner2\images\background.jpg")
    img4=img4.resize((1400,710),Image.ANTIALIAS)
    self.photoimg4=ImageTk.PhotoImage(img4)
    bg_img=Label(self.root,image=self.photoimg4)
    bg_img.place(x=0,y=0,width=1400,height=710)
    title_lbl=Label(bg_img,text="Advance Security Management System",font=("times new roman",20,"bold"),bg="yellow",fg="red")
    title_lbl.place(x=0,y=0,width=1350,height=30)
# Record button

    img5=Image.open(r"C:\Users\HP\Desktop\minner2\images\rec.png")
    img5=img5.resize((180,180),Image.ANTIALIAS)
    self.photoimg5=ImageTk.PhotoImage(img5)

    b1=Button(bg_img,image=self.photoimg5,command=record, cursor="hand2")
    b1.place(x=200,y=100,width=180,height=180)

    b1_1=Button(bg_img,text="Record",cursor="hand2",command=record,font=("times new roman",15,"bold"),bg="yellow",fg="red")
    b1_1.place(x=200,y=280,width=180,height=25)


#Identify button
    img7=Image.open(r"C:\Users\HP\Desktop\minner2\images\known.jpg")
    img7=img7.resize((180,180),Image.ANTIALIAS)
    self.photoimg7=ImageTk.PhotoImage(img7)

    b1=Button(bg_img,image=self.photoimg7,command=maincall, cursor="hand2")
    b1.place(x=420,y=100,width=180,height=180)

    b1_1=Button(bg_img,text="Identify",cursor="hand2",command=maincall,font=("times new roman",15,"bold"),bg="yellow",fg="red")
    b1_1.place(x=420,y=280,width=180,height=25)
#Noise button
    img6=Image.open(r"C:\Users\HP\Desktop\minner2\images\noice.png")
    img6=img6.resize((180,180),Image.ANTIALIAS)
    self.photoimg6=ImageTk.PhotoImage(img6)

    b1=Button(bg_img,image=self.photoimg6, command=noice_main, cursor="hand2")
    b1.place(x=640,y=100,width=180,height=180)
    
    # command=beep_alarm,

    b1_1=Button(bg_img,text="Noise",cursor="hand2",command=noice_main, font=("times new roman",15,"bold"),bg="yellow",fg="red")
    b1_1.place(x=640,y=280,width=180,height=25)
#IN/OUT
    img8=Image.open(r"C:\Users\HP\Desktop\minner2\images\inout-detecth.jpg")
    img8=img8.resize((180,180),Image.ANTIALIAS)
    self.photoimg8=ImageTk.PhotoImage(img8)

    b1=Button(bg_img,image=self.photoimg8,command=in_out,cursor="hand2")
    b1.place(x=860,y=100,width=180,height=180)
    
    b1_1=Button(bg_img,text="In Out",command=in_out,cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="red")
    b1_1.place(x=860,y=280,width=180,height=25)
#Fire button
    img9=Image.open(r"C:\Users\HP\Desktop\minner2\images\fire.png")
    img9=img9.resize((180,180),Image.ANTIALIAS)
    self.photoimg9=ImageTk.PhotoImage(img9)

    b1=Button(bg_img,image=self.photoimg9,command=fire,cursor="hand2")
    b1.place(x=200,y=320,width=180,height=180)

    b1_1=Button(bg_img,text="Fire",cursor="hand2",command=fire,font=("times new roman",15,"bold"),bg="yellow",fg="red")
    b1_1.place(x=200,y=480,width=180,height=25)

#object button
    img10=Image.open(r"C:\Users\HP\Desktop\minner2\images\object.png")
    img10=img10.resize((180,180),Image.ANTIALIAS)
    self.photoimg10=ImageTk.PhotoImage(img10)

    b1=Button(bg_img,image=self.photoimg10,command=object_detection,cursor="hand2" )
    b1.place(x=420,y=320,width=180,height=180)

    b1_1=Button(bg_img,text="Object Detection",command=object_detection,cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="red")
    b1_1.place(x=420,y=480,width=180,height=25)

#People Counting button
    img11=Image.open(r"C:\Users\HP\Desktop\minner2\images\count.png")
    img11=img11.resize((180,180),Image.ANTIALIAS)
    self.photoimg11=ImageTk.PhotoImage(img11)
    b1=Button(bg_img,image=self.photoimg11,command=counter, cursor="hand2")
    b1.place(x=640,y=320,width=180,height=180)
    b1_1=Button(bg_img,text="People Counting",cursor="hand2",command=counter,font=("times new roman",15,"bold"),bg="yellow",fg="red")
    b1_1.place(x=640,y=480,width=180,height=25)
#Exit button
    img12=Image.open(r"C:\Users\HP\Desktop\minner2\images\exit.png")
    img12=img12.resize((180,180),Image.ANTIALIAS)
    self.photoimg12=ImageTk.PhotoImage(img12)

    b1=Button(bg_img,image=self.photoimg12,command=self.root.quit ,cursor="hand2")
    b1.place(x=860,y=320,width=180,height=180)

    b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.root.quit,font=("times new roman",15,"bold"),bg="yellow",fg="red")
    b1_1.place(x=860,y=480,width=180,height=25)


    #==============time==================
    def time():
        now=datetime.now()
        string = now.strftime("%H:%M:%S")

        # string=datetime.datetime.strptime('2-1-2020 3:14:5', '%m-%d-%Y %H:%M:%S')
        lbl.config(text=string)
        lbl.after(1000,time)
    
    lbl=Label(title_lbl,font = ('times new roman',14,'bold'),background='white',foreground='blue')
    lbl.place(x=0,y=0,width=90,height=40)
    time()


if __name__ == "__main__":
    main()
    # root=Tk()
    # app=login_Window(root)
    # root.mainloop()

