def display_menu():
            print("\n CONTACT BOOK MENU")
print("=" * 40)
print("1. Add new contact")
print("2. View all contacts")
print("3. Search contact")
print("4. Delete contact")
print("5. Exit")
def add_contact(contacts):
            print("\n ADD NEW CONTACT")
name = input("Enter name: ").strip()
if name in contacts:
            print(f" {name} already exists!")
return
phone = input("Enter phone number: ").strip()
email = input("Enter email: ").strip()
contacts[name] = {
"phone": phone,
"email": email
}
print(f" Contact {name} added successfully!")
def view_contacts(contacts):
       if not contacts:
             print("\n No contacts saved yet!")
return
print("\n ALL CONTACTS")
print("=" * 40)
for name, info in contacts.items():
             print(f"\nName: {name}")
print(f"Phone: {info['phone']}")
print(f"Email: {info['email']}")
print("-" * 40)
def search_contact(contacts):
        name = input("\n Enter name to search: ").strip()
if name in contacts:
        print(f"\n CONTACT FOUND")
print("=" * 40)
print(f"Name: {name}")
print(f"Phone:{ contacts [ ] ['phone']}")
Sample Output:
print(f"Phone: {contacts[name]['phone']}")
print(f"Email: {contacts[name]['email']}")
else:
print(f" Contact {name} not found!")
def delete_contact(contacts):
name = input("\n Enter name to delete: ").strip()
if name in contacts:
del contacts[name]
print(f" Contact {name} deleted successfully!")
else:
print(f" Contact {name} not found!")
# Main program
contacts = {}
print(" WELCOME TO CONTACT BOOK")
while True:
display_menu()
choice = input("\nEnter choice (1-5): ")
if choice == '1':
add_contact(contacts)
elif choice == '2':
view_contacts(contacts)
elif choice == '3':
search_contact(contacts)
elif choice == '4':
delete_contact(contacts)
elif choice == '5':
print("\n Goodbye!")
break
else:
print(" Invalid choice! Please try again.")