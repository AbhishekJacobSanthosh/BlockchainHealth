users = {
    "doctor": {"password": "pass123", "role": "doctor", "balance": 100},
    "diagnostic": {"password": "diag123", "role": "diagnostic", "balance": 100},
    "pharmacy": {"password": "pharm123", "role": "pharmacy", "balance": 100}
}

def register_user():
    username = input("👤 Enter new username: ")
    if username in users:
        print("⚠️ User already exists!\n")
        return
    password = input("🔑 Enter password: ")
    role = input("🔷 Enter role (doctor/diagnostic/pharmacy): ").lower()
    
    if role not in ["doctor", "diagnostic", "pharmacy"]:
        print("❌ Invalid role! Must be doctor, diagnostic, or pharmacy.\n")
        return

    users[username] = {"password": password, "role": role, "balance": 100}  # Default balance
    print(f"✅ User {username} registered as {role} successfully!\n")

def login():
    username = input("👤 Enter username: ")
    password = input("🔑 Enter password: ")
    if username in users and users[username]["password"] == password:
        print(f"✅ Login successful! Welcome, {username} ({users[username]['role']}).\n")
        return username, users[username]["role"]
    
    print("❌ Invalid credentials!\n")
    return None, None
