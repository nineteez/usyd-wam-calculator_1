import functions

#refer to in classes below
STREAM_DATA = {
    "Capstone": {"required_wam": 50},
    "Work Integrated": {"required_wam": 75},
    "Research": {"required_wam": 75}
}

class Stream:
    def __init__(self, name):
        self.name = name
        self.required_wam = STREAM_DATA[name]["required_wam"]

class Unit:
    def __init__(self, unit_code, unit_competencies, final_exam_percentage):
        self.unit_code = unit_code
        self.unit_competencies = unit_competencies
        self.final_exam_percentage = final_exam_percentage

class Student:

    specialisation_options = [
        "Algorithms And Theory",
        "Cybersecurity",
        "Data Science And AI",
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
        self.grades = None

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
                print("Sorry! This is only available to USyd students.")
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
            

    @classmethod
    def build_student_object(cls):
        student = cls()
        for step in (
            student.set_name,
            student.set_semester,
            student.set_specialisation,
            student.set_stream
        ):
            if step() == 'exit':
                return None
        return student
    # def set_grade(self):
    #     if self.semester = 1:
    #         raw_grades = input('For each unit, enter name and total grade (pre exam) (e.g., COMP5045:78,COMP5310:74)')
    #     else:
    #         raw_grades = input('Enter completed subjects and grades so (e.g., COMP5045:78,COMP5310:74): ')

  
   
