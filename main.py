from users import register_user, login
from transactions import add_patient, update_patient, add_test_results, access_patient_data, check_balance
from node import start_node, connect_to_node
import threading

def main():
    threading.Thread(target=start_node, daemon=True).start()

    logged_in_user = None
    user_role = None

    while True:
        if not logged_in_user:
            print("\n🚀 Hospital Blockchain System")
            print("1️⃣ Register User")
            print("2️⃣ Login")
            print("3️⃣ Exit")
            choice = input("🔷 Choose an option: ")

            if choice == "1":
                register_user()
            elif choice == "2":
                logged_in_user, user_role = login()
            elif choice == "3":
                print("👋 Exiting... Goodbye!\n")
                break
            else:
                print("⚠️ Invalid option. Try again!\n")
            continue

        print(f"\n👤 Logged in as {logged_in_user} ({user_role})")
        print("1️⃣ Add Patient")
        print("2️⃣ Update Patient Data")
        print("3️⃣ Add Test Results")
        print("4️⃣ Access Patient Data")
        print("5️⃣ Check Balance")
        print("6️⃣ Connect to Node")
        print("7️⃣ Logout")

        choice = input("🔷 Choose an option: ")

        if choice == "1" and user_role == "doctor":
            add_patient(logged_in_user)
        elif choice == "2" and user_role == "doctor":
            update_patient(logged_in_user)
        elif choice == "3" and user_role == "diagnostic":
            add_test_results(logged_in_user)
        elif choice == "4":
            access_patient_data()
        elif choice == "5":
            check_balance(logged_in_user)
        elif choice == "6":
            connect_to_node()
        elif choice == "7":
            print("🔒 Logged out.\n")
            logged_in_user, user_role = None, None
        else:
            print("⚠️ Invalid option or unauthorized access!\n")

if __name__ == "__main__":
    main()
