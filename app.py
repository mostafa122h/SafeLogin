def main():
    print("SafeLogin - Phone Verification System")
    print("1. Send SMS Code")
    print("2. Call with Voice Code")

    choice = input("Choose option: ")

    phone = input("Enter phone number: ")

    if choice == "1":
        from verify_sms import send_sms_verification
        send_sms_verification(phone)
    elif choice == "2":
        from verify_voice import make_voice_call
        make_voice_call(phone)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
