import functions

# refer to in classes below
STREAM_DATA = {
    "Capstone": {"required_wam": 50},
    "Work Integrated": {"required_wam": 75},
    "Research": {"required_wam": 75}
}

# create object of student's possible streams and required marks
class Possible_streams:
    def __init__(self, student: object):
        self.student = student
        self.max_wam = None
        self.eligible_streams = []

    # Calculate stream eligibilties and store as attribute
    def get_eligible_streams(self):
        self.eligible_streams = []  # clear any previous values
        
        if self.student.semester == 1:
            max_semester_1_mark =  (self.student.wam + 100) / 2
            max_semester_2_mark = 100

        else:
            max_semester_1_mark = self.student.wam - self.student.this_sem_wam
            max_semester_2_mark = (self.student.this_sem_wam + 100) / 2

        max_wam = (max_semester_1_mark + max_semester_2_mark) / 2
        self.max_wam = round(max_wam, 2)

        #search streams to assign stream eligibilities
        for stream, data in STREAM_DATA.items():
            if self.max_wam >= data["required_wam"]:
                self.eligible_streams.append(stream)


class Student:
    specialisation_options = [
        "Algorithms And Theory",
        "Cybersecurity",
        "Data Science And Ai",
        "Digital Media",
        "Human Computer Interaction",
        "Networks And Distributed Systems",
        "Software Engineering"
    ]

    def __init__(self):
        self.name = None
        self.semester = None
        self.specialisation = None
        self.stream = None
        self.current_units = []
        self.wam = None
        self.this_sem_wam = None

    def set_name(self):
        prompt = "What's your name? Do you study the Master of \nComputer Science at USyd? (Format: <first_name> <yes/no>): "

        while True:
            response = input(prompt).strip()
            parts = response.split()

            if len(parts) != 2:
                prompt = "⚠️ Please enter exactly two words: <first_name> <yes/no>: "
                print('')
                continue

            first_name, answer = parts[0], parts[1].lower()

            if answer not in ("yes", "no"):
                print("⚠️ Second word must be 'yes' or 'no'. Try again.")
                prompt = "Please enter your name and 'yes' or 'no': "
                print('')
                continue

            if answer == 'no':
                print('')
                print(f"Sorry {first_name}! This is only available to USyd students.")
                return 'exit'

            self.name = first_name.capitalize()
            self.is_usyd_cs_masters = True
            print('')
            break

    def set_semester(self):
        convert = {'one': 1, 'two': 2}
        prompt = f"Hi {self.name}! What semester are you in? (1 or 2, or 'one'/'two', or 'exit'): "
        while True:
            semester = input(prompt).lower()

            if semester in ('1', '2'):
                int_semester = int(semester)
                self.semester = int_semester
                print('')
                break
            elif semester.lower() in convert:
                self.semester = convert[semester.lower()]
                print('')
                break
            elif semester.lower() == 'exit':
                print('')
                return 'exit'
            else:
                prompt = ("⚠️Answer must be (1 or 2, or 'one''two') or 'Exit': ")
                print('')

    def set_specialisation(self):
        prompt = f"Enter your specialisation:\n-{'\n-'.join(self.specialisation_options)}: "
        while True:
            specialisation = input(prompt).title()

            if specialisation in self.specialisation_options:
                self.specialisation = specialisation
                print('')
                break
            elif specialisation.lower() == 'exit':
                return 'exit'
            else:
                prompt = f"⚠️Answer must be in:\n-{'\n-'.join(self.specialisation_options)} or Exit: "
                print('')

        self.specialisation = specialisation

    def set_stream(self):
        possible_streams = ('Capstone', 'Work Integrated', 'Research')
        prompt = 'Enter your desired stream (Capstone, Work Integrated, Research): '.capitalize()
        while True:
            stream = input(prompt).title()

            if stream in possible_streams:
                self.stream = stream
                print('')
                break
            elif stream.lower() == 'exit':
                return 'exit'
            else:
                prompt = (f"⚠️Answer must be {', '.join(possible_streams)} or 'Exit': ")
                print('')

    def set_current_units(self):
        prompt = 'Which units are you taking by code? (space-separated, e.g., COMP9601 COMP9120 COMP9001 INFO5990): '

        while True:
            uos_code_list = input(prompt).upper().split()

            if len(uos_code_list) != 4:
                print("❌ You must enter exactly 4 space-separated UOS codes.")
                prompt = "Enter current units (4 codes, e.g., COMP9601 COMP9120 COMP9001 INFO5990): "
                continue

            invalid_codes = [code for code in uos_code_list if code not in functions.unit_to_topic]

            if invalid_codes:
                valid_codes = ', '.join(functions.unit_to_topic.keys())
                print(f"❌ Invalid code(s): {', '.join(invalid_codes)}")
                print(f"✅ Valid UOS codes are: {valid_codes}")
                prompt = "Enter current units (4 codes, e.g., COMP9601 COMP9120 COMP9001 INFO5990): "
                continue

            self.current_units = uos_code_list
            break

    # Calculate current WAM
    def set_current_wam(self):
        total = 0
        count = 0

        print("\nEnter your pre-exam grades for the following units:")

        for uos in self.current_units:
            while True:
                grade_input = input(f'{uos}: ')
                try:
                    grade = float(grade_input)
                    if 0 <= grade <= 100:
                        total += grade
                        count += 1
                        break
                    else:
                        print("⚠️ Grade must be between 0 and 100.")
                except ValueError:
                    print("❌ Please enter a valid number.")

        this_sem_wam = total / count

        if self.semester == 1:
            self.wam = round(this_sem_wam, 2)

        elif self.semester == 2:
            while True:
                try:
                    previous_wam = float(input("\nWhat is your WAM from last semester? (50–100): "))
                    if 50 <= previous_wam <= 100:
                        break
                    else:
                        print("⚠️ WAM must be between 50 and 100 to progress to this semester.")
                except ValueError:
                    print("❌ Please enter a valid number.")

            self.wam = round((previous_wam + this_sem_wam) / 2, 2)
            self.this_sem_wam = this_sem_wam

    @classmethod
    def build_student_object(cls):
        student = cls()
        for step in (
                student.set_name,
                student.set_semester,
                student.set_specialisation,
                student.set_stream,
                student.set_current_units,
                student.set_current_wam
        ):
            if step() == 'exit':
                return None
        return student

    # def set_grade(self):
    #     if self.semester = 1:
    #         raw_grades = input('For each unit, enter name and total grade (pre exam) (e.g., COMP5045:78,COMP5310:74)')
    #     else:
    #         raw_grades = input('Enter completed subjects and grades so (e.g., COMP5045:78,COMP5310:74): ')
