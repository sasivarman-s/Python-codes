
def cse():
    print("\n===== CSE TIME TABLE =====")
    print("Monday    : Chemistry | English | Physics | Logical Mathematics")
    print("Tuesday   : DSA | AI Modelling | BEEE | Python")
    print("Wednesday : CSL Lab | Python Lab | Chemistry | BEEE")
    print("Thursday  : Chemistry Lab | Physics Lab | Sports | English")
    print("Friday    : Database | Chemistry | BEEE | Computation Mathematics")

def ece():
    print("\n===== ECE TIME TABLE =====")
    print("Monday    : Chemistry | English | Physics | Mathematics")
    print("Tuesday   : EPL | Mathematics | BEEE | Solid Mechanics")
    print("Wednesday : CSL Lab | Circuits Lab | Chemistry | BEEE")
    print("Thursday  : Chemistry Lab | Physics Lab | Sports | English")
    print("Friday    : Physics | Chemistry | BEEE | Mathematics")

def eee():
    print("\n===== EEE TIME TABLE =====")
    print("Monday    : Chemistry | Physics | Junction Lab | Mathematics")
    print("Tuesday   : EPL | Calculus | BEEE | Solid Mechanics")
    print("Wednesday : CSL Lab | Electronics Lab | Chemistry | BEEE")
    print("Thursday  : Chemistry Lab | Physics Lab | Sports | Electrical Logics")
    print("Friday    : Physics | Chemistry | BEEE | Analog Mathematics")

def mech():
    print("\n===== MECH TIME TABLE =====")
    print("Monday    : Chemistry | English | Physics | Mathematics")
    print("Tuesday   : Thermodynamics | Mathematics | BEEE | Solid Mechanics")
    print("Wednesday : CSL Lab | Mechanical Lab | Chemistry | BEEE")
    print("Thursday  : Chemistry Lab | Physics Lab | Sports | English")
    print("Friday    : Physics | Chemistry | BEEE | Mathematics")

def civil():
    print("\n===== CIVIL TIME TABLE =====")
    print("Monday    : Chemistry | English | Physics | Mathematics")
    print("Tuesday   : Structural Analysis | Mathematics | BEEE | Solid Mechanics")
    print("Wednesday : CSL Lab | Civil Lab | Chemistry | BEEE")
    print("Thursday  : Chemistry Lab | Physics Lab | Sports | English")
    print("Friday    : Physics | Chemistry | BEEE | Mathematics")



CSE_B = ["sasivarman","sasi","sv","SV","mithun","shahjan","pranav",
         "nithin","nishant","yuva pk","sree kumar","pradeep",
         "prasanna","alam","sarvesh","udhaya","sywas",
         "irfan","yuvan","muthu","udhayanidhi","satheesh","oviyan","yuvaraj","omair khan"]

name = input("Enter your Name: ").strip()

if name.lower() in [x.lower() for x in CSE_B]:

    print("\nDATA SAVED IN DIGI-LOGBOOK!", name, "is present today")
    print("Welcome To Class", name,"!")

    while True:
        print("\nDo any others?:")
        print("choose an option:")
        print("1. Exit")
        print("2. Check Rank")
        print("3. Check Time Table")

        do = input("Enter your choice: ").strip().lower()

        if do in ["1", "exit"]:
            print("Exited successfully!..")
            break

        elif do in ["2", "check rank"]:
            try:
                attendance = float(input("Enter Attendance %: "))
                study_hours = float(input("Enter Study Hours/day: "))
                internal_marks = float(input("Enter Internal Marks: "))

                score = (attendance * 0.3) + (study_hours * 10) + (internal_marks * 0.5)

                if attendance >= 75 and internal_marks >= 40 and study_hours >= 2:
                    result = "PASS"
                else:
                    result = "FAIL"

                print("Score:", round(score, 2))
                print("Result:", result)

            except:
                print("Invalid input! Please enter numbers only.")

        elif do in ["3", "check time table"]:
            dept = input("Enter your department (CSE/ECE/EEE/MECH/CIVIL): ").strip().lower()

            if dept == "cse":
                cse()
            elif dept == "ece":
                ece()
            elif dept == "eee":
                eee()
            elif dept == "mech":
                mech()
            elif dept == "civil":
                civil()
            else:
                print("Invalid department!")

        else:
            print("Invalid option! Try again.")

    print("\ncall- 044 250 250")
    print("SV PRIVATE Ltd")

else:
    print("Wrong Entry!")
    print("Enter last 3 digits of roll number: ")

    try:
        n2 = int(input())

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
            print("Invalid number")

    except:
        print("Invalid input! Enter numbers only.")