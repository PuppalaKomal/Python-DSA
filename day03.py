# 25-02-2026
# Counting Problem 
#     it is totally based on how many times counting has been initialised/occured during the running time of the program
# Advantages:
#     understanding the algorithms
#     counting frequencey

# counting even numbers from 1 to n
# def count_even(n):
#     count = 0
#     for i in range(1, n+1):
#         if i % 2 == 0:
#             count += 1
#     return count
# def main():
#     n=int(input("Enter the value of n: "))
#     print("Count of even numbers from 1 to", n, "is", count_even(n))
# if __name__ == "__main__":
#     main()

# counting positive numbers
def count_positive(numbers):
    count = 0
    for i in range(-5, 10):
        if i > 0:
            count += 1
    return count
def main():
    numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    print("Count of positive numbers is", count_positive(numbers))
if __name__ == "__main__":
    main()
