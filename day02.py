# 24th feb 2026
# if/ else / elif
    # making or choosing conditions based on the logical flow of the program
# exception handling try
    # error handling in program makes code to run in a proper way after handeling the error


# ZeroDivisionError
# try:
#     num=int(input("Enter a number: "))
#     result1 = 10/num
#     print("Result: ",result1)
# except ZeroDivisionError:
#     print("You cannot divide by zero")
# finally:
#     print("Program ended successfully")
    
#ValueError
# try:
#     num=int(input("Enter a number: "))
#     print("Result: ",result1)
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# finally:
#     print("Program ended successfully")


# printing even and odd numbers
# def check_even_odd(num):
#     try:
#         if num%2==0:
#             print("Even number")
#         else:
#             print("Odd number")
#     except Exception as e:
#         print("An error occurred:", e)
# def main():
#     num=int(input("Enter a number: "))
#     check_even_odd(num)
# if __name__=="__main__":
#     main()

# find maximum of two numbers
# def find_maximum(num1, num2):
#     try:
#         if num1>num2:
#             print(num1,"is maximum")
#         else:
#             print(num2,"is maximum")
#     except Exception as e:
#         print("An error occurred:", e)
# def main():
#     num1=int(input("Enter first number: "))
#     num2=int(input("Enter second number: "))
#     find_maximum(num1, num2)
# if __name__=="__main__":
#     main()

# if elif else
def grade_check(marks):
    try:
        if marks<0 or marks>100:
            print("Invalid marks. Please enter marks between 0 and 100.")
        if marks>=90:
            print("Grade 0")
        elif marks>=80:
            print("Grade A+")
        elif marks>=70:
            print("Grade A")
        elif marks>=60:
            print("Grade B")
        elif marks>=50:
            print("Grade C")
        else:
            print("Grade F")
    except Exception as e:
        print("An error occurred:", e)
def main():
    marks=int(input("Enter your marks: "))
    grade_check(marks)
if __name__=="__main__":
    main()
