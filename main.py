import models
import functions
import time

def main():
    # Build student object
    student = models.Student.build_student_object()
    if student is None:
        functions.handle_exit()

    print(f"Sounds great!\n")
    time.sleep(2)
    print("Let's see what marks you need to get into your desired stream!")
    time.sleep(2)

    # Create Possible_streams object and calculate max WAM
    possible_streams = models.Possible_streams(student)
    possible_streams.get_eligible_streams()
    print(f"\n📊 Estimated Max WAM (if you score 100s in remaining units): {possible_streams.max_wam}")

    # Show required average for stream eligibility
    required_avg, is_possible = possible_streams.get_required_avg_for_stream()
    target_wam = models.STREAM_DATA[student.stream]["required_wam"]

    print(f"\n📘 To qualify for the {student.stream} stream (requires {target_wam} WAM):")
    if student.semester == 1:
        print(f"🎯 You must average {required_avg}% in your final exams this semester "
          f"and across all 4 units next semester to qualify.")
    elif student.semester == 2:
        print(f"🎯 You must average {required_avg}% in your upcoming final exams this semester to qualify.")

    else:
        print(f"❌ You would need {required_avg}%, which is not realistically achievable.")

    # Immediate eligibility check
    if student.stream in possible_streams.eligible_streams:
        print(f"🎉 You are eligible for your desired stream: {student.stream}")
        possible_streams.write_improvement_suggestions()
    elif possible_streams.eligible_streams:
        print(f'''⚠️ You are not yet eligible for {student.stream}, 
but you are eligible for: {', '.join(possible_streams.eligible_streams)}.
Run the program again to generate a study plan for this!''')
    else:
        print("❌ You are not currently eligible for any stream based on your projected max WAM.")


if __name__ == "__main__":
    main()
