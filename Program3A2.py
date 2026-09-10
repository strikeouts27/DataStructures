# Program3A2
# Andrew Stribling
# This program will check a number and than determine if the number is greater than 300. If it is not, it will ask the user to enter in an number greater than 300. 
# Once the user inputs a number greater than 300, it will divide the number by 5 and display it to 2 decimal points. 
# It will than add 105 to the number and than subtract by 34 and than multiply by 2. 

def main():
    number = int(input("Please enter a number: "))
    if number > 300:
        print("Please enter a valid number.")
    elif number <= 300:
        print("Is the number even or odd?")
        new_number = float(number/5)
        print(f"The number divided by 5 is: {new_number:.2f}")
        new_number += 105
        new_number -= 34
        new_number *= 2
        print(f"The final result is: {new_number}")
    else:
        print("Please enter a valid number.")
if __name__ == "__main__":
    main()