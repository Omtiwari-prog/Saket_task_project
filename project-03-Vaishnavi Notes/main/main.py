p=input("Enter your note: ")
print(f"Your note is: {p}")
if len(p) > 100:
    print("Your note is too long. Please keep it under 100 characters.")
else:  
   with open("notes.txt", "a") as file:
        file.write(p + "\n")
        print("Your note has been saved.")
   
with open("notes.txt", "r") as file:
  print("total notes:",len(open("notes.txt").readlines()))
    
choice = input("Do you want to read your notes? (y/n): ")
if choice.lower() == 'y':
    with open("notes.txt", "r") as file:
     print("Your notes:")
    
    for line in file:   
        print(line.strip()) 