import json

USERS_FILE = "users.json"

def load_users():
    """Load user data from file."""
    try:
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_users(users):
    """Save users data to file."""
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)

def register_user():
    """Register a new user with a specific role."""
    users = load_users()
    username = input("🆕 Enter username: ")
    if username in users:
        print("⚠️ User already exists!")
        return
    password = input("🔑 Enter password: ")
    role = input("👤 Enter role (doctor/diagnostic/pharmacy): ").strip().lower()
    if role not in ["doctor", "diagnostic", "pharmacy"]:
        print("⚠️ Invalid role! Try again.")
        return
    
    users[username] = {"password": password, "role": role, "balance": 0}
    save_users(users)
    print("✅ Registration successful!")

def login():
    """User login function."""
    users = load_users()
    username = input("👤 Enter username: ")
    password = input("🔑 Enter password: ")

    if username in users and users[username]["password"] == password:
        print(f"✅ Login successful! Welcome, {username}.")
        return username, users[username]["role"]
    
    print("⚠️ Invalid username or password!")
    return None, None
