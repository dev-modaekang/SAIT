import mysql.connector
import face_recognition
import pickle
import datetime
import os
import hashlib, binascii, os
from logger import *
from hash import *

friends=["Jun Wang","Modea Kong","Vincent Saban"]
foe=["Donal Trump"]


#insert record into database info:friends,warning: unknown, critical:foe
setup_logger('log_database', 'database.log')
                

# if error  unread result found, use buffered=True when connect
# create mysql connection
def Mysql_Init():
    conn = mysql.connector.connect(
            # ip address of database
            host="localhost",
            # username of database
            user="root",
            # password 
            password="mplftw20",
            # name of the database
            database="iss",
            # port number of the database
            port=3306,
            # utf8 encoding of the database
            charset="utf8",
            auth_plugin='mysql_native_password',
            buffered=True
        )
    # create cursor object by calling cursor()
    cursor = conn.cursor()
    return conn, cursor

# close database connection
def DataBase_Close(cursor,conn):
    cursor.close()
    conn.close()

#create tables and load known faces into face table
def Init_Face_Table():
    Check_Tables()
    Load_Images()

# check if the tables exist
def Check_Tables( ):
    conn, cursor = Mysql_Init()
    # existance of tables face  and  check_in 
    cursor.execute("show tables like 'face'")
    result = cursor.fetchone()
    if result is None:
        Create_Table_Face()
    cursor.execute("show tables like 'check_in'")
    result = cursor.fetchone()
    if result is None:
        Create_Table_Check()
    cursor.execute("show tables like 'users'")
    result = cursor.fetchone()
    if result is None:
        Create_Table_Users()
   
    cursor.execute("show tables like 'unknown'")
    result = cursor.fetchone()
    if result is None:
        Create_Table_Unknown()
    cursor.execute("show tables like 'usergroups'")
    result = cursor.fetchone()
    if result is None:
        Create_Table_Groups()
    DataBase_Close(cursor,conn)

# create personal face database 
def Create_Table_Face():
    conn, cursor = Mysql_Init()
    sql = """create table face (
        id int auto_increment primary key, 
        fname varchar(40) not null, 
        lname varchar(40) not null, 
        encoding blob not null,
        isfriend boolean default 0,
        isdelete boolean default 0 )charset utf8;"""
    try:
        # execute sql  
        cursor.execute(sql)
         # commit to database,make changes 
        conn.commit()
        logger(" table face created", 'info', 'database')
    except:
        #if errors occur, cancel all changes
        conn.rollback()
    DataBase_Close(cursor,conn)


# create table for check in 
def Create_Table_Check():
    conn, cursor = Mysql_Init()
    sql = """create table check_table(
    id int primary key auto_increment,
    fname varchar(45) not null,
    lname varchar(45) not null,
    date date not null, 
    time time not null)charset utf8;
   """
    try:
        cursor.execute(sql)
        conn.commit()
        logger(" table check_table created", 'info', 'database')
    except:
        conn.rollback()
    DataBase_Close(cursor,conn)

# create table for users
#gid default 1 for basic users
def Create_Table_Users():
    conn, cursor = Mysql_Init()
    sql = """create table users(
    id int primary key auto_increment,
    username varchar(45) not null,
    password varchar(192) not null,
    encoding blob not null,
    gid int default 1
    )charset utf8;
   """
    try:
        cursor.execute(sql)
        conn.commit()
        logger(" table users created", 'info', 'database')
    except:
        conn.rollback()
    DataBase_Close(cursor,conn)

# create personal face database 
def Create_Table_Unknown():
    conn, cursor = Mysql_Init()
    sql = """create table unknown (
        id int auto_increment primary key, 
        name varchar(40) not null,  
        encoding blob not null,
        date date not null, 
        time time not null,
        filename varchar(80) not null
        )charset utf8;"""
    try:
        cursor.execute(sql)
        conn.commit()
        logger(" table unknown created", 'info', 'database')
    except:
        conn.rollback()
    DataBase_Close(cursor,conn)

def Create_Table_Groups():
    conn, cursor = Mysql_Init()
    sql = """create table usergroups(
        id int auto_increment primary key, 
        name varchar(40) not null,
        gid int not null
        )charset utf8;"""
        
    try: 
        cursor.execute(sql)
        conn.commit()
        logger(" table usergroups created", 'info', 'database')
    except Exception as e:
        #if errors occur
        conn.rollback()
        #print(e)
    #except:
        #conn.rollback()
    DataBase_Close(cursor,conn) 


