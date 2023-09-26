name = input("Enter name: ")
while True:
    print("(H)ello\n(G)oodbye\n(Q)uit")
    choice = input(">>> ").upper()

    if choice == 'Q':
        break
    elif choice == 'H':
        print(f"Hello {name}")
    elif choice == 'G':
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
print("Finished.")
