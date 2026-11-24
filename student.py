
                
               
                






import json


def student():

    data = {}

    def save(data):
        with open("student.json", "w") as f:
            json.dump(data, f, indent=4)

    def give_roll():
        roll = int(input("Enter the roll number: "))
        print("Roll number created")
        return roll

    def add(roll):
        num = int(input("Enter the roll number: "))

        if num == roll:
            name = input("Enter the name: ")
            c = input("Enter the class: ")
            age = input("Enter the age: ")
            section = input("Enter the section: ")

            data[num] = {
                "name": name,
                "class": c,
                "age": age,
                "section": section
            }

            save(data)
            print("Student added successfully!")

        else:
            print("Roll number does not match.")

    while True:

        user_input = int(input(
            "\n1. Press 1 for entering roll number\n"
            "2. Press 2 for adding student\n"
            "3. Press 3 for deleting student\n"
            "4. Press 4 for updating student\n"
            "5. Press 5 for exit\n"
            "Enter your choice: "
        ))

        if user_input == 1:
            roll = give_roll()

        elif user_input == 2:
            try:
                add(roll)
            except NameError:
                print("Please enter the roll number first.")

        elif user_input == 3:
            print("Delete student")

        elif user_input == 4:
            print("Update student")

        elif user_input == 5:
            print("Program exited.")
            break

        else:
            print("Invalid choice. Please try again.")


student()