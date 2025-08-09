import os

file_details = "myregister.txt"

class LoginRegister:
    def details(self):
        print("1: Register")
        print("2: Login")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            self.name = input("Ente" \
            "" \
            "r your name: ")
            self.gender = input("Enter your gender: ")
            self.age = input("Enter your age: ")
            self.password = input("Enter your password (only in integers): ")

            
            with open(file_details, "a") as file:
                file.write(f"{self.name};{self.gender};{self.age};{self.password}\n")

            print("Registration successful!\n")

        elif choice == 2:
            if not os.path.exists(file_details):
                print("No users registered yet! Please register first.\n")
                self.details()
                return

            name = input("Enter your name: ")
            password = input("Enter your password: ")

            found = False
            with open(file_details, "r") as file:
                users = file.readlines()

            for user in users:
                stored_name, stored_gender, stored_age, stored_password = user.strip().split(";")
                if stored_name == name and stored_password == password:
                    print(f"Login successful! Welcome, {stored_name}.")
                    found = True
                    break

            if not found:
                print("User not found! Registering you now...\n")
                self.details()

        else:
            print("Invalid choice! Try again.\n")
            self.details()

s1 = LoginRegister()
s1.details()


            