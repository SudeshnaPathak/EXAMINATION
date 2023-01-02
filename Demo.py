import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

python_marks=""
Math_marks=""
Physics_marks=""
Chemistry_marks=""
Biology_marks=""
English_marks=""
BEE_marks=""
EM_marks=""
cse=""
cseai=""
cseaiml=""
it=""
ece=""
me=""
ee=""
gr = [ 0 , 0 , 0 , 0 , 0 , 0 ]
'''List for calculating the no of students in each grade'''
pct =[]
'''Empty list to store the percentage of all the students'''
nm = []
'''Empty list to store the names of all the students'''
python=[]
math=[]
physics=[]
chemistry=[]
biology=[]
english=[]
bee=[]
em=[]
'''Empty lists to store the marks of specific subjects'''


def add(n):
    x=0
    for i in n:
        if( i != "null"):
           x = x + int(i)
    return x

def percent(num):    
    if(stream.lower()=='cse' or stream.lower()== 'cseai' or stream.lower() == 'cseaiml'):
       num = (num * 100)/800
    elif(stream.lower()== 'it' or stream.lower()== 'ece' or stream.lower() == 'me' or stream.lower() == 'ee'):
        num =(num * 100)/700
    return num

def grade(num):
    pct.append(num)
    
    if(num >= 90):
        gr[0]=gr[0]+1
        return("You have passed with grade A")        
    elif(num >= 80):
        gr[1]=gr[1]+1
        return("You have passed with grade B")
    elif(num >= 70):
        gr[2]=gr[2]+1
        return("You have passed with grade C")        
    elif(num >= 60):
        gr[3]=gr[3]+1
        return("You have passed with grade D")        
    elif(num >= 50):
        gr[4]=gr[4]+1
        return("You have passed with grade E")        
    elif(num < 40):
        gr[5]=gr[5]+1
        return("You have failed with grade F")

def choice(stream):
    if(stream.lower()=='cse' or stream.lower()=='cseai' or stream.lower()=='cseaiml'):
        return("C001:C002:C003:C004:C005:C006:C007:C008")
    elif(stream.lower()=='it' or stream.lower()=='ece' or stream.lower()=='me'or stream.lower()=='ee'):
        return("C002:C003:C004:C005:C006:C007")
    
print('\n','Computer Sience and Engineering : CSE','\n',
      'c : CSEAI','\n',
      'Computer Sience and Engineering and Artificial Intelligence and Machine Learning : CSEAIML','\n',
      'Information Technology : IT','\n',
      'Electrical and Communications Engineering : ECE','\n',
      'Mechanical Engineering : ME','\n',
      'Electrical Engineering :EE','\n')
print("Please write all the stream name in short form as mentioned above and in capital letters only!!!")
print()

w = []
y = []
z = []
v = []

student_no=int(input("Enter the no. of students whose data you want to input : "))
print()
p = open("STUDENT.csv","w",newline="")
q = csv.writer(p)
q.writerow(["Student ID","Name","Class Roll Number","Batch ID"])
for i in range(student_no):
    name=input("Enter Student's Name : ")
    nm.append(name)
    batch=input("Enter Student's Batch(e.g. 2022-26) : ")
    stream=input("Enter Student's Stream(e.g. CSE) : ")
    roll=input("Enter Student's Class Roll Number : ")
    batch_id=stream+batch[2:4]
    student_id=batch_id+roll
    batch_name=stream+ " " +batch
    student=[ student_id , name , roll , batch_id]
    q.writerow(student)
    
    y.append(batch_id)
    z.append(student_id)
    w.append(stream)
    v.append(batch_name)
    
    print()
    print("The subjects are [Python Programming,Math,Physics,Chemistry,Biology,English,BEE,Engineering Mechanics]")
    print("The marks obtained is out of 100")
    print("Python Programming is not applicable for IT , ECE , ME & EE students , so Enter marks :null")
    print("If the Student remains absent in examination , Enter marks : 0")
    print("Enter the marks of the subjects in the specified sequence")
    l=[]
    for i in range(8):
        k=input("Enter marks:")
        l.append(k)
        
    if(l[0] != "null"):
       python.append(l[0])
    else:
        python.append("0")
    math.append(l[1])
    physics.append(l[2])
    chemistry.append(l[3])
    biology.append(l[4])
    english.append(l[5])
    bee.append(l[6])
    em.append(l[7])
    
    if(l[0]!= "null"):       
        python_marks=python_marks + " " +student_id+":"+l[0]    
    Math_marks=Math_marks+ " " +student_id+":"+l[1]                                            
    Physics_marks=Physics_marks+ " " +student_id+":"+l[2]    
    Chemistry_marks=Chemistry_marks+ " " +student_id+":"+l[3]   
    Biology_marks=Biology_marks+ " " +student_id+":"+l[4]   
    English_marks=English_marks+ " " +student_id+":"+l[5]    
    BEE_marks=BEE_marks+ " " +student_id+":"+l[6]   
    EM_marks=EM_marks+ " " +student_id+":"+l[7]

    
    if(stream.lower()=="cse"):
        cse = cse + "  " + batch_id
    elif(stream.lower()=="cseai"):
        cseai = cseai + "  " + batch_id
    elif(stream.lower()=="cseaiml"):
        cseaiml = cseaiml + "  " + batch_id
    elif(stream.lower()=="it"):
        it = it + "  " + batch_id
    elif(stream.lower()=="ece"):
        ece = ece + "  " + batch_id
    elif(stream.lower()=="me"):
        me = me + "  " + batch_id
    elif(stream.lower()=="ee"):
        ee = ee + "  " + batch_id
        
    print()
    f = open("Report Card.txt","w")
    f.writelines(['Name of the student :', name, '\n',
                  'Class Roll of the student :',roll,'\n',
                  'Stream of the student :',stream,'\n',
                  'Your Batch ID is:',batch_id,'\n',
                  'Your Student ID is :',student_id,'\n',
                  '\n',
                  'Marks obtained in Python is :',l[0],'\n',
                  'Marks obtained in Math is :',l[1],'\n',
                  'Marks obtained in Physics is :',l[2],'\n',
                  'Marks obtained in Chemistry is :',l[3],'\n',
                  'Marks obtained in Biology is :',l[4],'\n',
                  'Marks obtained in English is :',l[5],'\n',
                  'Marks obtained in BEE is :',l[6],'\n',
                  'Marks obtained in Mechanical Engineering is :',l[7],'\n',
                  'Total marks:',str(add(l))," ",'Percentage:',str(percent(add(l))),"%",'\n',
                  grade(percent(add(l))),'\n'])
                   
    f = open("Report Card.txt","r")
    res = f.read()
    print()
    print("REPORT CARD")
    print()
    print(res)