# load image , read the feature of face(encoding)and write to database
def Load_Images():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))   
    image_dir = os.path.join(BASE_DIR, "images")
    for root, dirs, files, in os.walk(image_dir):
        for file in files:
            #print(file)
            if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
                input_image= os.path.join(root, file)
                label = os.path.basename(os.path.dirname(input_image))
                fname=label.split("_")[0]
                lname=label.split("_")[1]
                fullname=fname+' '+lname
                # load image to a numpy nparray
                image = face_recognition.load_image_file(input_image)
                # return 128 facial landmarks for each face in the image 
                # if the image has more than one face, take the first one index 0
                # as the most clear face recognized.
                image_face_encoding = face_recognition.face_encodings(image)[0]
                #print (image_face_encoding) 
                #pickle encoding, convert PYTHON ndarray to MYSQL type 
                face_pickle=pickle.dumps(image_face_encoding)          
                # name of the face recognized(fname.lname).
                # store the face feature string to database.
                if fullname in friends:
                    isfriend=1
                else:
                    isfriend=0
                #check if the person exist
                result=Query_Data_Face(fname,lname)
                
                #no matching record found, then insert one.
                if len(result)==0:
                    Insert_Data_Face(fname,lname,face_pickle,isfriend)
#insert one record from an image file                    
def Add_New_Face_Manual(file,fname,lname, isfriend=1):
    if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
        image = face_recognition.load_image_file(file)
        image_face_encoding = face_recognition.face_encodings(image)[0]
        #print(file)
        #print(image_face_encoding)

        #pickle encoding, convert PYTHON ndarray to MYSQL type 
        face_pickle=pickle.dumps(image_face_encoding)          
        # name of the face recognized(fname.lname).
        # store the face feature string to database.
        fullname= fname +" "+lname
        if isfriend ==1:
            friends.append(fullname)
        else:
            foe.append(fullname)
        #check if the person exist
        result=Query_Data_Face(fname,lname)
        #no matching record found, then insert one.
        if len(result)==0:
            Insert_Data_Face(fname,lname,face_pickle,isfriend)
    else:
        print("wrong file, please use an image file")       

def Query_Data_Face(fname,lname,encoding=[]):
    # SQL insert name and facial landmarks
    conn, cursor = Mysql_Init()
    if encoding==[]:
        sql = "select * from face where fname='%s' and lname='%s';"% (fname,lname)
    else:
        sql = "select * from face where fname='%s' and lname='%s' and encoding='%s';"% (fname,lname,encoding)
    try:
        cursor.execute(sql)
        conn.commit()
        results = cursor.fetchall()
        return results
    except Exception as e:
        #if errors occur
        conn.rollback()
        #print(e)
    DataBase_Close(cursor,conn)
     
def Query_Data_Check( fname='', date=''):
    #query check in records
    conn, cursor = Mysql_Init()
    if date == '':
        if fname == '':
            #query all check in records
            sql = "select * from check_table;"
        else:
            #query all check in records of one person
            sql = "select * from check_table where fname = '%s';" % (fname)
        cursor.execute(sql)
    else:   
        if fname == '':
            #query all check in records of one day
            sql = "select * from check_table where date='%s';"%date
        else:
            #query check in record for one person in one day
            sql = "select * from check_table where date='%s' and fname = '%s';" % (date,fname)
        cursor.execute(sql)
    
    # submit to database and fetch all entries 
    conn.commit()
    results = cursor.fetchall()
    return results
    """for i in results:
        (id, fname,lname,date,time )=i
        #print ("id : "+str(id) +"\t"+"fname: "+fname+"."+lname+ "\t "+"date-time"+date+time)"""
    DataBase_Close(cursor,conn)

def Query_Data_Users (username,password="", encoding=[]):
    conn, cursor = Mysql_Init()
    
    #encoding's type is  numpy.ndarray 
    #print("what type : "+str(type(encoding)))
    if (encoding==[]and len(password)>0):
        query_sql ="select password from users where username='%s' ;"%(username)
        cursor.execute(query_sql,(username))
        try:
            conn.commit()
            #result is a tuple with one element
            result=cursor.fetchone()
            if  (verify_password(result[0], password)) :
                return True
            else: 
                return False
        except Exception as e:
            conn.rollback()
            #print(e)
            return False
    #verify username exists for signup
    #print (username)
    elif len(password)==0 and (len(encoding))==0:
        query_sql ="select * from users where username='%s' ;"%(username)
        cursor.execute(query_sql,(username))
        try:
            conn.commit()
            result=cursor.fetchone()
            if result==None:
                
                return False
            else:
                return True
        except Exception as e:
            conn.rollback()
            #print(e)
            return False

    else:
    #for facial authentication
        stored_encodings=[]
        query_sql ="select * from users where username='%s' ;"%(username)
        #print(query_sql)
        cursor.execute(query_sql,(username))
        try:
            conn.commit()
            #result is a tuple with one element
            result=cursor.fetchone()
            id,stored_username,stored_password,stored_encoding, stored_gid =result
                   
            if  (verify_password(stored_password, password)) :
                stored_encoding=pickle.loads(stored_encoding)
                stored_encodings.append(stored_encoding)
                matches = face_recognition.compare_faces(stored_encodings, encoding,tolerance=0.45)
                if matches[0]==True:
                    return True
                else: 
                    return False
        except Exception as e:
            conn.rollback()
            #print(e)
            return False
    
    DataBase_Close(cursor,conn)

