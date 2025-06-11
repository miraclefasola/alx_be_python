def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("please, add an item: ")
            if item:
                shopping_list.append(item)
                print(f"{item} added to your shopping list")
            else:
                print("item cannot be empty")
            pass
        elif choice == '2':
            # Prompt for and remove an item
            item = input("please remove an item: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed")

            else:
                print(f"{item} not found in shopping list")
            pass
        elif choice == '3':
            # Display the shopping list
            if not shopping_list:
                print("shopping list is empty")
            else:
                print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()