from helper import (numeric_char_exists,
                    lower_case_char_exists,
                    password_length, 
                    upper_case_char_exists)

def get_password_validation_result(password: str) -> dict:
    pass_length = password_length(password_string=password)
    numeric = numeric_char_exists(password_string=password)
    lower_case = lower_case_char_exists(password_string=password)
    upper_case = upper_case_char_exists(password_string=password)
    response = {
                "password_length": pass_length,
                "numeric_exists": numeric,
                "lower_case": lower_case,
                "upper_case": upper_case
                }
    return response

def main():
    password_input = input("Enter the password\n")
    result = get_password_validation_result(password=password_input)
    print(result)

if __name__ == "__main__":
    main()

