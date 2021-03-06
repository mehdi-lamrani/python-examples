# test_capitalize.py

def capital_case(str):
    return str.upper()

def upper_case(str):
    return str.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

def test_upper_case():
    assert upper_case('semaphore') == 'SEMAPHORE'


# Just run pytest on the terminal at the root path of the file
# Add pytest to your environment if not installed yet :
# pip install pytest