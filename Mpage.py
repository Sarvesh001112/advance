from datetime import datetime
from tkinter import *

from PIL import Image, ImageTk
from Pedestrian_Counter import counter

from Record import record
from fire import fire
# from main1 import motion
from identifier import maincall
from inout import in_out
from noice import noice_main
from object_main import object_detection


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
    root=Tk()
    obj=Security_System(root)
    root.mainloop()