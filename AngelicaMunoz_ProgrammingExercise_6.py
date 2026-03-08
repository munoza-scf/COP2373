"""
Input Validator Program

Author: Angelica C. Munoz
Date: March 08, 2026

Program Description:
    This program asks the user to enter a phone number, a Social Security
    number, and a zip code. It uses regular expressions to determine whether
    each value is valid. The program then displays whether each entry is
    valid or invalid.
"""

import re


PHONE_PATTERN = r"^\(\d{3}\) \d{3}-\d{4}$"
SSN_PATTERN = r"^\d{3}-\d{2}-\d{4}$"
ZIP_PATTERN = r"^\d{5}(-\d{4})?$"


def validate_phone_number(phone_number: str) -> bool:
    """
    Brief description:
        Validate a phone number using a regular expression.

    Parameters:
        phone_number (str): The phone number entered by the user.

    Variables:
        match_found (bool): Indicates whether the phone number matches the
            required format.

    Logical steps:
        1. Compare the phone number to the required pattern.
        2. Return True if the pattern matches.
        3. Return False if the pattern does not match.

    Return:
        bool: True if valid, otherwise False.
    """
    # Check for the format (123) 456-7890.
    match_found = bool(re.fullmatch(PHONE_PATTERN, phone_number))
    return match_found


def validate_social_security_number(ssn: str) -> bool:
    """
    Brief description:
        Validate a Social Security number using a regular expression.

    Parameters:
        ssn (str): The Social Security number entered by the user.

    Variables:
        match_found (bool): Indicates whether the Social Security number
            matches the required format.

    Logical steps:
        1. Compare the Social Security number to the required pattern.
        2. Return True if the pattern matches.
        3. Return False if the pattern does not match.

    Return:
        bool: True if valid, otherwise False.
    """
    # Check for the format 123-45-6789.
    match_found = bool(re.fullmatch(SSN_PATTERN, ssn))
    return match_found


def validate_zip_code(zip_code: str) -> bool:
    """
    Brief description:
        Validate a zip code using a regular expression.

    Parameters:
        zip_code (str): The zip code entered by the user.

    Variables:
        match_found (bool): Indicates whether the zip code matches the
            required format.

    Logical steps:
        1. Compare the zip code to the required pattern.
        2. Accept either 5 digits or ZIP+4 format.
        3. Return True if the pattern matches.
        4. Return False if the pattern does not match.

    Return:
        bool: True if valid, otherwise False.
    """
    # Accept either 12345 or 12345-6789.
    match_found = bool(re.fullmatch(ZIP_PATTERN, zip_code))
    return match_found


def display_validation_result(label: str, value: str, is_valid: bool) -> None:
    """
    Brief description:
        Display whether a user entry is valid or invalid.

    Parameters:
        label (str): The name of the value being tested.
        value (str): The value entered by the user.
        is_valid (bool): The validation result for the value.

    Variables:
        status (str): The word valid or invalid.

    Logical steps:
        1. Determine the correct status message.
        2. Display the label, value, and validation result.

    Return:
        None
    """
    # Convert the Boolean result into a readable status message.
    if is_valid:
        status = "valid"
    else:
        status = "invalid"

    print(f"{label} '{value}' is {status}.")


def run_validation_program() -> None:
    """
    Brief description:
        Get input from the user, validate it, and display the results.

    Parameters:
        None

    Variables:
        phone_number (str): The phone number entered by the user.
        ssn (str): The Social Security number entered by the user.
        zip_code (str): The zip code entered by the user.
        phone_valid (bool): Validation result for the phone number.
        ssn_valid (bool): Validation result for the Social Security number.
        zip_valid (bool): Validation result for the zip code.

    Logical steps:
        1. Ask the user for a phone number.
        2. Ask the user for a Social Security number.
        3. Ask the user for a zip code.
        4. Validate each value with the appropriate function.
        5. Display whether each value is valid or invalid.

    Return:
        None
    """
    print("=== Input Validator Program ===")
    print("Phone number format: (123) 456-7890")
    print("Social Security number format: 123-45-6789")
    print("Zip code format: 12345 or 12345-6789\n")

    # Collect values from the user for validation.
    phone_number = input("Enter a phone number: ").strip()
    ssn = input("Enter a Social Security number: ").strip()
    zip_code = input("Enter a zip code: ").strip()

    # Validate each value with the correct regular expression.
    phone_valid = validate_phone_number(phone_number)
    ssn_valid = validate_social_security_number(ssn)
    zip_valid = validate_zip_code(zip_code)

    print("\n--- Validation Results ---")

    # Display the results in a consistent, readable format.
    display_validation_result("Phone number", phone_number, phone_valid)
    display_validation_result("Social Security number", ssn, ssn_valid)
    display_validation_result("Zip code", zip_code, zip_valid)


if __name__ == "__main__":
    # Start the program from a single entry point.
    run_validation_program()
