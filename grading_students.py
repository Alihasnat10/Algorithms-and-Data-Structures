def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] < 38:
            continue
        elif grades[i] >= 38 and ((grades[i]+1)%5==0 or (grades[i]+2)%5==0):
            if (grades[i]+1)%5==0:
                grades[i] += 1
            elif (grades[i]+2)%5==0:
                grades[i] += 2
    return grades
grades = [73,67,38,33]
print(gradingStudents(grades))
