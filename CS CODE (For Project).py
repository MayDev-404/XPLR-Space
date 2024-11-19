import mysql.connector as mys
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import*
from PIL import Image,ImageTk,ImageFont,ImageDraw
root=Tk()
root.geometry("1000x1000")
image=Image.open(r"C:\Users\mayan\OneDrive\Pictures\explr.jpg")
photo=ImageTk.PhotoImage(image)
a_label=Label(image=photo)
a_label.pack()
root.mainloop()

Areasqdegrees=[]
distance=[]
Namestars=[]
Namecon=[]
Nameplanets=[]
Distanceplanets=[]

#connection
mycon=mys.connect(host='localhost',user='root',password='mayank',database='Xplrspace')
if mycon.is_connected():
    print("Successfully connected")
mycursor=mycon.cursor()

#searching
def searchnamestars():
    nm=input("Enter the star's name to be searched:")
    mycursor.execute("select * from star where Name_of_Star='{0}'".format(nm))
    records=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("No records found")
    else:
        print("No of rows",count)
        for i in records:
            print("\nStar:",i[0],
                  "\nDistance from earth in ly:",i[1],
                  "\nStar Type:",i[2],
                  "\nStage of life:",i[3],
                  "\nPart of Constellation:",i[4])

def searchnameplanets():
    nm=input("Enter the planet's name to be searched:")
    mycursor.execute("Select * from planets where Name='{0}'".format(nm))
    records=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("No records found")
    else:
        print("No of rows",count)
        for i in records:
            print("\nPlanet:",i[0],
                  "\nDistance from Earth in million km:",i[1],
                  "\nNo. of moons:",i[2],
                  "\nLength of year",i[3],
                  "\nNo. of Human Spacecraft:",i[4])

def searchnameastronauts():
    nm=input("Enter the Astronaut's name to be searched:")
    mycursor.execute("select * from astronauts where Name='{0}'".format(nm))
    records=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("No records found")
    else:
        print("No of rows",count)
        for i in records:
            print("\nName of Astronaut:",i[0],
                  "\nCountry:",i[1],
                  "\nMission:",i[2],
                  "\nage_during_accomplishment:",i[3],
                  "\nAccomplishment:",i[4])

def searchnameconstellations():
    nm=input("Enter the Constellation's name to be searched:")
    mycursor.execute("Select * from constellations where name='{0}'".format(nm))
    records=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("No records found")
    else:
        print("No of rows",count)
        for i in records:
            print("\nConstellation Name:",i[0],
                  "\nBrightest Star:",i[1],
                  "\nArea in square degree:",i[2])

def searchnamegalaxy():
    nm=input("Enter the Galaxies' name to be searched:")
    mycursor.execute("Select * from galaxies where Name='{0}'".format(nm))
    records=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("No records found")
    else:
        print("No of rows",count)
        for i in records:
            print("\nGalaxy's name:",i[0],
                  "\nDiameter in ly:",i[1])

#area square degrees and name of constellations list formation for graph
def accessdatacons():
    mycursor.execute("select * from constellations")
    mydata=mycursor.fetchall()
    for row in mydata:
        for area in row[-1::]:
            Areasqdegrees.append(area)
        for name in row[0:1]:
            Namecon.append(name)
    print(Namecon)
    print(Areasqdegrees)

#graph plotting of constellations
def graphcons():
    accessdatacons()
    plt.bar(Namecon,Areasqdegrees,width=0.3)
    plt.xlabel("constellations")
    plt.ylabel("area in square degrees")
    plt.show()

#graph of stars:
def accessdatastars():
    mycursor.execute("select * from star")
    records=mycursor.fetchall()
    for row in records:
        for dist in row[1:2]:
            distance.append(int(dist))
        for name in row[0:1]:
            Namestars.append(name)
    print(Namestars)
    print(distance)

def graphstars():
    accessdatastars()
    plt.bar(Namestars,distance,width=0.3)
    plt.xlabel("stars")
    plt.ylabel("distance in light years")
    plt.show()

#graph of planets

def accessdataplanets():
    mycursor.execute("select * from planets")
    records=mycursor.fetchall()
    for row in records:
        for name in row[0:1]:
            Nameplanets.append(name)
        for distnce in row[1:2]:
            Distanceplanets.append(distnce)
    print(Nameplanets)
    print(Distanceplanets)

def graphplanets():
    accessdataplanets()
    plt.bar(Nameplanets,Distanceplanets,width=0.3)
    plt.xlabel("name of planets")
    plt.ylabel("distance in light years")
    plt.show()
