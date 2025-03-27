from users import register_user, login
from transactions import add_patient, update_patient, add_test_results, access_patient_data, check_balance
from node import start_node, connect_to_node
import threading

def main():
    logged_in_user = None
    user_role = None
    node_thread = None

    while True:
        if not logged_in_user:
            print("\n🚀 Hospital Blockchain System")
            print("1️⃣ Register User")
            print("2️⃣ Login")
            print("3️⃣ Start a Node")
            print("4️⃣ Connect to an Existing Node")
            print("5️⃣ Exit")
            choice = input("🔷 Choose an option: ")

            if choice == "1":
                register_user()
            elif choice == "2":
                logged_in_user, user_role = login()
            elif choice == "3":
                port = int(input("🛠️ Enter the port number to start the node on: "))
                node_thread = threading.Thread(target=start_node, args=(port,), daemon=True)
                node_thread.start()
            elif choice == "4":
                port = int(input("🔗 Enter the port number to connect to: "))
                connect_to_node(port)
            elif choice == "5":
                print("👋 Exiting... Goodbye!\n")
                break
            else:
                print("⚠️ Invalid option. Try again!\n")
            continue

        print(f"\n👤 Logged in as {logged_in_user} ({user_role})")

        if user_role == "doctor":
            print("1️⃣ Add Patient")
            print("2️⃣ Update Patient Data")
            print("3️⃣ Access Patient Data")
            print("4️⃣ Check Balance")
            print("5️⃣ Logout")
        elif user_role == "diagnostic":
            print("1️⃣ Add Test Results")
            print("2️⃣ Access Patient Data")
            print("3️⃣ Check Balance")
            print("4️⃣ Logout")
        elif user_role == "pharmacy":
            print("1️⃣ Access Patient Data (Prescriptions)")
            print("2️⃣ Check Balance")
            print("3️⃣ Logout")

        choice = input("🔷 Choose an option: ")

        if user_role == "doctor":
            if choice == "1":
                add_patient(logged_in_user)
            elif choice == "2":
                update_patient(logged_in_user)
            elif choice == "3":
                access_patient_data()
            elif choice == "4":
                check_balance(logged_in_user)
            elif choice == "5":
                print("🔒 Logged out.\n")
                logged_in_user, user_role = None, None
            else:
                print("⚠️ Invalid option!\n")

        elif user_role == "diagnostic":
            if choice == "1":
                add_test_results(logged_in_user)
            elif choice == "2":
                access_patient_data()
            elif choice == "3":
                check_balance(logged_in_user)
            elif choice == "4":
                print("🔒 Logged out.\n")
                logged_in_user, user_role = None, None
            else:
                print("⚠️ Invalid option!\n")

        elif user_role == "pharmacy":
            if choice == "1":
                access_patient_data()
            elif choice == "2":
                check_balance(logged_in_user)
            elif choice == "3":
                print("🔒 Logged out.\n")
                logged_in_user, user_role = None, None
            else:
                print("⚠️ Invalid option!\n")

if __name__ == "__main__":
    main()
