import csv
import os

def create_file():
    if not os.path.exists("tickets.csv"):
        with open("tickets.csv","w",newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Ticket ID","User Name","Issue","Priority","Status"])

def create_ticket():
    ticket_id = input("Ticket ID: ")
    user = input("User Name: ")
    issue = input("Issue Description: ")
    priority = input("Priority (High/Medium/Low): ")

    with open("tickets.csv","a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow([ticket_id,user,issue,priority,"Open"])

    print("Ticket Created Successfully")

def view_tickets():
    with open("tickets.csv","r") as file:
        reader = csv.reader(file)
        print("\nALL TICKETS\n")
        for row in reader:
            print(row)

def search_ticket():
    search_id = input("Enter Ticket ID: ")
    found = False
    with open("tickets.csv","r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == search_id:
                print("\nTicket Found")
                print(row)
                found = True
    if not found:
        print("Ticket Not Found")

def update_ticket():
    ticket_id = input("Enter Ticket ID: ")
    new_status = input("New Status (Open/In Progress/Resolved): ")
    rows = []
    with open("tickets.csv","r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == ticket_id:
                row[4] = new_status
            rows.append(row)

    with open("tickets.csv","w",newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Status Updated")

def close_ticket():
    ticket_id = input("Enter Ticket ID: ")
    rows = []
    with open("tickets.csv","r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == ticket_id:
                row[4] = "Closed"
            rows.append(row)

    with open("tickets.csv","w",newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Ticket Closed")

create_file()

while True:
    print("\\n===== HELP DESK TICKETING SYSTEM =====")
    print("1. Create Ticket")
    print("2. View Tickets")
    print("3. Search Ticket")
    print("4. Update Ticket")
    print("5. Close Ticket")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        create_ticket()
    elif choice == "2":
        view_tickets()
    elif choice == "3":
        search_ticket()
    elif choice == "4":
        update_ticket()
    elif choice == "5":
        close_ticket()
    elif choice == "6":
        break
    else:
        print("Invalid Choice")
