import re  # Used for pattern matching with the regular expressions


def validate_phone(phone):
    #validate a phone number in the format (xxx) xxx-xxxx
    pattern = r'^\(\d{3}\)\s\d{3}-\d{4}$'  # Matches (123) 456-7890, the "d" is used for number of digits. So 3-3-4
    return bool(re.match(pattern, phone))


def validate_ssn(ssn):
    #Validate a Social Security Number in the format xxx-xx-xxxx
    pattern = r'^\d{3}-\d{2}-\d{4}$'  # Matches 123-45-6789, the "d" is used for number of digits. So 3-2-4
    return bool(re.match(pattern, ssn))


def validate_zip(zip_code):
    #Validate a ZIP code in the format xxxxx-xxxx
    pattern = r'^\d{5}-\d{4}$'  # Matches 12345-6789, the "d" is used for number of digits. So 5-4
    #Returns the match and zip code so it can be printed.
    return bool(re.match(pattern, zip_code))


def main():
    #"Get user input and display if each entry is valid
    phone = input("Enter a phone number ((xxx) xxx-xxxx): ")
    ssn = input("Enter a Social Security Number (xxx-xx-xxxx): ")
    zip_code = input("Enter a ZIP code (xxxxx-xxxx): ")

    #prints the validation results ie true or false
    print("\nValidation Results:")
    print(f"Phone number valid: {validate_phone(phone)}")
    print(f"SSN valid: {validate_ssn(ssn)}")
    print(f"ZIP code valid: {validate_zip(zip_code)}")

main()