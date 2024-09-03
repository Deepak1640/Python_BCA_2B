Attendance=float(input("Enter The Students Attendance: "))
if Attendance > 90:
    print("No fine")
elif Attendance > 85 and Attendance <= 90:
    print("Fine 500")
elif Attendance > 80 and Attendance <= 85:
    print("Fine 1000")
else:
    print("Attendance is below 80 contact to HOD")
