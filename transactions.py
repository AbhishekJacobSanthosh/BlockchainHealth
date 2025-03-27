from blockchain import load_blockchain, save_blockchain, create_block
from users import load_users, save_users

def add_patient(doctor):
    """Doctor adds a new patient (Genesis Block)."""
    patient_id = input("🆕 Enter Patient ID: ")
    transactions = [f"Doctor {doctor} added Patient {patient_id}"]
    blockchain = create_block("0" * 64, transactions)
    print("✅ Patient added successfully!")

def update_patient(doctor):
    """Doctor updates patient details."""
    patient_id = input("🔄 Enter Patient ID to update: ")
    new_data = input("✏️ Enter new patient details: ")
    blockchain = load_blockchain()
    previous_hash = blockchain[-1]["hash"]
    
    transactions = [f"Doctor {doctor} updated Patient {patient_id}: {new_data}"]
    create_block(previous_hash, transactions)
    print("✅ Patient data updated successfully!")

def add_test_results(diagnostic):
    """Diagnostic center adds test results."""
    patient_id = input("🧪 Enter Patient ID for test: ")
    test_result = input("📜 Enter test results: ")
    blockchain = load_blockchain()
    previous_hash = blockchain[-1]["hash"]

    transactions = [f"Diagnostic {diagnostic} added test results for Patient {patient_id}: {test_result}"]
    create_block(previous_hash, transactions)
    
    users = load_users()
    users[diagnostic]["balance"] += 10  # Reward diagnostic center
    save_users(users)
    print("✅ Test results added & balance updated!")

def check_balance(username):
    """Check user balance."""
    users = load_users()
    print(f"💰 Your Balance: {users[username]['balance']} e-cash")
