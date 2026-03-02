# def count_char(text):   
#     count = 0
#     for char in text:
#         count += 1
#     return count

# def main():
#     text = input("enter the text: ")
#     print("char count: ", count_char(text))
# if _name_ == "_main_":
#     main()



# def count_vowels(text):   
#     count = 0
#     vowels = "aeiouAEIOU"
#     for char in text:
#         if char in vowels:
#             count += 1
#     return count

# def main():
#     text = input("enter the text: ")
#     print("vowel count: ", count_vowels(text))
# if _name_ == "_main_":
#     main()

#Reversing a string 
def rev_str(text):
    reversed_text= ""
    for char in text:
        reversed_text=char + reversed_text
    return reversed_text
def main():
        text=input("Enter name: ")
        print("Reversed text: ",rev_str(text))
main()