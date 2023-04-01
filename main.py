
def Option():
    '''Printing all the available options'''

    print("1.Add New Course\n ")
    print("2.Update Existing Course\n ")
    print("3.Delete a Course\n")
    print("4.Show ALl Courses\n")
    print("5.Individual Course display\n")
    print("6. Search Courses\n")
    print('7.Want to store in file?\n')
    print('8.Check Pre requisite \n')
    print("Do you Want to quit?  \n"
          "Press 10 to Exit !!!\n")

Courses={'PL':['Basic Programming','csc110','3','N/A'],'OOP2':['JAVA','csc125','3','csc110'],

         'DS':['Data Structure','csc216','3','csc110','csc125'],'Algo':['Algorithm','csc221','3','csc110','csc216'],'OS':['Operating System','csc551','3','csc125']}
print('Please Enter an Option :\n')
Option()



def add_new_course():
    '''Adding a new course method'''
    courseName = input('enter course name')
    infolist = []
    print('enter the information of the course')
    for i in range(1, 5):
        #if Courses[i][3] in Courses:
        x = input()
        infolist.append(x)
    Courses[courseName] = infolist

    print(f"course info of {courseName} is",infolist)

def Update_Course():
    '''Updating any course method'''

    #for i in Courses:
    up=input('Enter the course you want to change')

    newlist=[]
    if up in Courses.keys():
        for i in range(1,5):
            change = input('Enter the values')
            newlist.append(change)
        Courses[up]=newlist
        print(f"Updated Course {up} info are:\n", newlist)
    elif up not in Courses.keys():
        print("no Coursese found, Do you want to find agin to delete? \n Yes!! or NO!!?  ")
        ans=input()
        if ans=='yes':
            return Update_Course()
        elif ans=='no':
            exit()


def Dele_course():
    '''Deleting any course from the dictionary'''
    print('Enter the course you want to delete')
    delete=input()
    if delete in Courses:

        del Courses[delete]
        print("After deleting the courses are : \n",Courses)

    else:
        print("NO such Courses FOUND!!!")


    #return Courses
def All_Course_display():
    '''Displaying all the courses'''
    print(Courses)

def show_individual_Courses():
    '''Showing particular course method'''

    print('Which course information you want to see?\n')
    courseinput=input()
    for course in Courses:
        if course==courseinput:
            print('The course values are:',Courses[course])
            break
        else:
            print('No Courses found, Do you want to add the new Course or do you want to search again to see a course?')
            answer=input()
            if answer=='find':
                return show_individual_Courses()
            elif answer=='add':
                add_new_course()

    #print(stored)

def search_Course():
    '''searching for any course function'''
    search=input('which course do you want to search?  ')
    for course in Courses.keys():
        if course==search:
            print('Found!!!\n',Courses[course])
            #break
       #''' elif course!=search:
          #  print('Not Found. Do you want to search Again? ')
           # ans=input()
           # if ans=='yes':
              #  search_Course()
           # elif ans=='no':
           #     exit()

def store_in_file():

    '''storing the course information in a file '''
    file_path='D:\Fall 2022-2023 (9th Semester)\Python\MidProject.txt'

    with open(file_path,'w') as file_object:
        for course in Courses.keys():
            file=course +'\n'+ Courses[course][0]+'\n'+ Courses[course][1]+'\n'+Courses[course][2] +'\n'+Courses[course][3]+'\n'
            file_object.write(file)
    if file:
        print("file stored")
    else:
        print("file not stored")


def pre_requisite_check():

    print("which Course to add?  ")
    check=input()
    print('what is the new Pre requisite?')
    change=input()
    for course in Courses.keys():
        if change in Courses[course][3]:
            print('Pre requisite already exists ')
            break
        else:
            Courses[course][3]=change
    print(Courses[check])


x=int(input())

if x==1:
    add_new_course()
elif x==2:
    Update_Course()
elif x==3:
    Dele_course()
elif x==4:
    All_Course_display()
elif x==5:
    show_individual_Courses()
elif x==6:
    search_Course()
elif x==7:
    store_in_file()
elif x==8:
    pre_requisite_check()
elif x==10:
    exit()









