def tickets_sales():
    rows = int(input("On how many rows have tickets been sold?: "))
    for i in range(rows):
        tickets = input().strip("->")
        ticket_row, ticket_amount = tickets.split()
        ticket_row_int = int(ticket_row)
        ticket_amount_int = int(ticket_amount)
        if ticket_row_int >= 1 and ticket_row_int <=3:
            ticket_money += 20 * ticket_amount_int
        elif ticket_row_int >= 4 and ticket_row_int <= 10:
            ticket_money += 15 * ticket_amount_int
        else:
            print("Invalid row")
        if ticket_amount_int > 10:
            print("Not available amount of seats on the row")
        
tickets_sales()        