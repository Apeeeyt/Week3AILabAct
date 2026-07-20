def check_borrowing(overdue_books, status):
    if overdue_books == "yes":
        return "Not allowed: overdue books"
    elif status == "suspended":
        return "Not allowed: suspended account"
    elif status == "active":
        return "Borrowing allowed"
    else:
        return "Invalid status"

successful_borrowers = 0

while True:
    name = input("Enter student name (or 'exit' to quit): ").strip().lower()
    
    if name == "exit":
        break
    
    overdue_input = input("Do you have overdue books? (yes/no): ").strip().lower()
    status_input = input("What is your borrower status? (active/suspended): ").strip().lower()
    books_input = int(input("How many books do you want to borrow? (0-3): "))
    
    result = check_borrowing(overdue_input, status_input)
    
    if result == "Borrowing allowed":
        if books_input > 3:
            print(name + ": You requested " + str(books_input) + " books, but maximum is 3. You can borrow 3 books.")
            books_allowed = 3
        elif books_input == 0:
            print(name + ": You're eligible but requested 0 books. Have a nice day!")
            books_allowed = 0
        else:
            books_allowed = books_input
            print(name + ": Borrowing allowed! You can borrow " + str(books_allowed) + " book(s).")
        
        if books_allowed > 0:
            successful_borrowers = successful_borrowers + 1
    elif result == "Not allowed: overdue books":
        print(name + ": Not allowed - you have overdue books")
    elif result == "Not allowed: suspended account":
        print(name + ": Not allowed - your account is suspended")
    else:
        print(name + ": Invalid status entered")

print()
print("Total students allowed to borrow:", successful_borrowers)
