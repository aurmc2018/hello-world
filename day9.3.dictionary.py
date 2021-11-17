course = { "800":"B.E. Civil Engineering",
           "civil":
               {
                "811":"Mathematics",
                "812": "Physics",
                "813": "Chemistry",
           },
}


subject ={
    "course_name":
        "B.E.Civil",{
                "1":{"8C1":"Engineering English",
                     "812":"Engineering Physics",
                     "813":"Engineering Chemistry",
                     "814":"Engineering Drawing",
                     },
                "2":{"821":"Engineering Civil Maths 2"}
        }
       "B.E.Mechanical",{
                "1":{"911":"Engineering English",
                     "912":"Engineering Physics",
                     "913":"Engineering Chemistry",
                     "914":"Engineering Drawing"
                     },
                "2":{"921":"ENgineering  Maths 2",},
        }
}


course_teachers = []
course_students = []

course_semester = []
course_subjects = {}

no_more_sem_flag = False
no_more_sub_flag = False

sem = ""
subj_ctr = ""

def add_subjects():
    subj_code =""
    sub = ""
    while not no_more_sub_flag:
        subj_code = input(" Enter subject code, No. eg 112,  0 to quit")
        if subj_code == "0":
            break
        sub = input(" Enter subject name eg. Mathematics I")
        course_subjects[subj_code] = sub
    print(course_subjects)

def add_semester():
    sem_count = 0
    sem_count = int(input("enter how many semesters eg.3| 4| 8"))
    print(sem_count)
    for i in range(1, sem_count+1):
        course_semester.append(i)
    print(course_semester)


#add_semester()
#add_subjects()
print(course)
print(subject["B.E.Civil"])