#adding records
    
def addrecordsstars():
    ans='yes'
    while ans.lower()=='Yes'.lower():
        starname=input("enter star name to be added:")
        dist=eval(input("enter distance from earth in light years:"))
        typestar=input("enter type of star:")
        stageoflife=input("enter stage of life:")
        partofcons=input("enter constellation name:")
        qry="insert into star values(%s,%s,%s,%s,%s)"
        starlist=[starname,dist,typestar,stageoflife,partofcons]
        mycursor.execute(qry,starlist)
        mycon.commit()
        print("record added")
        ans=input("do you want to add more yes/no?")

def addrecordsplanets():
    ans='yes'
    while ans.lower()=='Yes'.lower():
        planetname=input("enter planet name to be added:")
        dist=eval(input("enter distance from earth in light years:"))
        noofmoons=input("enter no of moons:")
        lengthofyear=input("enter length of year:")
        noofhs=input("enter no of human spacecrafts:")
        qry="insert into Planets values(%s,%s,%s,%s,%s)"
        planetlist=[planetname,dist,noofmoons,lengthofyear,noofhs]
        mycursor.execute(qry,planetlist)
        mycon.commit()
        print("woah, record added")
        ans=input("do you want to add more yes/no?")

def addrecordsastronauts():
    ans='yes'
    while ans.lower()=='Yes'.lower():
        astname=input("enter astronaut name to be added:")
        country=input("enter from which country:")
        mission=input("enter mission:")
        age=int(input("enter age of accomplishment:"))
        accmp=input("enter accomplishment(text):")
        qry="insert into astronauts values(%s,%s,%s,%s,%s)"
        astronautlist=[astname,country,mission,age,accmp]
        mycursor.execute(qry,astronautlist)
        mycon.commit()
        print("woah, record added")
        ans=input("do you want to add more yes/no?")

def addgalaxies():
    ans='yes'
    while ans.lower()=='Yes'.lower():
        glname=input("enter galaxy name to be added:")
        diam=int(input("enter diameter in light year(int):"))
        qry="insert into galaxies values(%s,%s)"
        gllist=[glname,diam]
        mycursor.execute(qry,gllist)
        mycon.commit()
        print("woah, record added")
        ans=input("do you want to add more yes/no?")

def addconst():
    ans='yes'
    while ans.lower()=='Yes'.lower():
        constname=input("enter constellation name to be added:")
        brightstar=input("enter brightest star(text):")
        area=int(input("enter area in light years:"))
        qry="insert into constellations values(%s,%s,%s)"
        constlist=[constname,brightstar,area]
        mycursor.execute(qry,constlist)
        mycon.commit()
        print("woah, record added")
        ans=input("do you want to add more yes/no?")

#deletion of records
        
def deletestar():
    no=input("Enter the name of star to be deleted:")
    mycursor.execute("delete from star where Name_of_Star='{0}'".format(no))
    records=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("No records found")
    else:
        print("No of rows",count)
        for i in records:             #fetchall and fetchmany
            print(i[0],":",i[1],":",i[2],":",i[3],":",i[4])
        ans=input("Do you wish to delete record yes/no:")
        if ans.lower=='Yes'.lower():
            mycursor.execute("Delete from star where Name_of_Star='{0}'".format(no))
            print("Record Deleted")
            mycon.commit()
        else:
            print("No record deleted")

def deleteplanet():
    no=input("Enter the name of planet to be deleted:")
    mycursor.execute("delete from planets where Name='{0}'".format(no))
    records=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("No records found")
    else:
        print("No of rows",count)
        for i in records:             #fetchall and fetchmany
            print(i[0],":",i[1],":",i[2],":",i[3],":",i[4])
        ans=input("Do you wish to delete record yes/no:")
        if ans.lower=='Yes'.lower():
            mycursor.execute("Delete from planets where Name='{0}'".format(no))
            print("Record Deleted")
            mycon.commit()
        else:
            print("No record deleted")

def deleteastronaut():
    no=input("Enter the name of astronaut to be deleted:")
    mycursor.execute("delete from astronauts where Name='{0}'".format(no))
    records=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("No records found")
    else:
        print("No of rows",count)
        for i in records:             #fetchall and fetchmany
            print(i[0],":",i[1],":",i[2],":",i[3],":",i[4])
        ans=input("Do you wish to delete record yes/no:")
        if ans.lower=='Yes'.lower():
            mycursor.execute("Delete from atsronauts where Name='{0}'".format(no))
            print("Record Deleted")
            mycon.commit()
        else:
            print("No record deleted")

