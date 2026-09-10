"""
3A1 Program
Andrew Stribling
This program will ask the user to input the number of pages they read for three books. It will then determine if the user has achieved the reading challenge based on the total number of pages read.
"""
def main():
    book_one = int(input("Hello student, please enter in the number of pages you read for book one: "))
    book_two = int(input("please enter in the number of pages you read for book two: "))
    book_three = int(input("please enter in the number of pages you read for book three: "))
    label = ["Excellent", "Good", "You do not achieve the challenge."]

    if book_one + book_two + book_three > 650:
        print(label[0])
    elif book_one + book_two + book_three > 500:
        print(label[1])
    else:
        print(label[2])

if __name__ == "__main__":
    main()
