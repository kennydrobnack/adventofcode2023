import re
#On each line, the calibration value can be found by combining the first digit and the last digit (in that order) 
#to form a single two-digit number.

def first_plus_last_digit(code):
    m = re.search(r"\d", code)
    rev = code[::-1]
    r = re.search(r"\d", rev)
    first_digit = code[m.start()]
    last_digit = rev[r.start()]
    return int(f"{first_digit}{last_digit}")

def add_first_and_last_digits_of_list(list_of_codes):
    sum = 0
    for code in list_of_codes:
        sum = sum + first_plus_last_digit(code)
    return sum

def main():
    test_codes = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet"
    ]
    result = add_first_and_last_digits_of_list(test_codes)
    print(f"Results: {result}")
    my_file = open("./day1/day1_data.txt", "r") 
    data = my_file.read() 
    data_into_list = data.split("\n")
    result = add_first_and_last_digits_of_list(data_into_list)
    print(f"Results: {result}")

if __name__ == "__main__":
    main()
