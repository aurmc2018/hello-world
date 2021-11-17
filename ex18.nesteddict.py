#print("Test Visualizer")
coures = {}
courses = {
    "civil": "B.E. Civil Engineering",
    "mech": "B.E. Mechanical Engineering",
    "subject_codes": {
        "811": "Maths",
        "822": "Physics",
        "833": "Chemistry",
    },
}

for i in courses:
    print(i)
    if (i != "subject_codes"):
        print(courses)
    else:
        subj_length = len(courses["subject_codes"])
        j = 0
        for j in courses[i]:
            print(courses[i][j])

