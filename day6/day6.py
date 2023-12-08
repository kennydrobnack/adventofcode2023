import fileinput
from functools import reduce
import re


def find_possible_winning_races(race_time, record_distance):
    print(f"Calculating ways to win a race time {race_time} with record distance {record_distance}")
    winning_times = [hold_time for hold_time in range(1, record_distance - 1) 
                     if calculate_race_distance(hold_time, race_time) > record_distance]
    print(f"Winning times for race of time {race_time} previous record {record_distance}:\n {winning_times}")
    return len(winning_times)

def calculate_race_distance(button_hold_time, total_time):
    speed = button_hold_time
    distance = speed * (total_time - button_hold_time)
    return distance

def read_lines_bad_kerning(line):
    number = re.sub("\D", "", line)
    return int(number)

def read_lines(line):
    numbers = re.split("\s+", line)
    del numbers[0]
    numbers = [int(i) for i in numbers]
    return numbers

def multiply_ways_to_win_races(lines):
    times = read_lines(lines[0])
    distances = read_lines(lines[1])
    number_of_races = len(times)
    winning_combos_per_race = list(map(
        lambda r: find_possible_winning_races(times[r], distances[r]), 
        [r for r in range(0, number_of_races)])
    )
    results = reduce((lambda x, y: x * y), winning_combos_per_race)

    return results

def part_two_results(lines):
    time = read_lines_bad_kerning(lines[0])
    distance = read_lines_bad_kerning(lines[1])
    return find_possible_winning_races(time, distance)

def main():
    print("Running")
    my_file = open("./day6/day6_data.txt", "r") 
    data = my_file.read() 
    data_into_list = data.split("\n")
    result = multiply_ways_to_win_races(data_into_list)
    print(f"Final result: {result}")
    print("Starting part two:")
    results2 = part_two_results(data_into_list)
    print(f"Final part two results: {results2}")

if __name__ == '__main__':
    main()