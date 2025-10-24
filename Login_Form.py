import time
import getpass  # For hiding PIN input

max_attempt = 3

# Correct login details
corr_username = "student"
corr_pin = 1234

attempts = 0
login = False

print("🎓 Welcome to the Secure Login Portal 🎓\n")

while attempts < max_attempt:
    print("Please input your details:")
    name = input("👤 Username: ")

    # Use getpass to hide PIN as it's typed (optional)
    try:
        pin = int(getpass.getpass("🔐 PIN: "))
    except ValueError:
        print("⚠️ Invalid input! PIN must be numbers only.\n")
        continue  # Restart this loop iteration

    if name == corr_username and pin == corr_pin:
        print("\n✅ You are logged in successfully!\n")
        login = True
        break
    else:
        attempts += 1
        remaining_attempts = max_attempt - attempts
        print("❌ WRONG Username or PIN. Please try again.")

        if remaining_attempts > 0:
            print(f"⏳ You have {remaining_attempts} attempt(s) left.\n")
        else:
            print("\n🚫 Too many failed attempts. Please wait 20 seconds...")
            time.sleep(20)
            # Option to retry
            retry = input("Would you like to try again? (y/n): ").lower()
            if retry == "y":
                attempts = 0  # reset attempts
            else:
                print("👋 Goodbye!")
                break

if not login:
    raise SystemExit(0)
