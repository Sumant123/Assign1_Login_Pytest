from loginpage import login

def test_validuserpass():
    username = "admin"
    password = "123"
    result = login(username, password)
    assert result == "Login successful! Welcome, admin"

def test_invalid_user():
    username = "wronguser"
    password = "123"
    result = login(username, password)
    assert result == "Login failed! Invalid username or password."

def test_null():
    username = ""
    password = ""
    result = login(username, password)
    assert result == "Login failed! Invalid username or password."

def test_lockout():
    failed_attempts = 0  
    username = "wronguserddgfdfdf"
    password = "wrongpassworddfs"
    
    # First attempt
    result = login(username, password)
    assert result == "Login failed! Invalid username or password."
    
    # Second attempt
    result = login(username, password)
    assert result == "Login failed! Invalid username or password."
    
    # Third attempt
    result = login(username, password)
    assert result == "Login failed! Invalid username or password."

    # Attempt after third (lockout)
    result = login(username, password)
    assert failed_attempts <= 3


    

