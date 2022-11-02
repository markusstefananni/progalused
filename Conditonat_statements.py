def are_equal(num_a: int, num_b: int) -> str:
    """
    Return "equal" if given numbers are equal and "not equal" if not.

    are_equal(12, 13) => "not equal"
    are_equal(5, 5) => "equal"

    :param num_a: first number
    :param num_b: second number

    :return: "equal" if given numbers are equal and "not equal" if they aren't.
    """
    # your code goes here
    if num_a == num_b:
        return"equal"
    else:
        return "not equal"

#print(are_equal(12, 13))
#print(are_equal(5, 5))

#2. Positive or negative

def positive_or_negative(num_a: int) -> str:
    """
    Return "negative", "positive" or "zero" depending on the given integer.

    positive_or_negative(12) => "positive"
    positive_or_negative(0) => "zero"
    positive_or_negative(-12) => "negative"

    :param num_a: given integer
    :return "negative", "positive" or "zero" depending on the given integer.
    """
    # your code goes here
    if num_a > 0:
        return "positive"
    elif num_a < 0:
        return"negative"
    else:
        return "zero"

print(positive_or_negative(12))
print(positive_or_negative(0))
print(positive_or_negative(-12))

#3. Is in string

def is_in_string(letter: str, word: str) -> bool:
    """
    If given letter is in given word return True, else return False.

    is_in_string("a", "car") => True
    is_in_string("b", "car") => False

    :param letter: given letter.
    :param word: given word.
    :return: boolean depending on if given letter is in given word.
    """
    # your code goes here
    if letter in word:
        return True
    else:
        return False

print(is_in_string("a", "car"))
print(is_in_string("b", "car"))

#4. Are same length

def are_same_length(str_a: str, str_b: str) -> bool:
    """
    Return True if given strings are of equal length or False if not.

    are_same_length("aa", "bb") => True
    are_same_length("a", "bbb") => False

    :param str_b: first string
    :param str_a: second string
    :return boolean True or False.
    """
    # your code goes here
    if len(str_a) == len(str_b):
        return True
    else:
        return False
print("----------")
print(are_same_length("aa", "bb"))
print(are_same_length("a", "bbb"))

#5. Is letter or digit

def is_letter_or_digit(symbol: str) -> str:
    """
    Return "letter" if given symbol is a letter, "digit" if given symbol is a digit and "other" if its neither.

    is_letter_or_digit("a") => "letter"
    is_letter_or_digit("1") => "digit"
    is_letter_or_digit("?") => "other"

    :param symbol: symbol
    :return "letter", "digit" or "other".
    """
    # your code goes here
    if symbol.isalpha() == True:
        return "letter"
    elif symbol.isdigit() == True:
        return "digit"
    else:
        return "other"


print("-------")
print(is_letter_or_digit("a"))
print(is_letter_or_digit("1"))
print(is_letter_or_digit("?"))

#6. last symbols

def are_last_symbols_same(str_a: str, str_b: str) -> bool:
    if str_a[-1] == str_b[-1]:
        return "true"
    else:
        return "false"
print("-----------")
print(are_last_symbols_same("tere", "ekfegaole"))
print(are_last_symbols_same("tere", "ekffff"))

print(" ")

#7. Hundred

def hundred(num_a: int) -> int:
    if num_a > int(100):
        return print(num_a % 100)
    if num_a < int(100):
        return print(100 - num_a)

hundred(110)
hundred(45)

