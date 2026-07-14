name=["om","ria","sia","tia"]
print(name[0:4])

l1=[8999081760]
print(name[0],":",l1)

l2=[789456123]
print(name[1],":",l2)

l3=[8956789123]
print(name[2],":",l3)

l4=[7856542131]
print(name[3],":", l4)

contacts= {
    "om": 8999081760,
    "ria": 789456123,
    "sia": 8956789123,
    "tia": 7856542131
}
print(contacts["ria"])  
print(contacts["tia"])
print(contacts["om"])
print(contacts["sia"])

def add_contact():  
    name = input("Enter the name of the contact: ")
    number = input("Enter the phone number of the contact: ")
    contacts[name] = number
    print(f"Contact {name} added successfully!")
    
add_contact()
print(contacts)
for name, number in contacts.items():
    print(f"{name}: {number}")
    
    
view_contact = input("Enter the name of the contact you want to view: ")
if view_contact in contacts:
    print(f"{view_contact}:{contacts[view_contact]}")
  
  
search_contact = input("Enter the name of the contact you want to search: ")
if search_contact in contacts:
    print(f"{search_contact}: {contacts[search_contact]}")  
      
    
delete_contact = input("Enter the name of the contact you want to delete: ")
if delete_contact in contacts:
    del contacts[delete_contact]
    
    print(f"Contact {delete_contact} deleted successfully!")