"""
Spam Scanner (Keyword-Based)

Author: Angelica C. Munoz
Date: February 15, 2026

Program Description:
    This program asks the user to enter an email message and then scans the
    message for 30 common spam/phishing trigger words or phrases. Each time a
    trigger appears in the message, the program adds 1 point to the spam score.
    Finally, the program displays the spam score, a likelihood rating, and
    which triggers were found (with counts).
"""

from __future__ import annotations

import re
from typing import Dict, List, Tuple


TRIGGERS: List[str] = [
    "free",
    "100% free",
    "risk-free",
    "guaranteed",
    "winner",
    "you're a winner",
    "congratulations",
    "act now",
    "limited time",
    "limited time offer",
    "urgent",
    "urgent action required",
    "click here",
    "call now",
    "earn cash",
    "make money fast",
    "cash bonus",
    "get paid",
    "financial freedom",
    "work from home",
    "no catch",
    "exclusive deal",
    "free trial",
    "verify your account",
    "account will be closed",
    "password reset",
    "wire transfer",
    "gift card",
    "miracle cure",
    "no prescription needed"
]


def get_spam_triggers() -> List[str]:
    """
    Brief description:
        Return the list of 30 words/phrases commonly found in spam/phishing.

    Parameters (name: type):
        None

    Variables (name: type):
        None

    Logical steps:
        1. Return the TRIGGERS constant list.

    Return:
        list[str]: The list of spam trigger words/phrases.
    """
    # Return the constant list so the trigger data is centralized.
    return TRIGGERS


def normalize(text: str) -> str:
    """
    Brief description:
        Normalize text so matching is consistent and case-insensitive.

    Parameters (name: type):
        text (str): The text to normalize.

    Variables (name: type):
        normalized (str): The normalized version of the input text.

    Logical steps:
        1. Convert text to lowercase.
        2. Replace hyphens with spaces so "risk-free" matches "risk-free".
        3. Collapse multiple whitespace characters into a single space.
        4. Strip leading/trailing whitespace.
        5. Return the normalized string.

    Return:
        str: Normalized text used for consistent searching.
    """
    # Lowercase to avoid missing matches due to capitalization differences.
    normalized = text.lower()

    # Replace hyphens so hyphenated and spaced phrases match consistently.
    normalized = normalized.replace("-", " ")

    # Collapse repeated whitespace for reliable phrase matching.
    normalized = re.sub(r"\s+", " ", normalized).strip()

    return normalized


def get_email_message_from_user() -> str:
    """
    Brief description:
        Read a multi-line email message until the user enters a blank line.

    Parameters (name: type):
        None

    Variables (name: type):
        lines (list[str]): Stores each line of the user's message.
        line (str): A single line of input from the user.
        message (str): The final message assembled from all lines.

    Logical steps:
        1. Prompt the user for an email message.
        2. Read lines until a blank line is entered.
        3. Join the lines into one message.
        4. Return the message.

    Return:
        str: The full email message entered by the user.
    """
    # Give clear directions so the user knows how to finish input.
    print("=== Spam Scanner ===")
    print("Enter the email message below.")
    print("When you are finished, press Enter on a blank line.\n")

    # Store lines because emails are often multiple lines.
    lines: List[str] = []

    while True:
        # Read one line of input from the user.
        line = input()

        # A blank line signals the end of the email message.
        if line == "":
            break

        # Keep each non-blank line to assemble the full email later.
        lines.append(line)

    # Join all lines into one message for scanning.
    message = "\n".join(lines).strip()

    return message


def count_trigger_occurrences(message: str, trigger: str) -> int:
    """
    Brief description:
        Count how many times a trigger word/phrase appears in the message.

    Parameters (name: type):
        message (str): The full email message.
        trigger (str): One trigger word or phrase to search for.

    Variables (name: type):
        normalized_message (str): Normalized message text.
        normalized_trigger (str): Normalized trigger text.
        tokens (list[str]): Words in the trigger phrase.
        pattern (str): Regex pattern used for whole-word/phrase matching.
        matches (list[str]): List of matched occurrences.

    Logical steps:
        1. Normalize the message and trigger.
        2. Split the trigger into tokens (words).
        3. Build a whole-word/phrase regex pattern using token boundaries.
        4. Find all matches in the message.
        5. Return the number of matches.

    Return:
        int: The number of occurrences of the trigger in the message.
    """
    # Normalize both strings so matching is consistent.
    normalized_message = normalize(message)
    normalized_trigger = normalize(trigger)

    # Split the trigger into individual words for phrase matching.
    tokens = normalized_trigger.split()

    # Match the full phrase with flexible whitespace between tokens.
    pattern = r"\b" + r"\s+".join(re.escape(t) for t in tokens) + r"\b"

    # Find all occurrences of the trigger in the message.
    matches = re.findall(pattern, normalized_message, flags=re.IGNORECASE)

    return len(matches)