r = open("COURSE.csv","w",newline="")
s = csv.writer(r)
course=[['Course ID' ,'Course Name' , 'Marks Obtained'],
        ['C001','Python Programming',python_marks],
        ['C002','Math',Math_marks],
        ['C003','Physics',Physics_marks],
        ['C004','Chemistry',Chemistry_marks],
        ['C005','Biology',Biology_marks],
        ['C006','English',English_marks],
        ['C007','BEE',BEE_marks],
        ['C008','Mechanical Engineering',EM_marks]]
s.writerows(course)

m = open("DEPARTMENT.csv","w",newline="")
n = csv.writer(m)
department = [['Department ID' , 'Department Name' , 'List of Batches'],
              ['CSE','Computer Sience and Engineering' , cse],
              ['CSEAI','Computer Sience and Engineering and Artificial Intelligence' , cseai],
              ['CSEAIML','Computer Sience and Engineering and Artificial Intelligence and Machine Learning ',cseaiml],
              ['IT','Information Technology ',it],
              ['ECE','Electrical and Communications Engineering ',ece], 
              ['ME','Mechanical Engineering',me],
              ['EE','Electrical Engineering',ee]]
n.writerows(department)

pc = pct.copy()
for i in y:
    j = 0
    g = -1
    for k in z:
        g = g+1
        if(i == k[0:len(k)-2]):
           j = j+1
           if(j>1):
              y.pop(g)
              z.pop(g)
              w.pop(g)
              v.pop(g)
              pc[y.index(i)]= pc[y.index(i)]+pc[g]
              pc.pop(g)
              z[y.index(i)]= z[y.index(i)]+ " " +k
    if(j > 0):
       pc[y.index(i)]=pc[y.index(i)]/j
    
length = len(y)
t = open("BATCH.csv","w",newline="")
u = csv.writer(t)
u.writerow(["Batch ID" , "Batch Name" , "Department Name" , "List of cources" ,"List of Students"])
for i in range(length):
    batch = [ y[i] , v[i] , w[i] , choice(w[i]) , z[i] ]
    u.writerow(batch)

grd = [ 'A' , 'B' , 'C' , 'D' , 'E' , 'F']
X = np.arange(6)
plt.title("Graph showing the No of Students in each grade")
plt.bar(X , gr , color = 'm' , width = 0.5)
plt.xticks(X , grd)
plt.xlabel("Grades")
plt.ylabel("No of Students in each grade")
plt.show()


plt.pie(pct , labels = nm )
plt.title("Percentage of all Students")
plt.show()

plt.plot(y,pc,'b')
plt.xlabel("Batch Name")
plt.ylabel("Average Percentage")
plt.title("Average of Students Vs Batch")
plt.show()

plt.scatter(python , python , color = 'r',label = "Python Programming")
plt.scatter(math , math , color = 'g' ,label = "Math")
plt.scatter(physics , physics , color = 'b', label = "Physics")
plt.scatter(chemistry , chemistry , color = 'c', label = " Chemistry")
plt.scatter(biology ,biology , color = 'm', label = "Biology")
plt.scatter(english , english , color = 'y', label = "English")
plt.scatter(bee ,bee , color = 'k', label= "BEE")
plt.scatter(me, me , color = 'r',marker = ">" , label = "Engineering Mechanics")
plt.legend()
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Marks Vs Subject")
plt.show()













        

    
