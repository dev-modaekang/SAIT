import os, cv2,ssl, smtplib
from PIL import Image
import numpy as np
import face_recognition
import datetime
from tkinter import *
from tkinter import messagebox
import shutil
from mysql_functions import *
from logger import *
import threading
import time
from playsound import playsound




def alert():
   playsound('drip.ogg')    

def email_sender(name,date,time):
    
    gmail_user = "issnotification7"
    gmail_pass = "Notifier9000"

    sender = gmail_user
    to = "exozeeed@gmail.com"
    txt = name + str(date)+str(time)+"detected!"
    if name.startswith("Unk"):
        subject = "Unknown Person Alert!!!"
    else:
        subject = " Foe Alert!!!"  
    email_txt = 'Subject: {}\n\n{}'.format(subject, txt)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_pass)
        server.sendmail(sender, to,email_txt)
        server.close()
        print ('Email sent!')
    except Exception as e:
        print(e)
        print ('Something went wrong...')

def init():
    global known_face_name, known_face_encodings,unknown_face_name,unknown_face_encodings
    global video_capture, face_locations, face_encodings,face_names,process_this_frame
    Init_Face_Table()
    #load faces and names from database: 
    #table face is for known person, unknown is for unknown person
    known_face_name,known_face_encodings=Load_Names_Faces("face")
    unknown_face_name,unknown_face_encodings=Load_Names_Faces("unknown")

    #logging levels: debug,info,warning,error and critical
    #camera captured faces info: friends , warning: unknown, critical:foe
    setup_logger('log_camera','camera.log')   
    #insert record into database info:friends,warning: unknown, critical:foe
    setup_logger('log_database', 'database.log')

    video_capture = cv2.VideoCapture(0)

    face_locations = []
    face_encodings = []
    face_names = []
    

def face_capture():
    global frame, face_names,face_locations, talert
    # Grab a single frame of video
    ret, frame = video_capture.read()   
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding,tolerance=0.45)
        name=""
        now = datetime.datetime.now()
        date = now.strftime('%y-%m-%d')
        time = now.strftime('%H:%M:%S')
        d_t = now.strftime('%y-%m-%d-%H:%M:%S')
        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_name[first_match_index]
            if "." in name:
                fname,lname=name.split(".")
                lname=lname[:-1]
                # foes name endswith 0; friend name endswith 1.
                if name.endswith("0"):
                    logger(("Found a foe!"+str(name[:-1])), 'critical', 'camera')
                    #start a new thread for sound the alarm
                    talert=threading.Thread(target=alert)
                    talert.start()
                   
                else:
                    logger(("Found a friend!"+str(name[:-1])), 'info', 'camera')  
                #found a known face, query database, if this person signed in today
                #result is a list
                result=Query_Data_Check( fname, date)
                #print (result)
                #if can not find the person signed in today, then store this person info into check_table
                if len(result)== 0:
                        #foe is end with (isfriend0)
                    if name.endswith("0"):
                        Insert_Data_Check(fname,lname,date, time)
                        logger(("insert into database check_table "+str(name[:-1])), 'critical', 'database')
                        #send email for alerting 
                        tmail=threading.Thread(target=email_sender,args=(name,date,time))
                        tmail.start()
                    else:
                         
                        logger(("check in successful"+str(name[:-1])), 'info', 'camera')
                        Insert_Data_Check(fname,lname,date, time)
                        logger(("insert into database check_table "+str(name[:-1])), 'info', 'database')              
        else:
            name = "Unknown"+str(d_t)
            logger(("found a unknown "+str(name)), 'warning', 'camera')
            #check with unknown faces:
            matches = face_recognition.compare_faces(unknown_face_encodings, face_encoding,tolerance=0.45)
            if True in matches:
                first_match_index = matches.index(True)
                name = unknown_face_name[first_match_index]
            else:
                filename="unknown/"+name+".jpg"
                Insert_Data_Unknown(name,face_encoding,date, time,filename)
                logger(("insert into database  unknown "+str(name)), 'warning', 'database')
                unknown_face_encodings.append(face_encoding)
                unknown_face_name.append(name)
        #store names into list for latter display 
        face_names.append(name)
            

def face_display():
    # Display the results
    global frame, face_locations,face_names
    
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        font = cv2.FONT_HERSHEY_DUPLEX
        stroke = 2
        #    print name in color green if friend
        if name.endswith("1")and (name.startswith("Unknown")==False): 
            color = (0,255,0)  #color=green
            name = "friend_"+name

        elif name.startswith ("Unknown"):
            color = (255,0,0) #color=blue
            #crop face to file path 
            saveImg = frame
            #output the img to  local
            filename="unknown/"+name+".jpg"
            cv2.imwrite(filename, saveImg,[int(cv2.IMWRITE_PNG_COMPRESSION), 9])

        else:
            color = (0,0,255) #color=red
            name = "foe_"+name
        # display name face frame in various color
        cv2.putText(frame, name, (left + 6, top -16), font, 1.0, color, stroke,1)
        cv2.rectangle(frame, (left, top), (right, bottom),  color, 2)

def main():
    init()
    while True:
        face_capture()
        face_display()
        # Display the resulting image
        cv2.imshow('Video', frame)
        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
         # Release handle to the webcam
            video_capture.release()
            cv2.destroyAllWindows()
            break
if __name__ == "__main__":
    main()



