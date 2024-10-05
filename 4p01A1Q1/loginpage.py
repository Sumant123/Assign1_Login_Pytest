# This code has been Refactored

# Database with users
stored_username = "admin"
stored_password = "123"

failed_attempts = 0
max = 3

def login(username, password) :
    # Check 
    if username == stored_username and password == stored_password:
        return f"Login successful! Welcome, {username}"
    else:
        return "Login failed! Invalid username or password."
    
def lockout(failed_attempts) :
     while failed_attempts < max:
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
        if failed_attempts >= max:
            print("Account locked. Too many failed attempts.")
            break

if __name__ == "__main__":
    lockout(failed_attempts)


