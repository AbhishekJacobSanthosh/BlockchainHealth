from users import register_user, login
from transactions import add_patient, update_patient, add_test_results, check_balance
from node import start_node, connect_to_node
import threading

def main():
    port = int(input("Enter node port: "))
    threading.Thread(target=start_node, args=(port,), daemon=True).start()

    logged_in_user, user_role = None, None

    while True:
        if not logged_in_user:
            print("\n1️⃣ Register User\n2️⃣ Login\n3️⃣ Exit")
            choice = input("🔷 Choose an option: ")
            if choice == "1":
                register_user()
            elif choice == "2":
                logged_in_user, user_role = login()
            elif choice == "3":
                break
            continue

        print(f"\n👤 Logged in as {logged_in_user} ({user_role})")
        if user_role == "doctor":
            print("1️⃣ Add Patient\n2️⃣ Update Patient\n3️⃣ Check Balance\n4️⃣ Logout")
            choice = input("🔷 Choose: ")
            if choice == "1":
                add_patient(logged_in_user)
            elif choice == "2":
                update_patient(logged_in_user)
            elif choice == "3":
                check_balance(logged_in_user)
            elif choice == "4":
                logged_in_user = None

if __name__ == "__main__":
    main()
