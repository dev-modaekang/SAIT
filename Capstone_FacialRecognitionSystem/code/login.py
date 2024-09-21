from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from mysql_functions import *
import face_recognition
import numpy as np
import cv2
import hashlib, binascii, os
import re

def passValid(passwd):
        numlen=0
        lowerlen=0
        upperlen=0
        special=0
        invalid=0

        if len(passwd)>20 or len(passwd)<8:
            return "invalid password, length should be in 8-20"
        for s in passwd:
            if s.isdigit():
                numlen += 1
            elif s.islower():
                lowerlen += 1
            elif s.isupper():
                upperlen += 1
            elif s=="_" or s == "?" or s == "!":
                special+= 1
            else:
                invalid += 1
        if lowerlen <=0 and upperlen <=0:
            return "invalid password, must have at least one upper and lower case letter"
        elif numlen ==0:
            return "invalid password, must have a number"
        elif upperlen<1:
            return "invalid password, must have an upper case "
        elif invalid >0:
            return "invalid password, contains invalid symbol"
        elif special <1:
            return "invalid password, must have a symbol ? or ! or _ "
        else:
            return "valid password"    

def userValid(username):

        if len(username)>30 or len(username)<6:
            return "invalid username, length should be in 6-30"
        elif re.match("^[a-zA-Z0-9.]+$",username)==None:
            return "invalid username, can't contain symbols other than period" 
        else:
            return "valid username"    


