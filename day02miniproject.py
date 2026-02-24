def calculate_fee(course, marks):
    course = course.strip().lower()

    if course == "ai":
        fee = 50000
    elif course == "web":
        fee = 40000
    elif course == "data science":
        fee = 30000
    else:
        return None   # Important: return immediately if invalid course

    # Apply discount
    if marks > 90:
        print("Congratulations! You get a Rs:5000 discount on fee")
        fee -= 5000
    elif marks > 80:
        print("Congratulations! You get a Rs:3000 discount on fee")
        fee -= 3000

    return fee


def main():
    print("Welcome to the fee calculator")
    course = input("Enter the course name: ")

    try:
        marks = int(input("Enter the marks: "))
        if marks < 0 or marks > 100:
            print("Invalid marks. Please enter marks between 0 and 100.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer for marks.")
        return

    fee = calculate_fee(course, marks)

    if fee is None:
        print("Invalid course name. Please enter a valid course name.")
    else:
        print("The fee for", course, "is Rs:", fee)


main()