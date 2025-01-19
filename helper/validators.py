def remove_whitespace_from_string(input_string: str) -> str:
    return input_string.replace(" ", "")

def password_length(password_string: str) -> int:
    """
    Returns the length of the password after removing white space from the 
    password string.

    Keyword arguments:
    password_string (str) -> the password string which needs to be analysed.    
    """
    clear_password = remove_whitespace_from_string(password_string)
    return len(clear_password)


def upper_case_char_exists(password_string: str) -> bool:
    """
    Checks if any upper case character exists, ASCII value between [65, 90] is present in the password. 

    Keyword arguments:
    password_string (str) -> the password string which needs to be analysed. 
    """
    clear_password = remove_whitespace_from_string(password_string)
    for item in clear_password:
        if ord(item) in range(65, 91):
            return True
    return False

    
def lower_case_char_exists(password_string: str) -> bool:
    """
    Checks if any lower case character exists, ASCII value between [97, 122] is present in the password.

    Keyword arguments:
    password_string (str) -> the password string which needs to be analysed. 
    """
    clear_password = remove_whitespace_from_string(password_string)
    for item in clear_password:
        if ord(item) in range(97, 123):
            return True
    return False


def numeric_char_exists(password_string: str) -> bool:
    """
    Checks if any numeric character exists, ASCII value between [48, 57] is present in the password.

    Keyword arguments:
    password_string (str) -> the password string which needs to be analysed. 
    """
    clear_password = remove_whitespace_from_string(password_string)
    for item in clear_password:
        if ord(item) in range(48, 58):
            return True
    return False

