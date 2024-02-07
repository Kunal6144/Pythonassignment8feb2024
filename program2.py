def login():
    # Correct login information
    correct_username = "python"
    correct_password = "rules"

    # Number of attempts
    attempts = 0

    while attempts < 5:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == correct_username and password == correct_password:
            print("Welcome!")
            return  # Exit the function if login is successful

        print("Incorrect username or password. Please try again.")
        attempts += 1

    print("Access denied.")

if __name__ == "__main__":
    login()
