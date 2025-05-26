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
    time.sleep(2)

    # Create instance of Possible_streams for student and call it
    possible_streams = models.Possible_streams(student)
    possible_streams.get_eligible_streams()
    print(f"\n📊 Estimated Max WAM: {possible_streams.max_wam}")

    if student.stream in possible_streams.eligible_streams:
        print(f"🎉 You are eligible for your desired stream: {student.stream}")
    elif possible_streams.eligible_streams:
        required_wam = models.STREAM_DATA[student.stream]["required_wam"]
        print(f'''⚠️ You are not eligible for {student.stream} as it requires {required_wam}WAM.
        but you are eligible for: {', '.join(possible_streams.eligible_streams)}''')
    else:
        print("❌ You are not currently eligible for any stream based on your projected max WAM.")
    

if __name__ == "__main__":
    main()
