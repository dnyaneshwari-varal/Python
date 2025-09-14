class Faculty:
    id_counter = 1  # auto increment

    def __init__(self, faculty_name):
        self.faculty_id = Faculty.id_counter
        Faculty.id_counter += 1
        self.faculty_name = faculty_name

    def calculatePayment(self):
        return 0

    def printDetails(self):
        print(f"Faculty ID: {self.faculty_id}")
        print(f"Faculty Name: {self.faculty_name}")



class VisitingFaculty(Faculty):
    def __init__(self, name, hours, rate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate
        self.total_payment = 0
        self.tds = 0

    def calculatePayment(self):
        gross = self.hours * self.rate
        self.tds = gross * 0.10
        self.total_payment = gross - self.tds
        return self.total_payment

    def printDetails(self):
        super().printDetails()
        print(f"Hours Worked: {self.hours}")
        print(f"Rate per Hour: {self.rate}")
        print(f"TDS Deducted: {self.tds}")
        print(f"Total Payment: {self.total_payment}")

class OnRollFaculty(Faculty):
    def __init__(self, name, basicSalary, totalLeaves):
        super().__init__(name)
        self.basicSalary = basicSalary
        self.totalLeaves = totalLeaves
        self.grossSalary = 0
        self.netSalary = 0

    def calculatePayment(self, leavesTaken=0, gratuity=0):
        pf = 0.10 * self.basicSalary
        deduction = 0
        if leavesTaken > self.totalLeaves:
            deduction = (leavesTaken - self.totalLeaves) * (self.basicSalary / 30)

        self.grossSalary = self.basicSalary + gratuity
        self.netSalary = self.grossSalary - pf - deduction
        return self.netSalary

    def printDetails(self):
        super().printDetails()
        print(f"Basic Salary: {self.basicSalary}")
        print(f"Gross Salary: {self.grossSalary}")
        print(f"Net Salary: {self.netSalary}")
        print(f"Total Leaves Allowed: {self.totalLeaves}")

class TestMain:
    @staticmethod
    def getFacultyDetails():
        print("\nChoose Faculty Type:")
        print("1. Visiting Faculty")
        print("2. On-Roll Faculty")
        choice = int(input("Enter choice: "))

        name = input("Enter Faculty Name: ")

        if choice == 1:
            hours = float(input("Enter working hours: "))
            rate = float(input("Enter rate per hour: "))
            return VisitingFaculty(name, hours, rate)

        elif choice == 2:
            basic = float(input("Enter Basic Salary: "))
            leaves = int(input("Enter Total Leaves: "))
            return OnRollFaculty(name, basic, leaves)

        else:
            print("Invalid choice")
            return None

    @staticmethod
    def show(faculty):
        if isinstance(faculty, VisitingFaculty):
            faculty.calculatePayment()
        elif isinstance(faculty, OnRollFaculty):
            leavesTaken = int(input("Enter Leaves Taken: "))
            gratuity = float(input("Enter Gratuity Amount: "))
            faculty.calculatePayment(leavesTaken, gratuity)

        print("\n--- Faculty Details ---")
        faculty.printDetails()



if __name__ == "__main__":
    faculties = []

    # 1 Visiting + 3 OnRoll
    for i in range(4):
        f = TestMain.getFacultyDetails()
        faculties.append(f)

    for f in faculties:
        TestMain.show(f)
