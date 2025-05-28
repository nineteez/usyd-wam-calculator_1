import functions
import time

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
            max_semester_1_mark = self.student.previous_wam
            max_semester_2_mark = (self.student.this_sem_wam + 100) / 2

        max_wam = (max_semester_1_mark + max_semester_2_mark) / 2
        self.max_wam = round(max_wam, 2)

        # Search streams to assign stream eligibilities
        for stream, data in STREAM_DATA.items():
            if self.max_wam >= data["required_wam"]:
                self.eligible_streams.append(stream)

    # New method: Calculate required average to reach stream
    def get_required_avg_for_stream(self):
        target_wam = STREAM_DATA[self.student.stream]["required_wam"]

        if self.student.semester == 1:
            p = self.student.this_sem_wam
            required_avg = (12 * target_wam - 2 * p) / 10

        elif self.student.semester == 2:
            w1 = self.student.previous_wam
            p = self.student.this_sem_wam
            required_avg = 2 * (2 * target_wam - w1) - p

        required_avg = round(required_avg, 2)

        if required_avg > 100:
            eligibility = False
        elif required_avg < 0:
            eligibility = True
            required_avg = 0
        else:
            eligibility = True

        return required_avg, eligibility

    #Write improvement suggestions to a file
    def write_improvement_suggestions(self):
        file_name = f"{self.student.name} - Improvement Suggestions.txt"
        improvement_suggestions = open(file_name, "w")

        # Write a Customer HEader
        header = f'''Study plan for second year {self.student.stream} 
Student: {self.student.name}
Semester: {self.student.semester}
Specialisation: {self.student.specialisation}
        '''
        improvement_suggestions.write(header + "\n\n")


        total_units = list(functions.unit_to_topic.keys())
        
        # Create list of exams for current semester
        remaining_exams = list(self.student.current_units)

        # Create list of remaining units for semester 2 (if semester 1 student)
        if self.student.semester == 1:
            remaining_units = []
            for unit in total_units:
                if unit not in self.student.current_units:
                    remaining_units.append(unit)

        # Create write functions

        # Current semester exam study recommendations
        def write_exam_topics():
            improvement_suggestions.write("\nThis semester Exam Focus:\n")

            for unit in remaining_exams:
                if unit in functions.unit_to_topic:
                    improvement_suggestions.write(f"\nUnit: {unit}\n")
                    topics = functions.unit_to_topic[unit]
        
                    for topic in topics:
                        improvement_suggestions.write(f"  Topic: {topic}\n")
                        for outcome in functions.learning_outcomes.get(topic, []):
                            improvement_suggestions.write(f"    • {outcome}\n")


        # Next semester study recommendations
        def next_semester_study_plan():
            improvement_suggestions.write("\nNext Semester Focus:\n")

            for unit in remaining_units:
                if unit in functions.unit_to_topic:
                    improvement_suggestions.write(f"\nUnit: {unit}\n")
                    topics = functions.unit_to_topic[unit]

                    for topic in topics:
                        improvement_suggestions.write(f"  Topic: {topic}\n")
                        for outcome in functions.learning_outcomes.get(topic, []):
                            improvement_suggestions.write(f"    • {outcome}\n")                    



        # Write study suggestions
        if self.student.semester == 1:
            # Write Sem1 
            write_exam_topics()

            # Write Sem2 
            next_semester_study_plan()
        
        elif self.student.semester == 2:

            #Write Sem2 
            write_exam_topics()


        improvement_suggestions.close()
        print(f'View your study plan in the attached file: {file_name}')
        time.sleep(1)
        print(f'Good Luck! {self.student.name}!')

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
            self.this_sem_wam = round(this_sem_wam, 2)
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

            self.previous_wam = previous_wam
            self.this_sem_wam = this_sem_wam
            self.wam = round((previous_wam + this_sem_wam) / 2, 2)

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
