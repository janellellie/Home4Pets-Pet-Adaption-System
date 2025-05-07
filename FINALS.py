pets = {
    "1": {"name": "Casey", "type": "Dog", "age": 2},
    "2": {"name": "Bambi", "type": "Dog", "age": 1},
    "3": {"name": "Oreo", "type": "Cat", "age": 3},
    "4": {"name": "Luna", "type": "Cat", "age": 5},
    "5": {"name": "Tofu", "type": "Hamster", "age": 1},
    "6": {"name": "Pickles", "type": "Hamster", "age": 2},
}

adopters = {} 

print("+" + "=" * 20 + "+")
print("| Welcome to Home4Pets |")
print("+" + "=" * 20 + "+")

start = input("\nDo you want to proceed? (y/n): ")

if start.lower() == "y":
    while True:
        if not pets:
            print("\nAll pets have been adopted. Thank you for your support!")
            break

        print("\nWhat do you want to do with Home4Pets?")
        print("\nOptions: ")
        print("1. View Available Pets")
        print("2. Adopt Pet")
        print("3. View Adopters List")
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
            print("\nChoose a pet to adopt:")
            pet_choice = input("Enter the number of the pet you want to adopt: ")

            if pet_choice in pets:
                selected_pet = pets[pet_choice]
                print(f"\nYou selected {selected_pet['name']} the {selected_pet['type']}!")
                proceed_decision = input("Do you want to proceed with the adoption process? (y/n): ")

                if proceed_decision.lower() == "y":
                    print("\nPlease provide your details to continue as a pet owner:")
                    name = input("Name: ")
                    age = input("Age: ")
                    phone_number = input("Phone number: ")
                    address = input("Address: ")

                    adopters[name] = {
                        "age": age,
                        "phone_number": phone_number,
                        "address": address,
                        "adopted_pet": selected_pet
                    }

                    print(f"\nThank you for registering, {name}")
                    print(f"and Congratulations on adopting {selected_pet['name']} the {selected_pet['type']}!")

                    del pets[pet_choice]

                elif proceed_decision.lower() == "n":
                    print("\nReturning to the main options.")
                else:
                    print("\nInvalid input. Returning to the main options.")
            else:
                print("\nPlease choose another pet.")

        elif choice == "3":
            if adopters:
                print("\nList of Adopters:")
                for adopter_name, details in adopters.items():
                    pet = details['adopted_pet']
                    print(f"\nAdopter: {adopter_name}")
                    print(f"  Age: {details['age']}")
                    print(f"  Phone: {details['phone_number']}")
                    print(f"  Address: {details['address']}")
                    print(f"  Adopted Pet: {pet['name']} the {pet['type']} (Age: {pet['age']})")
                    print("-" * 30)
            else:
                print("\nNo pets have been adopted yet.")

        elif choice == "4":
            print("\nThank you for visiting Home4Pets. Goodbye!")
            break

        else:
            print("\nInvalid choice! Please select a valid option.")
else:
    print("\nThank you! Have a great day!")
