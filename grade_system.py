def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "E"


def main():
    print("===== Student Grade System =====")

    try:
        # Get marks from the user
        marks = float(input("Enter student marks (0-100): "))

        # Validate marks
        if marks < 0 or marks > 100:
            print("Error: Marks must be between 0 and 100.")
            return

        # Calculate grade
        grade = calculate_grade(marks)

        # Display result
        print(f"Marks : {marks}")
        print(f"Grade : {grade}")

    except ValueError:
        print("Error: Please enter a valid number.")

    except Exception as e:
        print(f"Unexpected error: {e}")


# Start the program
main()