def deleteconstellation():
    no=input("Enter the name of constllation to be deleted:")
    mycursor.execute("delete from constellations where name='{0}'".format(no))
    records=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("No records found")
    else:
        print("No of rows",count)
        for i in records:             #fetchall and fetchmany
            print(i[0],":",i[1],":",i[2])
        ans=input("Do you wish to delete record yes/no:")
        if ans.lower=='Yes'.lower():
            mycursor.execute("Delete from constellations where name='{0}'".format(no))
            print("Record Deleted")
            mycon.commit()
        else:
            print("No record deleted")

def deletegalaxy():
    no=input("Enter the name of galaxy to be deleted:")
    mycursor.execute("delete from galaxies where Name='{0}'".format(no))
    records=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("No records found")
    else:
        print("No of rows",count)
        for i in records:             #fetchall and fetchmany
            print(i[0],":",i[1])
        ans=input("Do you wish to delete record yes/no:")
        if ans.lower=='Yes'.lower():
            mycursor.execute("Delete from galaxies where Name='{0}'".format(no))
            print("Record Deleted")
            mycon.commit()
        else:
            print("No record deleted")

#displaying of records

def displaystars():
    mycursor.execute("select * from star")
    records=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("No records Found")
    else:
        print("no of rows",count)
        print('Name \t:Distance_from_Earth\t:Star_Type\t:Stage_of_life\t:Part_of_constellation')
        for i in records:
            print(i[0],":",i[1],":",i[2],":",i[3],":",i[4])

def displayastronaut():
    mycursor.execute("select * from astronauts")
    records=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("No records Found")
    else:
        print("no of rows",count)
        print('Name:Country:mission:age_during_accomplishment:Accomplishment')
        for i in records:
            print(i[0],":",i[1],":",i[2],":",i[3],":",i[4])

def displayplanets():
    mycursor.execute("select * from planets")
    records=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("No records Found")
    else:
        print("no of rows",count)
        print('Name:Distance_from_Earth:Number_of_moons:Length_of_Year_in_Earth_Days:No_of_Human_Spacecraft')
        for i in records:
            print(i[0],":",i[1],":",i[2],":",i[3],":",i[4])

def displayconstellations():
    mycursor.execute("select * from constellations")
    records=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("No records Found")
    else:
        print("no of rows",count)
        print('name:brightest_star:area_sq_degree')
        for i in records:
            print(i[0],":",i[1],":",i[2])

def displaygalaxies():
    mycursor.execute("select * from galaxies")
    records=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("No records Found")
    else:
        print("no of rows",count)
        print('name:diameter_in_light_year')
        for i in records:
            print(i[0],":",i[1])