def scan_message_for_spam(
    message: str,
    triggers: List[str],
) -> Tuple[int, Dict[str, int]]:
    """
    Brief description:
        Scan a message for all triggers and calculate a spam score.

    Parameters (name: type):
        message (str): The email message entered by the user.
        triggers (list[str]): The list of trigger words/phrases.

    Variables (name: type):
        score (int): Total spam score (sum of all trigger occurrences).
        found (dict[str, int]): Triggers found and their counts.
        trigger (str): The current trigger being scanned.
        count (int): Occurrence count for the current trigger.

    Logical steps:
        1. Initialize score to 0 and found to an empty dictionary.
        2. Loop through each trigger in triggers.
        3. Count occurrences of the trigger in the message.
        4. If count > 0, store it and add to score.
        5. Return score and found.

    Return:
        tuple[int, dict[str, int]]: (spam score, triggers found with counts)
    """
    # Initialize score and a dictionary to track which triggers were found.
    score = 0
    found: Dict[str, int] = {}

    for trigger in triggers:
        # Count occurrences so repeated spam wording increases the score.
        count = count_trigger_occurrences(message, trigger)

        # Only keep triggers that actually appear in the message.
        if count > 0:
            found[trigger] = count
            score += count

    return score, found


def rate_spam_likelihood(score: int) -> str:
    """
    Brief description:
        Convert a spam score into a human-readable likelihood rating.

    Parameters (name: type):
        score (int): The spam score calculated from scanning the message.

    Variables (name: type):
        None

    Logical steps:
        1. Use thresholds to map score to a rating string.
        2. Return the rating string.

    Return:
        str: A likelihood rating describing how spammy the message appears.
    """
    # Use thresholds to describe risk in a consistent way.
    if score <= 2:
        return "Unlikely spam"

    if score <= 6:
        return "Possibly spam (suspicious)"

    if score <= 11:
        return "Likely spam"

    return "Very likely spam"


def display_results(score: int, rating: str, found: Dict[str, int]) -> None:
    """
    Brief description:
        Display the spam score, rating, and triggers found with counts.

    Parameters (name: type):
        score (int): Total spam score.
        rating (str): Likelihood rating based on the score.
        found (dict[str, int]): Triggers found and their counts.

    Variables (name: type):
        trigger (str): Trigger currently being printed.

    Logical steps:
        1. Display the score and rating.
        2. If triggers were found, display each trigger and count.
        3. Otherwise, display a no-triggers message.

    Return:
        None
    """
    # Print the headline results first so the user sees the score immediately.
    print("\n--- Results ---")
    print(f"Spam score: {score}")
    print(f"Likelihood rating: {rating}")

    if not found:
        # Tell the user clearly when no trigger phrases were detected.
        print("\nNo spam triggers were found in the message.")
        return

    print("\nTriggers found (trigger: count):")

    # Sort for readability: most frequent triggers first.
    for trigger in sorted(found, key=lambda k: (-found[k], k.lower())):
        print(f"  - {trigger}: {found[trigger]}")


def run_spam_scanner() -> None:
    """
    Brief description:
        Orchestrate the spam scanner flow from input to results.

    Parameters (name: type):
        None

    Variables (name: type):
        message (str): The user's email message.
        triggers (list[str]): Trigger list used for scanning.
        score (int): Calculated spam score.
        found (dict[str, int]): Triggers found in the message.
        rating (str): Likelihood rating based on the score.

    Logical steps:
        1. Read the email message from the user.
        2. If message is empty, exit gracefully.
        3. Load triggers.
        4. Scan the message to get score and found triggers.
        5. Rate the score.
        6. Display results.

    Return:
        None
    """
    # Get the email message from the user.
    message = get_email_message_from_user()

    # Exit gracefully if the user did not enter any text.
    if not message:
        print("\nNo message was entered. The program will now exit.")
        return

    # Load triggers from the centralized list.
    triggers = get_spam_triggers()

    # Calculate spam score and gather triggers that appeared.
    score, found = scan_message_for_spam(message, triggers)

    # Convert numeric score into a readable rating.
    rating = rate_spam_likelihood(score)

    # Display the final results for the user.
    display_results(score, rating, found)


if __name__ == "__main__":
    # Start the application from a single entry point.
    run_spam_scanner()
