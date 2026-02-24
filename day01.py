# 23rd feb 2026
# Intro to DSA
# I/O operations
# loops 

# Print numbers from 1 to n
def print_numbers_sum(n):
    for i in range(1,n+1):
        print(i)
def main():
    n = int(input("Enter the value of n: "))
    print_numbers_sum(n)
if __name__ == "__main__":
    main()

# Sum of First n natural numbers
def calculate_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
def main():
    n = int(input("Enter the value of n: "))
    print("Sum of first",n,"natural numbers is:",calculate_sum(n))
if __name__ == "__main__":
    main()
