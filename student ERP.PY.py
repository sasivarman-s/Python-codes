# checks whether the student is present or not and further checks which class is he/she
# CSE_B is a class, checks like digital attendance

CSE_B = ["sasivarman","sasi","sv","SV","mithun","shahjan","pranav",
         "nithin","nishant","yuva pk","sree kumar","pradeep",
         "prasanna","alam","sarvesh","udhaya","sywas",
         "irfan","yuvan","muthu","udhayanidhi","satheesh","oviyan","yuvaraj","omair khan"]

name = input("Enter your Name: ")

# Fix: case-insensitive check
if name.lower() in [x.lower() for x in CSE_B]:

    print("    DATA SAVED IN DIGI-LOGBOOK!", name, "is present today")
    print("Welcome To Class", name, "!")
    print("Enjoy your day!")
    print("do any others?")
    print("1.Exit \n2.check rank")

    do = input("Any other to do?: ")

    # Fix: correct condition checking
    if do.lower() == "exit":
        print("Exited successfully!..")

    elif do.lower() == "check rank":

        attendance = float(input("Enter Attendance Percentage: "))
        study_hours = float(input("Enter Study Hours per Day: "))
        internal_marks = float(input("Enter Internal Marks: "))

        student_data = (attendance, study_hours, internal_marks)

        score = (attendance * 0.3) + (study_hours * 10) + (internal_marks * 0.5)

        if attendance >= 75 and internal_marks >= 40 and study_hours >= 2:
            result = "PASS"
        else:
            result = "FAIL"

        print("Student Data:", student_data)
        print("Calculated Performance Score:", score)
        print("Predicted Result:", result)

    print("call- 044 250 250")
    print("SV PRIVATE Ltd")

else:
    print("Wrong Entry!, You might Entered Another Class?")
    print("Enter the roll number to search which class you might be?")

    n2 = int(input("Last 3 Digits of Your Roll Number: "))

    # Fix: proper range logic
    if n2 <= 100:
        print("CSE")
    elif n2 <= 200:
        print("ECE")
    elif n2 <= 300:
        print("EEE")
    elif n2 <= 400:
        print("MECH")
    elif n2 <= 500:
        print("CIVIL")
    else:
        print("Invalid format/number, you should contact office room")
        print("call- 044 250 250")
        print("SV PRIVATE Ltd")
