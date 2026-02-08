"""
Cinema Ticket Pre-Sale (COP 2373 Programming II)

This program pre-sells a limited number of cinema tickets.
Rules:
- A buyer can purchase 1 to 4 tickets per transaction.
- No more than 20 tickets total can be sold.
- After each purchase, the program displays how many tickets remain.
- The program repeats until all tickets are sold, then displays the total number of buyers.
"""

TOTAL_TICKETS = 20
MAX_PER_BUYER = 4


def request_tickets(tickets_remaining: int) -> int:
    """
    Prompt the user for how many tickets they want to buy and validate the input.

    Parameters:
        tickets_remaining (int): The number of tickets currently available.

    Variables:
        raw (str): The user's input as a string.
        requested (int): The validated number of tickets the buyer wants.

    Logic:
        1. Loop until a valid request is entered.
        2. Ask the user for a number of tickets.
        3. Validate that the input is an integer.
        4. Validate that the number is between 1 and 4.
        5. Validate that the number does not exceed tickets_remaining.
        6. Return the validated requested value.

    Return:
        int: The number of tickets the buyer will purchase (1-4, and <= tickets_remaining).
    """
    while True:
        raw = input(f"How many tickets would you like to buy (1-{MAX_PER_BUYER})? "
                    f"Tickets remaining: {tickets_remaining} >>> ").strip()
        try:
            requested = int(raw)
        except ValueError:
            print("Please enter a whole number (example: 1, 2, 3, 4).")
            continue

        if requested < 1 or requested > MAX_PER_BUYER:
            print(f"Each buyer can purchase 1 to {MAX_PER_BUYER} tickets.")
        elif requested > tickets_remaining:
            print(f"Only {tickets_remaining} ticket(s) remain. Please enter {tickets_remaining} or less.")
        else:
            return requested


def apply_purchase(tickets_remaining: int, requested: int) -> int:
    """
    Subtract the purchased tickets from the remaining ticket count.

    Parameters:
        tickets_remaining (int): Tickets available before the purchase.
        requested (int): Tickets requested by the buyer (already validated).

    Variables:
        updated_remaining (int): Tickets available after subtracting requested.

    Logic:
        1. Compute updated_remaining = tickets_remaining - requested.
        2. Return updated_remaining.

    Return:
        int: The updated number of tickets remaining after the purchase.
    """
    updated_remaining = tickets_remaining - requested
    return updated_remaining


def main() -> None:
    """
    Control the ticket pre-sale loop until tickets are sold out, then report totals.

    Parameters:
        None

    Variables:
        tickets_remaining (int): Accumulator that tracks the tickets still available.
        buyers (int): Accumulator that counts how many buyers completed a purchase.
        requested (int): Tickets requested for the current buyer.

    Logic:
        1. Initialize tickets_remaining to TOTAL_TICKETS and buyers to 0.
        2. Loop while tickets_remaining > 0:
            a. Call request_tickets to get a validated ticket request.
            b. Call apply_purchase to update tickets_remaining.
            c. Increment buyers by 1.
            d. Display the updated number of remaining tickets.
        3. After the loop ends, display the total number of buyers.

    Return:
        None
    """
    tickets_remaining = TOTAL_TICKETS
    buyers = 0

    print("Cinema Ticket Pre-Sale")
    print("-" * 22)

    while tickets_remaining > 0:
        requested = request_tickets(tickets_remaining)
        tickets_remaining = apply_purchase(tickets_remaining, requested)
        buyers += 1  # accumulator (count buyers)

        if tickets_remaining > 0:
            print(f"Purchase complete! Tickets remaining: {tickets_remaining}\n")
        else:
            print("Purchase complete! Tickets remaining: 0\n")

    print(f"Sold out! Total number of buyers: {buyers}")


if __name__ == "__main__":
    main()