def adminright():
    print("Welcome!")
    u=input("Enter username:")
    mycursor.execute("select * from admin where name='{0}'".format(u))
    records=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("Enter valid username:")
    else:
        p=input("Enter your password:")
        k=0
        while k!=3:
            print("""1.Add
2.Delete
3.Exit""")
            k=int(input("Enter choice:"))
            if k==1:
                print("""Add
                      1.Stars
                      2.Galaxy
                      3.Astronaut
                      4.Planet
                      5.Constellations""")
                a=int(input("Enter an option"))
                if a==1:
                    print("You have decided to add records in stars table")
                    addrecordsstars()
                    ch=input("Do you wish to see the updated table yes/no?")
                    if ch.lower()=="Yes".lower():
                        displaystars()
                    else:
                        print("You can refer to table in MySQL also to see the changes")
                elif a==2:
                    print("You have decided to add records in galaxies table")
                    addgalaxies()
                    ch=input("Do you wish to see the updated table yes/no?")
                    if ch.lower()=="Yes".lower():
                        displaygalaxies()
                    else:
                        print("You can refer to table in MySQL also to see the changes")
                elif a==3:
                    print("You have decided to add records in astronauts table")
                    addrecordsastronauts()
                    ch=input("Do you wish to see the updated table yes/no?")
                    if ch.lower()=="Yes".lower():
                        displayastronaut()
                    else:
                        print("You can refer to table in MySQL also to see the changes")
                elif a==4:
                    print("You have decided to add records in planets table")
                    addrecordsplanets()
                    ch=input("Do you wish to see the updated table yes/no?")
                    if ch.lower()=="Yes".lower():
                        displayplanets()
                    else:
                        print("You can refer to table in MySQL also to see the changes")
                elif a==5:
                    print("You have decided to add records in constellations table")
                    addconst()
                    ch=input("Do you wish to see the updated table yes/no?")
                    if ch.lower()=="Yes".lower():
                        displayconstellations()
                    else:
                        print("You can refer to table in MySQL also to see the changes")
                else:
                    print("Enter valid choice")
            elif k==2:
                print("""Delete
                      1.Stars
                      2.Galaxy
                      3.Astronaut
                      4.Planet
                      5.Constellations""")
                d=int(input("Enter an option"))
                if d==1:
                    print("You have decided to delete a record from table stars")
                    deletestar()
                    ch=input("Do you wish to see the updated table yes/no?")
                    if ch.lower()=="Yes".lower():
                        displaystars()
                    else:
                        print("You can refer to table in MySQL also to see the changes")
                elif d==2:
                    print("You have decided to delete a record from table galaxies")
                    deletegalaxy()
                    ch=input("Do you wish to see the updated table yes/no?")
                    if ch.lower()=="Yes".lower():
                        displaygalaxies()
                    else:
                        print("You can refer to table in MySQL also to see the changes")
                elif d==3:
                    print("You have decided to delete a record from table astronauts")
                    deleteastronaut()
                    ch=input("Do you wish to see the updated table yes/no?")
                    if ch.lower()=="Yes".lower():
                        displayastronaut()
                    else:
                        print("You can refer to table in MySQL also to see the changes")
                elif d==4:
                    print("You have decided to delete a record from table planets")
                    deleteplanet()
                    ch=input("Do you wish to see the updated table yes/no?")
                    if ch.lower()=="Yes".lower():
                        displayplanets()
                    else:
                        print("You can refer to table in MySQL also to see the changes")
                elif d==5:
                    print("You have decided to delete a record from table constellations")
                    deleteconstellation()
                    ch=input("Do you wish to see the updated table yes/no?")
                    if ch.lower()=="Yes".lower():
                        displayconstellations()
                    else:
                        print("You can refer to table in MySQL also to see the changes")
                else:
                    print("Enter Valid Choice")
            else:
                print("You have decided to exit the program")

def username():
    user=input("Enter your name")
    age=int(input("Enter your age"))
    qry="insert into users values(%s,%s)"
    userlist=[user,age]
    mycursor.execute(qry,userlist)
    mycon.commit()
    u=0
    while u!=4:
        print("""1.Search
2.Display
3.Graph
4.Exit""")
        u=int(input("Enter choice"))
        if u==1:
            print("""Search
                      1.Stars
                      2.Galaxy
                      3.Astronaut
                      4.Planet
                      5.Constellations""")
            ch=int(input("Enter your choice"))
            if ch==1:
                print("You are on the way to reach stars")
                searchnamestars()
            elif ch==2:
                print("You are on the way to reach galaxies")
                searchnamegalaxy()
            elif ch==3:
                print("You are on the path of Astronaut's Knowledge")
                searchnameastronauts()
            elif ch==4:
                print("You are on the way to jump over to planets")
                searchnameplanets()
            elif ch==5:
                print("You are on the way to play in the constellations")
                searchnameconstellations()
            else:
                print("Enter Valid choice")
        elif u==2:
            print("""Display
                      1.Stars
                      2.Galaxy
                      3.Astronaut
                      4.Planet
                      5.Constellations""")
            ch=int(input("Enter your choice"))
            if ch==1:
                print("You will soon get the data of stars")
                displaystars()
            elif ch==2:
                print("You will soon get the data of galaxies")
                displaygalaxies()
            elif ch==3:
                print("You will soon get the data of astronauts")
                displayastronaut()
            elif ch==4:
                print("You will soon get the data of planets")
                displayplanets()
            elif ch==5:
                print("You will soon get the data of constellations")
                displayconstellations()
            else:
                print("Enter Valid choice")
        elif u==3:
            print("""1.Stars
2.Planet
3.Constellations""")
            ch=int(input("Enter your choice"))
            if ch==1:
                print("You will soon get an analytical approach towards stars through a graph")
                graphstars()
            elif ch==2:
                print("You will soon get an analytical approach towards planets through a graph")
                graphplanets()
            elif ch==3:
                print("You will soon get an analytical approach towards constellations through a graph")
                graphcons()
            else:
                print("Enter Valid choice")
        else:
            print("You have successfully exited the program")

def mainfunction():
    ch=input("Are you an admin or a user?")
    if ch.lower()=='Admin'.lower():
        adminright()
    elif ch.lower()=='User'.lower():
        username()
    else:
        print("Invalid choice entered")

mainfunction()
            
