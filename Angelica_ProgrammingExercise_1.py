"""
Angelica C. Muñoz
COP 2373 - Programming II
Programming Exercise 1 - Cinema Ticket Pre-Sale
"""

TOTAL_TICKETS = 20
MAX_TICKETS_PER_BUYER = 4


def get_ticket_request(tickets_remaining):
    """
    Description:
        Prompts the user for how many tickets they want to purchase and validates
        the request based on the course rules:
        - Each buyer may purchase up to 4 tickets.
        - A buyer cannot purchase more tickets than remain available.
        - The user must enter a positive whole number.

    Parameters:
        tickets_remaining (int): The number of tickets still available for sale.

    Variables:
        max_allowed (int): The maximum number of tickets the buyer may request.
        user_input (str): Raw input entered by the user.
        requested_tickets (int): The validated number of tickets requested.

    Logical Steps:
        1. Determine the maximum allowed tickets for this buyer.
        2. Prompt the user for an amount.
        3. Validate that the input is an integer.
        4. Validate that the integer is within the allowed range.
        5. Repeat until a valid request is entered.
        6. Return the validated request.

    Returns:
        int: The validated number of tickets requested by the buyer.
    """

    # Calculate the maximum tickets allowed for this purchase
    max_allowed = min(MAX_TICKETS_PER_BUYER, tickets_remaining)

    while True:
        # Ask the user for the number of tickets they want to buy
        user_input = input(
            f"How many tickets would you like to buy (1-{max_allowed})? "
        ).strip()

        try:
            # Convert the user's input to an integer
            requested_tickets = int(user_input)
        except ValueError:
            # Explain why the input was rejected
            print("Please enter a whole number (example: 2).")
            continue

        # Ensure the request is within the allowed range
        if 1 <= requested_tickets <= max_allowed:
            return requested_tickets

        # Explain why the request was rejected
        print(
            f"Invalid amount. You can buy between 1 and {max_allowed} tickets."
        )


def run_ticket_presale():
    """
    Description:
        Runs the cinema ticket pre-sale until all tickets are sold.
        Tracks the number of buyers and reports remaining ticket inventory
        after each successful purchase.

    Parameters:
        None

    Variables:
        tickets_remaining (int): Tracks how many tickets are still available.
        buyers_count (int): Accumulator that tracks the total number of buyers.
        requested_tickets (int): The number of tickets requested by the buyer.

    Logical Steps:
        1. Set tickets remaining to the total tickets available.
        2. Initialize buyers_count to 0.
        3. While tickets remain:
            a. Get a valid ticket request from the buyer.
            b. Subtract the request from tickets remaining.
            c. Increment buyers_count by 1.
            d. Display the remaining tickets.
        4. When tickets are sold out, display the total buyers.

    Returns:
        None
    """

    # Start with the total number of tickets available
    tickets_remaining = TOTAL_TICKETS

    # Accumulator to count how many buyers successfully purchased tickets
    buyers_count = 0

    print("Cinema Ticket Pre-Sale")
    print("----------------------")

    while tickets_remaining > 0:
        # Get a validated ticket request based on remaining inventory
        requested_tickets = get_ticket_request(tickets_remaining)

        # Reduce the inventory by the number of tickets purchased
        tickets_remaining -= requested_tickets

        # Count this purchase as one buyer
        buyers_count += 1

        # Display how many tickets remain after the purchase
        print(f"Tickets remaining: {tickets_remaining}")

        # Confirm when inventory is sold out
        if tickets_remaining == 0:
            print("All tickets have been sold.")

    print(f"Total number of buyers: {buyers_count}")


if __name__ == "__main__":

    run_ticket_presale()
