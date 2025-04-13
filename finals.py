pets = {
    "1": {"name": "Bella", "type": "Dog", "age": 2},
    "2": {"name": "Max", "type": "Cat", "age": 1},
    "3": {"name": "Charlie", "type": "Rabbit", "age": 3},
    "4": {"name": "Lucy", "type": "Parrot", "age": 5},
    "5": {"name": "Daisy", "type": "Hamster", "age": 1}
}

print("+" + "="*20 + "+")
print("| Welcome to Home4Pets |")
print("+" + "="*20 + "+")

start = input("Do you want to proceed? (y/n): ")

if start.lower() == "y":  
    while True:
        print("\nWhat do you want to do with Home4Pets?")

        print("Options: ")
        print("1. View Available Pets")
        print("2. Register Adopter")
        print("3. Adopt Pet")
        print("4. Exit")

        choice = input("Your Choice (1/2/3/4): ")

        if choice == "1":
            print("\nAvailable Pets:")
            for pet_id, pet_info in pets.items():
                print(f"ID: {pet_id}")
                print(f"  Name: {pet_info['name']}")
                print(f"  Type: {pet_info['type']}")
                print(f"  Age: {pet_info['age']} years")
                print("-" * 30)

        elif choice == "2":
            print("\nPlease provide your details to register as an adopter:")
            name = input("Name: ")
            age = input("Age: ")
            email = input("Email: ")
            print(f"\nThank you for registering, {name}. We will contact you soon at {email}.")

        elif choice == "3":
            print("\nChoose a pet to adopt:")
            pet_choice = input("Enter the number of the pet you want to adopt (1-5): ")
            if pet_choice in pets:
                print(f"\nCongratulations on adopting {pets[pet_choice]['name']} the {pets[pet_choice]['type']}!")
            else:
                print("\nInvalid pet selection. Please choose a valid number from 1 to 5.")

        elif choice == "4":
            print("\nThank you for visiting Home4Pets. Goodbye!")
            break  # Exits the while loop and ends the program

        else:
            print("\nInvalid choice! Please select a valid option.")
else:
    print("\nThank you! Have a great day!!")