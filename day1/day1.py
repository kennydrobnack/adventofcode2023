import re
#On each line, the calibration value can be found by combining the first digit and the last digit (in that order) 
#to form a single two-digit number.

def first_plus_last_digit(code):
    matches = re.findall(r"\d", code)
    first_digit = matches[0]
    last_digit = matches[-1]
    return int(f"{first_digit}{last_digit}")

def part_two_first_plus_last_digit(code):
    pattern = "one|two|three|four|five|six|seven|eight|nine"
    matches = re.findall(f"{pattern}|\d", code)
    first_digit = written_number_to_digit(matches[0])
    rev_pattern = f"{pattern[::-1]}|\d"
    rev_matches = re.findall(rev_pattern, code[::-1])
    try:
        last_digit = rev_matches[0]
        if (len(last_digit) > 1):
            last_digit = written_number_to_digit(last_digit[::-1])
    except Exception as ex:
        print(f"Failed to find last digit of {code} with error {ex}")
    return int(f"{first_digit}{last_digit}")    

def written_number_to_digit(code):
    p = re.compile('one')
    code = p.sub("1", code)
    p = re.compile('two')
    code = p.sub("2", code)
    p = re.compile('three')
    code = p.sub("3", code)
    p = re.compile('four')
    code = p.sub("4", code)
    p = re.compile('five')
    code = p.sub("5", code)
    p = re.compile('six')
    code = p.sub("6", code)
    p = re.compile('seven')
    code = p.sub("7", code)
    p = re.compile('eight')
    code = p.sub("8", code)
    p = re.compile('nine')
    code = p.sub("9", code)
    return code

def add_first_and_last_digits_of_list(list_of_codes):
    sum = 0
    for code in list_of_codes:
        updated_code = written_number_to_digit(code)
        sum = sum + first_plus_last_digit(updated_code)
    return sum

def part_two_add_first_and_last_digits_of_list(list_of_codes):
    sum = 0
    try:
        for code in list_of_codes:
            sum = sum + part_two_first_plus_last_digit(code)
    except:
        print("Something went wrong!")
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
    part_two_test_codes = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen"
    ]
    result = part_two_add_first_and_last_digits_of_list(part_two_test_codes)
    print(f"Results: {result}")
    result = part_two_add_first_and_last_digits_of_list(data_into_list)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
