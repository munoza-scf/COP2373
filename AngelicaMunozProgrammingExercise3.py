"""
Monthly Expense Analyzer

Author: Angelica C. Muñoz
Date: February 22, 2026

Program Description:
    This program prompts the user to enter their monthly expenses by
    specifying the type of expense and the amount. The program uses
    the reduce() function to calculate the total expense, highest
    expense, and lowest expense. The results are clearly labeled and
    displayed to the user.
"""

from functools import reduce
from typing import List, Tuple


def get_monthly_expenses() -> List[Tuple[str, float]]:
    """
    Collect expense types and amounts from the user.

    Return:
        List of expense tuples (type, amount).
    """
    print("=== Monthly Expense Analyzer ===")
    print("Enter 'done' as the expense type when finished.\n")

    expenses = []

    while True:
        expense_type = input("Enter expense type: ").strip()

        if expense_type.lower() == "done":
            break

        amount = float(input("Enter amount for " + expense_type + ": $"))

        expenses.append((expense_type, amount))

    return expenses


def calculate_total(expenses: List[Tuple[str, float]]) -> float:
    """Calculate total expense using reduce."""
    return reduce(lambda x, y: x + y[1], expenses, 0)


def find_highest_expense(
    expenses: List[Tuple[str, float]]
) -> Tuple[str, float]:
    """Find highest expense using reduce."""
    return reduce(lambda x, y: x if x[1] > y[1] else y, expenses)


def find_lowest_expense(
    expenses: List[Tuple[str, float]]
) -> Tuple[str, float]:
    """Find lowest expense using reduce."""
    return reduce(lambda x, y: x if x[1] < y[1] else y, expenses)


def display_results(
    total: float,
    highest: Tuple[str, float],
    lowest: Tuple[str, float]
) -> None:
    """Display total, highest, and lowest expenses."""
    print("\n--- Expense Summary ---")
    print(f"Total Monthly Expense: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} - ${highest[1]:.2f}")
    print(f"Lowest Expense: {lowest[0]} - ${lowest[1]:.2f}")


def run_expense_analyzer() -> None:
    """Orchestrate program execution."""
    expenses = get_monthly_expenses()

    if not expenses:
        print("No expenses were entered.")
        return

    total = calculate_total(expenses)
    highest = find_highest_expense(expenses)
    lowest = find_lowest_expense(expenses)

    display_results(total, highest, lowest)


if __name__ == "__main__":
    run_expense_analyzer()
