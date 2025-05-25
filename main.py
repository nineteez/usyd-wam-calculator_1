import models
import functions
import time

def main():
    # Build student class
    student = models.Student.build_student_object()
    if student is None:
        functions.handle_exit()
    print(f'Sounds great!\n')
    time.sleep(2)
    print('Lets see what marks you need to get into your desired stream!') 
    functions.calculate_required_wam(student)
    


if __name__ == "__main__":
    main()
