import tkinter as tk
# from tkinter import tk
from PIL import Image,ImageTk
import smtplib
import playsound
import threading
from datetime import datetime
from time import strftime
from fire import main_funt
# from noice import beep_alarm
import tkinter.font as font

# class Security_System:
window = tk.Tk()
window.title("Smart cctv")
# window.iconphoto(False, tk.PhotoImage(file='inout.jpg'))
window.geometry('1080x700')


frame1 = tk.Frame(window)

label_title = tk.Label(frame1, text="Smart cctv Camera")
label_font = font.Font(size=35, weight='bold',family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10,10), column=2)


icon = Image.open('known.jpg')
icon = icon.resize((150,150), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5,10), column=2)
# def __init__(self,root):
#     self.root=root
#     self.root.geometry("1400x660+0+0")
#     self.root.title("Advance Security Management System")
    
# bg image
# bg_img=ttk.Frame(self)
# img4=Image.open(r"C:\Users\HP\Desktop\minner2\background.jpg")
# img4=img4.resize((1400,710),Image.ANTIALIAS)
# self.photoimg4=ImageTk.PhotoImage(img4)

# bg_img=Label(self.root,image=self.photoimg4)
# bg_img.place(x=0,y=0,width=1400,height=710)

# title_lbl=Label(bg_img,text="Advance Security Management System",font=("times new roman",20,"bold"),bg="yellow",fg="red")
# title_lbl.place(x=0,y=0,width=1350,height=30)
#Motion button
img5=Image.open(r"motion.jpg")
img5=img5.resize((180,180),Image.ANTIALIAS)
photoimg5=ImageTk.PhotoImage(img5)

b1=tk.Button(icon,image=photoimg5,cursor="hand2")
b1.place(x=200,y=100,width=180,height=180)

b1_1=tk.Button(icon,text="Monitor",cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="red")
b1_1.place(x=200,y=280,width=180,height=25)
#Identify button
img7=Image.open(r"known.jpg")
img7=img7.resize((180,180),Image.ANTIALIAS)
photoimg7=ImageTk.PhotoImage(img7)

b1=tk.Button(icon,image=photoimg7,cursor="hand2")
b1.place(x=420,y=100,width=180,height=180)
b1_1=tk.Button(icon,text="Identify",cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="red")
b1_1.place(x=420,y=280,width=180,height=25)
#Noise button
img6=Image.open(r"noise.jpg")
img6=img6.resize((180,180),Image.ANTIALIAS)
photoimg6=ImageTk.PhotoImage(img6)

b1=tk.Button(icon,image=photoimg6,cursor="hand2")
b1.place(x=640,y=100,width=180,height=180)

b1_1=tk.Button(icon,text="Noise",cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="red")
b1_1.place(x=640,y=280,width=180,height=25)
#IN/OUT
img8=Image.open(r"known.jpg")
img8=img8.resize((180,180),Image.ANTIALIAS)
photoimg8=ImageTk.PhotoImage(img8)
b1=tk.Button(icon,image=photoimg8,cursor="hand2")
b1.place(x=860,y=100,width=180,height=180)
b1_1=tk.Button(icon,text="In Out",cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="red")
b1_1.place(x=860,y=280,width=180,height=25)
#Record button
img9=Image.open(r"known.jpg")
img9=img9.resize((180,180),Image.ANTIALIAS)
photoimg9=ImageTk.PhotoImage(img9)
b1=tk.Button(icon,image=photoimg9,cursor="hand2")
b1.place(x=200,y=320,width=180,height=180)
b1_1=tk.Button(icon,text="Record",cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="red")
b1_1.place(x=200,y=480,width=180,height=25)
#object button
img10=Image.open(r"object.png")
img10=img10.resize((180,180),Image.ANTIALIAS)
photoimg10=ImageTk.PhotoImage(img10)

b1=tk.Button(icon,image=photoimg10,cursor="hand2" )
b1.place(x=420,y=320,width=180,height=180)

b1_1=tk.Button(icon,text="Object Detection",cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="red")
b1_1.place(x=420,y=480,width=180,height=25)
#People Counting button
img11=Image.open(r"known.jpg")
img11=img11.resize((180,180),Image.ANTIALIAS)
photoimg11=ImageTk.PhotoImage(img11)
b1=tk.Button(icon,image=photoimg11,cursor="hand2")
b1.place(x=640,y=320,width=180,height=180)
b1_1=tk.Button(icon,text="People Counting",cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="red")
b1_1.place(x=640,y=480,width=180,height=25)
#fire button
img12=Image.open(r"C:\Users\HP\Desktop\minner2\fire.png")
img12=img12.resize((180,180),Image.ANTIALIAS)
photoimg12=ImageTk.PhotoImage(img12)

b1=tk.Button(icon,image=photoimg12,command=main_funt,cursor="hand2")
b1.place(x=860,y=320,width=180,height=180)

b1_1=tk.Button(icon,text="FIRE",command=main_funt,cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="red")
b1_1.place(x=860,y=480,width=180,height=25)


    #==============time==================
def time():
        now=datetime.now()
        string = now.strftime("%H:%M:%S")

        # string=datetime.datetime.strptime('2-1-2020 3:14:5', '%m-%d-%Y %H:%M:%S')
        lbl.config(text=string)
        lbl.after(1000,time)
    
lbl=tk.Label(label_icon,font = ('times new roman',14,'bold'),background='white',foreground='blue')
lbl.place(x=0,y=0,width=90,height=40)
time()

#       #*** noice button*****
  
    # def noice(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Noice_Detector(self.new_window) 

    #     # fire button 
    # def fire(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Fire_Detector(self.new_window) 


# if __name__ == "__main__":
#     root=Tk()
#     obj=Security_System(root)
#     root.mainloop()

frame1.pack()
window.mainloop()