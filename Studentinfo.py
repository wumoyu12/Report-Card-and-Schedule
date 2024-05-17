'''
Names: Moyu Wu, Jovanna
Start: May 2, 2024
End:
Description: We will display the student report card and schedule 
''' 
import os.path
from os import path

def Menu():
    global option
    option = str(input("1.Add New Student\n2.Check Information\n3.Modify/Delete Information"))
    CheckOption()
    AskID()

    match option:
        case option if int(option) == 1:
            Add()
        case option if int(option) == 2:
            CheckInfo()
        case option if int(option) == 3:
            Change()

def CheckOption():
    optionlen = len(option)
    if optionlen != 1:
        print("Invalid")
        Menu()
    else:
        ordoption = ord(option)
        optionlist = list(option)
        for i in range(0,len(option)):
            newnum = ord(optionlist[i])
            if (newnum < 49 or newnum > 51):
                print("Invalid")
                Menu()

def AskID():
    global ID, filename
    ID = str(input("Please enter student ID:"))
    CheckID()
    filename = ID + ".txt"
    Checkfile()

def CheckID():
    IDlen = len(ID)
    if IDlen != 9:
        print("Invalid")
        AskID()
    else:
        for i in range(0,len(ID)):
            newnum = ord(ID[i])
            if (newnum < 48 or newnum > 57):
                print("Invalid")
                AskID()

def Checkfile():
    global ifexists
    ifexists = bool(path.exists(filename))

def Add():
    if (ifexists == False):
        print("Created successfully, please enter the student information.")
        AskInfo()
    else:
        print("This student has already been added.")
        print("The following is the student's information:")
        pythfile = open(filename, "r")
        print(pythfile.read())
        pythfile.close()

def AskInfo():
    AskName()
    AskGradelevel()
    AskCourse()

def AskName():
    global fullname
    AskFName()
    AskLName()

    fullname = lname + " " + fname

def AskFName():
    global fname
    fname = str(input("Enter the student's first name."))
    fname = fname.upper()
    Checkfname()
    fname = fname.capitalize()

def AskLName():
    global lname
    lname = str(input("Enter the student's last name."))
    lname = lname.upper()
    Checklname()
    lname = lname.capitalize()


def Checkfname():
    namelen = len(fname)
    if namelen == 0:
        print("Invalid")
        AskFName()
    else:
        namelist = list(fname)
        for i in range (0, namelen):
            newname = ord(namelist[i])
            if newname < 65 or newname > 90:
                print("Invalid")
                AskFName()

def Checklname():
    namelen = len(lname)
    if namelen == 0:
        print("Invalid")
        AskLName()
    else:
        namelist = list(lname)
        for i in range (0, namelen):
            newname = ord(namelist[i])
            if newname < 65 or newname > 90:
                print("Invalid")
                AskLName()
                
def AskGradelevel():
    global askgrade 
    askgrade = str(input("What grade are you in?"))
    Checkgrades()

def Checkgrades():
    global askgrade
    match askgrade:
        case askgrade if int(askgrade) == 9:
            print("I am in ninth grade")
        case askgrade if int(askgrade) == 10:
            print("I am in tenth grade")
        case askgrade if int(askgrade) == 11:
            print("I am in  eleventh grade")
        case askgrade if int(askgrade) == 12:
            print("I am in twelfth grade")
        case askgrade == "":
            print("Invaild")
            AskGradelevel()
            

def AskCourse():
    global howmany, days, Days
    howmany = str(input("How many days a week do students have classes?"))
    Checkhowmany()
    Askdays()

def Askdays():
    global days
    count = int(howmany)
    while count == 0:
        days = str(input("On what days of the week do student have classes(Please enter one at time)?\n1-Mon 2-Tues 3-Wed 4-Thur 5-Fri 6-Sat 7-Sun"))
        Checkdays()
        count = count - 1

        match days:
            case days if int(days) == 1:
                MonCourse()
            case days if int(days) == 2:
                TuesCourse()
            case days if int(days) == 3:
                WedCourse()
            case days if int(days) == 4:
                ThurCourse()
            case days if int(days) == 5:
                FriCourse()
            case days if int(days) == 6:
                SatCourse()
            case days if int(days) == 7:
                SunCourse()

def Checkhowmany():
    numlen = len(howmany)
    if numlen != 1:
        print("Enter a valid number!")
        AskCourse()
    else:
        numlist = list(howmany)
        for i in range(0,len(numlist)):
            newnum = ord(numlist[i])
            if (newnum < 49 or newnum > 55):
                print("Invalid(only numbers 1-7)")
                AskCourse()

def MonCourse():

    print("Mon")

def TuesCourse():

    print("Tues")

def WedCourse():

    print("Wed")

def ThurCourse():

    print("Thur")

def FriCourse():

    print("Fri")

def SatCourse():

    print("Sat")

def SunCourse():
    print("Sun")

def Checkdays():
    dayslen = len(days)
    if dayslen != 1:
        print("Enter a valid number!")
        AskCourse()
    else:
        dayslist = list(days)
    for i in range(0,len(dayslist)):
            newdays = ord(dayslist[i])
            if (newdays < 49 or newdays > 55):
                print("Invalid(only numbers 1-7)")
                AskCourse()



def CheckInfo():
    if (ifexists == True):
        print("The following is the student's information:")
        pythfile = open(filename, "r")
        print(pythfile.read())
        pythfile.close()
    else:
        print("")



def Change():
    if (ifexists == True):
        print("The following is the student's information:")
        pythfile = open(filename, "r")
        print(pythfile.read())
        pythfile.close()
    else:
        print("Would you like to remove the information: ")
        print("")
        pythfile, "r+"
        pythfile.truncate();

def main():
    Menu()

if __name__ == "__main__":
    main()