class APP:
    def __init__(self):
        self.camera=None
        self.imagename=""
        self.root=Tk()
        self.root.configure(background='white')
        self.root.title("")
        self.root.geometry('%dx%d' % (800, 800))
        self.createFirstPage()
        mainloop()
    
    def createFirstPage(self):
        self.page1=Frame(self.root,bg='white')
        self.page1.pack()
        self.frame=LabelFrame(self.page1,bg='white',text="", padx=50,pady=50,borderwidth=3)
        #distance between window and frame(outside the frame)
        self.frame.pack(padx=20,pady=20)
        self.label1=Label(self.frame,text="Sign in to your account",bg='white',fg="#02b3e5",font=("Times", 16))
        self.label1.grid(row=0,column=0,columnspan=2,pady=5,padx=10)
        self.user_label=Label(self.frame,text="User Name",bg='white')
        self.user_label.grid(row=2,column=0,pady=10,padx=10)
        self.user_box=Entry(self.frame,width=20)
        self.user_box.grid(row=2,column=1,padx=20)
        #create password
        self.password_label=Label(self.frame,text="Password",bg='white')
        self.password_label.grid(row=4,column=0,padx=10,pady=5)
        self.password_box=Entry(self.frame,show="*",width=20)
        self.password_box.grid(row=4,column=1,padx=20,pady=5)

        #create login button
        self.login=Button(self.frame,text="SIGN IN",width=25,bg='#02b3e5',fg='white',command=self.login)
        self.login.grid(row=8,column=0,columnspan=2,pady=20)


        #create show password checkbox
        self.var=StringVar()
        self.checkbox=Checkbutton(self.frame,text="Show Password",bg='white',variable=self.var,
            onvalue="On",offvalue="Off",command=self.toggle_password)
        self.checkbox.deselect()
        self.checkbox.grid(row=6,column=1,pady=5,padx=10)

        self.signup=Button(self.frame,text="SIGN UP",width=25,bg='#02b3e5',fg='white',command=self.createSignupPage)
        self.signup.grid(row=9,column=0,columnspan=2, pady=10)
        self.labels11=[]
        self.labels12=[]
        self.labels13=[]
        flabel=Label()
        self.labels11.append(flabel)
        self.labels12.append(flabel)
        self.labels13.append(flabel)

    def login(self):
        self.username1=""
        self.password1=""
        self.username1=self.user_box.get()
        self.password1=self.password_box.get()
        if self.username1=="" :
            textcon="Enter a username"
        else:
            textcon=""
        self.labelend11=Label(self.frame,text=textcon,fg="red", font=("Times",10), bg='white')
        self.labels11.append(self.labelend11)
        self.labels11[1].grid(row=3,column=1)
        self.labels11[0].grid_forget()
        self.labels11.remove(self.labels11[0])
        
        if self.password1 =="":
            textcon="Enter a password"
        else:
            textcon=""
        self.labelend12=Label(self.frame,text=textcon,fg="red", font=("Times",10), bg='white')
        self.labels12.append(self.labelend12)
        self.labels12[1].grid(row=5,column=1)
        self.labels12[0].grid_forget()
        self.labels12.remove(self.labels12[0])
        if not (self.username1 =="" or self.password1==""):
            result=Query_Data_Users (username= self.username1,password=self.password1)
            if result==True:
                textcon="Username password correct"
                self.createFacePage()
            else:
                textcon="Wrong usename or password. Try again"
            self.labelend13=Label(self.frame,text=textcon,fg="red", font=("Times",10), bg='white')
            self.labels13.append(self.labelend13)
            self.labels13[1].grid(row=1,column=0, columnspan=2)
            self.labels13[0].grid_forget()
            self.labels13.remove(self.labels13[0])
    def createFacePage(self):
        self.page4=Toplevel(self.root,bg="white")
        self.face_locations=[]
        self.face_encodings=[]
        self.camera=cv2.VideoCapture(0)
        self.label41=Label(self.page4, text='Verifying Face', fg='white',bg="#02b3e5", font=('Times',16))
        self.label41.grid(row=0, column=0,columnspan=3)
        self.data2 = Label(self.page4)
        self.data2.grid(row=1, column=0,columnspan=3)

        self.button41 = Button(self.page4, width=15, height=1, text="Submit", fg='white',bg="#02b3e5", font=("Times", 12),
           relief='raise',command = self.submitface)
        self.button41.grid(row=2, column=0)
        self.button42 = Button(self.page4, width=15, height=1, text="Capture", fg='white',bg="#02b3e5", font=("Times", 12),
           relief='raise',command = self.video_capture)
        self.button42.grid(row=2, column=1)

        self.button43 = Button(self.page4, width=15, height=1, text="Cancel", fg='white',bg="#02b3e5", font=("Times", 12),
           relief='raise',command = self.backtoFirst)
        self.button43.grid(row=2, column=2)
        self.video_loop(self.data2)
       

    def video_capture(self):
        self.face_locations=[]
        self.face_encodings=[]
        success, img = self.camera.read()  # read fram from camera
        if success:
            #for tracking facial landmark:
            while self.face_encodings==[] and self.face_locations==[]:
                small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
                # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                rgb_small_frame = small_frame[:, :, ::-1]
                self.face_locations = face_recognition.face_locations(rgb_small_frame)
                self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)
            

    def video_loop(self, panela):

        success, self.img = self.camera.read()  # read fram from camera
        if success:
            #for displaying in page:
            # convert BGR to RGB
            cv2image = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGBA)  
            # convert frame to image.
            current_image = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=current_image)
            panela.imgtk = imgtk
            panela.config(image=imgtk)
            self.root.after(1, lambda: self.video_loop(panela))

    def submitface(self):
        self.username1=self.user_box.get()
        self.password1=self.password_box.get()
        #print(self.username1)
        #print(self.password1)
        #print(self.face_encodings)
        #print(type(self.face_encodings))
        #print(len(self.face_encodings))
        #print(self.face_locations)
        if len(self.face_encodings)>0:
            result=Query_Data_Users(self.username1, self.password1,self.face_encodings[0])
            if result==True:
                print("good")
                self.createWelcome()
        else:
            return

    def createWelcome(self):
        self.page4.destroy()
        self.page1.pack_forget()
        # release camera and windows
        self.camera.release()
        cv2.destroyAllWindows()
        self.page5=Frame(self.root,bg='white')
        self.page5.pack()
        label=Label(self.page5, text="Welcome      " +self.username1,bg='white',fg="#02b3e5", font=('Times', 20)).pack()
        image = Image.open("1.jpg")
        photo = ImageTk.PhotoImage(image = image)
        self.data1 = Label(self.page5,  width=780,image = photo)
        self.data1.image = photo
        self.data1.pack(padx=5, pady=5)

    def retake(self):
        return


    def backtoFirst(self):
        self.page4.destroy()
        self.page1.pack()
        # release camera and windows
        self.camera.release()
        cv2.destroyAllWindows()

    def createSignupPage(self):
        global frame2
        #self.page1.pack_forget()
        #self.page2=Frame(self.root, bg="white")
        self.page2=Toplevel(self.root,bg="white")
        #self.page2.pack()
        frame2=LabelFrame(self.page2,bg='white',text="", padx=10,pady=10,borderwidth=3)
        #distance between window and frame(outside the frame)
        frame2.pack(padx=20,pady=20)
        self.label2=Label(frame2,text="Create your account",bg='white',fg="#02b3e5",font=("Times", 16))
        self.label2.grid(row=0,column=0,columnspan=2,pady=10,padx=10)
        #create username
        self.user_label2=Label(frame2,text="User Name *",bg='white')
        self.user_label2.grid(row=1,column=0,pady=8,padx=10)
        self.user_box2=Entry(frame2,width=20)
        self.user_box2.grid(row=1,column=1,padx=20)
        self.remind1_text="You can use letters,numbers&periods"
        self.remind1=Label(frame2,text=self.remind1_text, font=("Times",10), bg='white')
        self.remind1.grid(row=2,column=1)

        #create password
        self.password_label2=Label(frame2,text="Password *",bg='white')
        self.password_label2.grid(row=3,column=0,padx=10,pady=20)
        self.password_box2=Entry(frame2,show="*",width=20)
        self.password_box2.grid(row=3,column=1,padx=20)
        
        #confirm password
        self.password_label22=Label(frame2,text="Confirm Password *",bg='white')
        self.password_label22.grid(row=4,column=0,padx=10)
        self.password_box22=Entry(frame2,show="*",width=20)
        self.password_box22.grid(row=4,column=1,padx=20,pady=15)
     

        self.remind2_text="Use 8 to 20 characters with a mix of upper and lower letters, numbers & symbols(?,!_)"
        self.remind2=Label(frame2,text=self.remind2_text, font=("Times",10), bg='white')
        self.remind2.grid(row=5,column=0,columnspan=2)

        #create show password checkbox
        self.var2=StringVar()
        self.checkbox2=Checkbutton(frame2,text="Show Password",font=("Times",9),bg='white',variable=self.var2,
           onvalue="On",offvalue="Off",command=self.toggle_password2)
        self.checkbox2.deselect()
        self.checkbox2.grid(row=6,column=0,pady=20,padx=10)

        #self.my_image_label=Label(frame2,image=self.my_image).grid(row=8,column=0,pady=20,padx=10)
        self.upload=Button(frame2,text="Upload Image *",fg='white',bg="#02b3e5",font=("Times",10) , command=self.openImage)
        self.upload.grid(row=7,column=0,pady=10,padx=0)

        self.signup=Button(frame2,text="Submit",width=25,bg='#02b3e5',fg='white',command=self.submit)
        self.signup.grid(row=11,column=0,columnspan=2, pady=30)
        
        self.back=Button(frame2,text="Return to sign in ",width=25,bg='#02b3e5',fg='white',command=self.backFirst)
        self.back.grid(row=13,column=0,columnspan=2, pady=30)

        self.labels=[]
        self.labels2=[]
        self.labels3=[]
        self.labels4=[]
        self.labels5=[]
        self.flabel=Label()
        self.labels.append(self.flabel)
        self.labels2.append(self.flabel)
        self.labels3.append(self.flabel)
        self.labels4.append(self.flabel)
        self.labels5.append(self.flabel)

    def openImage(self):
        
        try:
            self.imagename=filedialog.askopenfilename(initialdir="",title="Select A File",filetypes=(("jpg files","*.jpg"),\
                ("all files","*.*"),("jpeg files","*.jpeg"),("png files","*.png")))
            self.my_image=ImageTk.PhotoImage(Image.open(self.imagename))
            #display image
            self.imagePage()
            self.file_label=Label(frame2,text=self.imagename, font=("Times",9), bg='white')
            #display imagefile path
            self.labels3.append(self.file_label)
            self.labels3[1].grid(row=7,column=1)
            self.labels3[0].grid_forget()
            self.labels3.remove(self.labels3[0])
        except Exception as e:
            print(e)
            pass


    #display image file
    def imagePage(self):
        self.page3=Toplevel(self.root,bg="white")
        self.my_image_label=Label(self.page3,image=self.my_image).pack()
        
    #check username, password, encoding and submit
    def submit(self):        
        self.username2=""
        self.username2=self.user_box2.get()
        self.password2=""
        self.password22=""
        self.image_face_encoding=[]
        self.password2=self.password_box2.get()
        self.password22=self.password_box22.get()
        self.user_exist=Query_Data_Users(username=self.username2)
        #print (self.username2)
        #print (self.user_exist)
        user_valid=userValid(self.username2)
        if self.user_exist==True:
            textcon="That username is taken. Try another."
        elif self.username2=="":
            textcon = " Choose a username"
        elif user_valid != "valid username":
            textcon = user_valid
        else:
            textcon = ""  
        self.labelend1=Label(frame2,text=textcon,fg="red", font=("Times",10), bg='white')
        self.labels.append(self.labelend1)
        self.labels[1].grid(row=8,column=0,columnspan=2)
        self.labels[0].grid_forget()
        self.labels.remove(self.labels[0])
        pas_valid=passValid(self.password2)
        if self.password2!=self.password22:
            textcon="Those passwords didn't match.Try again."
        elif self.password2=="":
            textcon="Choose a password to protect your account."
        elif pas_valid != "valid password":
            textcon=pas_valid
        else:
            textcon=""
        self.labelend2=Label(frame2,text=textcon,fg="red", font=("Times",10), bg='white')
        self.labels2.append(self.labelend2)
        self.labels2[1].grid(row=9,column=0,columnspan=2)
        self.labels2[0].grid_forget()
        self.labels2.remove(self.labels2[0])
        
        if self.imagename=="" :
            textcon1="Picture of user did not upload. Try again." 

        elif (self.imagename.endswith("png") or self.imagename.endswith("jpg") or self.imagename.endswith("jpeg")):

            self.image = face_recognition.load_image_file(self.imagename)
            
            self.image_face_encoding = face_recognition.face_encodings(self.image)
            if len(self.image_face_encoding)==0:
                textcon1="Wrong picture, please load a picture of user's frontal face"
            else:
                textcon1=""
                self.image_face_encoding=self.image_face_encoding[0]
        self.labelend3=Label(frame2,text=textcon1,fg="red", font=("Times",10), bg='white')
        self.labels4.append(self.labelend3)
        self.labels4[1].grid(row=10,column=0,columnspan=2)
        self.labels4[0].grid_forget()
        self.labels4.remove(self.labels4[0])


        if  self.user_exist==False and self.password2==self.password22 and len(self.image_face_encoding)!=0\
         and pas_valid == "valid password" and user_valid =="valid username":
               
            result = Insert_Data_Users(self.username2,self.password2,self.image_face_encoding)
            if result ==True:
                textcon="Register Successful"
            else:
                textcon="Register Failed"
            self.labelreg= Label(frame2,text=textcon,bg="white",fg="#02b3e5", font=("Times",10) )
            self.labels5.append(self.labelreg)
            self.labels5[0].grid_forget()
            self.labels5[1].grid(row=12,column=0,columnspan=2)
            self.labels5.remove(self.labels5[0])


    def backFirst(self):
        self.page2.destroy()
        self.page1.pack()
        
    def toggle_password2(self):
       
        if self.var2.get()=="Off":
            self.password_box2.config(show="*")
            self.password_box22.config(show="*")

        else:
            self.password_box2.config(show="")

            self.password_box22.config(show="")
    def toggle_password(self):
       
        if self.var.get()=="Off":
            self.password_box.config(show="*")
        else:
            self.password_box.config(show="")
if __name__ == '__main__':
    

    demo = APP()



    


