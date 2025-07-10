import json
import os
class ContactBook:
    def __init__(self,filename='contacts.json'):
        self.filename=filename
        self.contacts=[]
        self.load_contact()

    def load_contact(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename,'r') as file:
                    self.contacts=json.load(file)
            except json.JSONDecodeError:
                print("⚠️ Warning: File is empty or corrupted. Starting with an empty contact list.")
                self.contacts = []

        else:
            self.contacts=[]

    def save_contacts(self):
        with open(self.filename,'w') as file:
            json.dump(self.contacts,file,indent=4)

    def add_contact(self,name,phone,email,address):
        new_contact={
            'name':name,
            'phone':phone,
            'email':email,
            'address':address
        }
        self.contacts.append(new_contact)
        self.save_contacts()
        print(f"\n✅ New Contact {name} has beed added successfully")
    
    def view_contacts(self):
        if not self.contacts:
            print("📭 No Contact Founded")
            return
        print("\n📒 Contact List:")
        for index,contact in enumerate(self.contacts,start=1):
            print(f"\nContact {index}:")
            print(f"👤 Name   : {contact['name']}")
            print(f"📞 Phone  : {contact['phone']}")
            print(f"📧 Email  : {contact['email']}")
            print(f"🏠 Address: {contact['address']}")
        
    def search_contact(self,search_name):
        found=False
        for index,contact in enumerate(self.contacts,start=1):
            if search_name.lower() in contact['name'].lower():
                print(f"\n🔍 Found Contact {index}:")
                print(f"👤 Name   : {contact['name']}")
                print(f"📞 Phone  : {contact['phone']}")
                print(f"📧 Email  : {contact['email']}")
                print(f"🏠 Address: {contact['address']}")
                found = True

        if not found:
            print(f"\n❌ No contact found with name containing '{search_name}'.")

    def update_contact(self, name_to_update):
        for contact in self.contacts:
            if contact["name"].lower() == name_to_update.lower():
                print(f"\n📝 Updating contact: {contact['name']}")

                new_name = input(f"\nEnter new name (press enter to keep '{contact['name']}'): ") or contact["name"]
                new_phone = input(f"Enter new phone (press enter to keep '{contact['phone']}'): ") or contact["phone"]
                new_email = input(f"Enter new email (press enter to keep '{contact['email']}'): ") or contact["email"]
                new_address = input(f"Enter new address (press enter to keep '{contact['address']}'): ") or contact["address"]

                contact["name"] = new_name
                contact["phone"] = new_phone
                contact["email"] = new_email
                contact["address"] = new_address

                self.save_contacts()
                print(f"\n✅ Contact '{name_to_update}' updated successfully.")
                return

        print(f"\n❌ Contact with name '{name_to_update}' not found.")

    def delete_contact(self,name_to_delete):
        for contact in self.contacts:
            if contact['name'].lower()==name_to_delete.lower():
                self.contacts.remove(contact)
                self.save_contacts()
                print(f"\n🗑️  Contact '{contact['name']}' deleted successfully.")
                return
        print(f"❌ Contact with name '{name_to_delete}' not found.")
 

    
if __name__ == "__main__":
    if __name__ == "__main__":
        book = ContactBook()

        while True:
            print("\n📘 Contact Book Menu")
            print("1️⃣  Add Contact")
            print("2️⃣  View Contacts")
            print("3️⃣  Search Contact")
            print("4️⃣  Delete Contact")
            print("5️⃣  Update Contact")
            print("6️⃣  Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                book.add_contact(name, phone, email, address)

            elif choice == "2":
                book.view_contacts()

            elif choice == "3":
                name = input("Enter name to search: ")
                book.search_contact(name)

            elif choice == "4":
                name = input("Enter name to delete: ")
                book.delete_contact(name)

            elif choice == "5":
                name = input("Enter name to update: ")
                book.update_contact(name)

            elif choice == "6":
                print("👋 Exiting... Goodbye!")
                break

            else:
                print("❌ Invalid choice. Please enter a number between 1 and 6.")
