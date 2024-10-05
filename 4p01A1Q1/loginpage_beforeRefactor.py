# This code has NOT been refactored.

# Database with users
stored_username = "admin"
stored_password = "123"

failed_attempts = 0

def login(username, password) :
    # Check 
    if username == stored_username and password == stored_password:
        return f"Login successful! Welcome, {username}"
    else:
        return "Login failed! Invalid username or password."

if __name__ == "__main__":
    print("Welcome to the login page!")

    #3 login attempts
    while failed_attempts < 3:
        # Get the username and password from the user
        user = input("Enter your username: ")
        pwd = input("Enter your password: ")
        result = login(user, pwd)
        print(result)

        # Check valid login
        if "successful" in result:
            break
        else:
            failed_attempts += 1
            
        # lockout 
        if failed_attempts >= 3:
            print("Account locked. Too many failed attempts.")
            break


