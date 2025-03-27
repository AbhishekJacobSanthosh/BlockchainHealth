from blockchain import Blockchain

blockchain = Blockchain()

def add_patient(username):
    patient_name = input("👤 Enter patient name: ")
    blockchain.new_transaction("Hospital", patient_name, "New patient record created.")
    blockchain.mine_block()
    print(f"✅ Genesis block created for {patient_name}.\n")

def update_patient(username):
    patient = input("👤 Enter patient name: ")
    details = input("📝 Enter update (e.g., 'Blood test ordered'): ")
    
    blockchain.new_transaction(username, patient, details)  # Store actual doctor name
    blockchain.update_balance(username, 10)  # Give doctor incentive
    
    blockchain.mine_block()
    print(f"✅ Transaction added: {username} updated {patient}'s record.\n")

def add_test_results(username):
    patient = input("👤 Enter patient name: ")
    details = input("📊 Enter test results: ")
    
    blockchain.new_transaction(username, patient, details)  # Store actual diagnostic center name
    blockchain.update_balance(username, 10)  # Give incentive
    
    blockchain.mine_block()
    print(f"✅ Test results added for {patient}.\n")

def access_patient_data():
    blockchain.display_blockchain()

def check_balance(username):
    print(f"💰 Balance for {username}: {blockchain.get_balance(username)}\n")
