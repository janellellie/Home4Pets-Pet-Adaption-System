pets = {}
adopters = {}
next_pet_id = 1  

print("\n======================")
print("  Welcome to Home4Pets")
print("======================")

start = input("\nDo you want to proceed? (y/n): ")

if start.lower() != "y":
    print("\nThank you! Have a great day!")
else:
    while True:
        print("\nWhat do you want to do?")
        print("1. Manage Pets (Add or Delete)")
        print("2. View Available Pets")
        print("3. Adopt a Pet")
        print("4. View Adopted Pets")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

       
        if choice == "1":
            print("\na. Add a Pet")
            print("b. Delete a Pet")
            action = input("Choose (a/b): ").lower()

            if action == "a":
                name = input("Pet's Name: ")
                pet_type = input("Type (e.g. Dog, Cat): ")
                age = input("Age: ")

                pet_id = str(next_pet_id)
                pets[pet_id] = {
                    "name": name,
                    "type": pet_type,
                    "age": age
                }
                next_pet_id += 1

                print(f"\n{name} has been added with ID {pet_id}.")

            elif action == "b":
                if not pets:
                    print("\nNo pets to delete.")
                else:
                    for pid, info in pets.items():
                        print(f"{pid}: {info['name']} the {info['type']}")
                    delete_id = input("Enter the pet ID to delete: ")
                    if delete_id in pets:
                        removed = pets.pop(delete_id)
                        print(f"{removed['name']} has been removed.")
                    else:
                        print("Invalid ID.")
            else:
                print("Invalid option.")

        elif choice == "2":
            if not pets:
                print("\nNo pets available right now.")
            else:
                print("\nAvailable Pets:")
                for pid, info in pets.items():
                    print(f"ID: {pid} - Name: {info['name']}, Type: {info['type']}, Age: {info['age']}")

        elif choice == "3":
            if not pets:
                print("\nNo pets available for adoption.")
            else:
                for pid, info in pets.items():
                    print(f"{pid}: {info['name']} the {info['type']}")
                pet_id = input("Enter the ID of the pet you want to adopt: ")

                if pet_id in pets:
                    pet = pets[pet_id]
                    confirm = input(f"Adopt {pet['name']} the {pet['type']}? (y/n): ")
                    if confirm.lower() == "y":
                        name = input("Your Name: ")
                        age = input("Your Age: ")
                        phone = input("Phone Number: ")
                        address = input("Address: ")

                        adopters[name] = {
                            "age": age,
                            "phone": phone,
                            "address": address,
                            "adopted_pet": pet
                        }

                        print(f"\n{name}, you have adopted {pet['name']} the {pet['type']}!")
                        del pets[pet_id]
                    else:
                        print("Adoption cancelled.")
                else:
                    print("Invalid pet ID.")

        elif choice == "4":
            if not adopters:
                print("\nNo pets have been adopted yet.")
            else:
                print("\nAdopted Pets:")
                for name, info in adopters.items():
                    pet = info["adopted_pet"]
                    print(f"{name} adopted {pet['name']} the {pet['type']} (Age: {pet['age']})")
                    print(f"Contact: {info['phone']}, Address: {info['address']}")


        elif choice == "5":
            print("\nThank you for using Home4Pets!")
            break

        else:
            print("Invalid choice. Please try again.")