def Query_Data_Unknown(encoding):
    # SQL query for unknown facial landmarks
    conn, cursor = Mysql_Init()
    sql = "select * from unknown where encoding='%s';"% (encoding)
    try:
        cursor.execute(sql)
        conn.commit()
        results = cursor.fetchall()
        return results
    except Exception as e:
        conn.rollback()
        #print(e)
    DataBase_Close(cursor,conn)

# save known face feature to database
def Insert_Data_Face( fname,lname,encoding,isfriend):
    # SQL insert name and facial landmarks
    conn, cursor = Mysql_Init()
    #print (fname+ '\t'+ lname+'\t'+str(isfriend) +'\n'+str(encoding))
    insert_sql = "insert into face(fname,lname,encoding,isfriend) values(%s,%s,%s,%s)"
    #print(insert_sql)
    try: 
        cursor.execute(insert_sql, (fname, lname, encoding,isfriend)) 
        conn.commit()
        logger(" A new face added to table face  "+fname+" "+lname, 'info', 'database')
    except Exception as e:
        conn.rollback()
    DataBase_Close(cursor,conn)  

#save user info into database
def Insert_Data_Users(username,password,encoding,gid=0):
    conn, cursor = Mysql_Init()
    #password encryption
    password=hash_password(password)
    #converting cv2 facial landmark into pickled string   
    face_pickle=pickle.dumps(encoding) 
    insert_sql = "insert into users(username,password,encoding) values(%s,%s,%s)"
    try:
        cursor.execute(insert_sql, (username,password,face_pickle)) 
        conn.commit()
        logger(" A new user added to table users "+username, 'info', 'database')
        return True
    except Exception as e:
        #if errors occur
        conn.rollback()
        return False
    DataBase_Close(cursor,conn)

#save personel check in time 
def Insert_Data_Check(fname,lname,date, time):
    conn, cursor = Mysql_Init()
    insert_sql = "insert into check_table  (fname,lname,date, time)values(%s,%s,%s,%s)" 
    try:
        cursor.execute(insert_sql,(fname,lname,date,time))
        conn.commit()
        print("check in successed")
    except Exception as e:
        conn.rollback()
        #print(e)
    DataBase_Close(cursor,conn)

def Insert_Data_Unknown(name,encoding,date, time,filename):
    conn, cursor = Mysql_Init()
    insert_sql = "insert into unknown (name,encoding,date, time,filename)values(%s,%s,%s,%s,%s);" 
    #pickle encoding, convert PYTHON ndarray to MYSQL type 
    face_pickle=pickle.dumps(encoding) 
    try:
        cursor.execute(insert_sql,(name,face_pickle,date, time,filename)) 
        conn.commit()
    except Exception as e:
        conn.rollback()
        #print(e)
    DataBase_Close(cursor,conn)
def Insert_Data_Groups():
    conn, cursor = Mysql_Init()
    insert_sql = "insert into usergroups (name,gid)values(%s,%s);" 
    try:
        cursor.execute(insert_sql,("Basic","1"))
        cursor.execute(insert_sql,("Admin","2"))
        cursor.execute(insert_sql,("IT","3"))
        cursor.execute(insert_sql,("Financial","4")) 
        conn.commit()
    except Exception as e:
        #if errors occur
        conn.rollback()
        #print(e)
    DataBase_Close(cursor,conn)

def Load_Names_Faces(tablename):
    conn, cursor = Mysql_Init()
    # SQL query facial landmarks 
    queryall_sql="select * from %s;" %(tablename)
    names=[]
    encodings=[]
    try:
        # query command to check all rows
        # load the encoding into a np array
        cursor.execute(queryall_sql)
        rows=cursor.fetchall()
        #Get the results
        for row in rows:
            if tablename=="face":
                ##every row is in a tuple, unpack the tuple
                (id,fname,lname,encoding,isfriend,isdelete)=row
                #save names into a list
                names.append(fname+'.'+lname+str(isfriend))
            elif tablename=="unknown":
                (id,name,encoding,date,time,filename)=row
                names.append(name+str(date)+str(time))
            #load pickle -face encoding to a numpy  array
            encoding=pickle.loads(encoding)
            #save the encoding into list
            encodings.append(encoding)
            #print(names)
        conn.commit()
    except Exception as e:
        #if errors occur
        conn.rollback()
    DataBase_Close(cursor,conn)
    return names,encodings

if __name__ == '__main__':
    Check_Tables( )
    #Create_Table_Groups()
    #Insert_Data_Groups()
    #user=Query_Data_Users(username="jerry",password="jerry")
    #print(user)
    #user=Query_Data_Users(username="jkjfkoejf")
    #print(user)
    #Load_Images()
    #Add_New_Face_Manual("Will_Smith.jpg","Will","Smith",1)
    #Insert_Data_Check("Jun","Wang","20-02-21","00:09:47")
    #names,faces=Load_Names_Faces()
    #print (names)
    #print (faces)

