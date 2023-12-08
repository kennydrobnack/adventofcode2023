from day6 import multiply_ways_to_win_races, calculate_race_distance, find_possible_winning_races, read_lines_bad_kerning, part_two_results

def test_multiply_ways_to_win():
    sample_line1 = "Time:      7  15   30"
    sample_line2 = "Distance:  9  40  200"
    assert multiply_ways_to_win_races([sample_line1, sample_line2]) == 288, "Results should be 288"

def test_find_possible_winning_races():
    race_time = 7
    race_record = 9
    assert find_possible_winning_races(race_time, race_record) == 4

def test_race_distance():
    hold_time = 5
    total_time = 7
    assert calculate_race_distance(hold_time, total_time) == 10

def test_readlines_bad_kerning():
    line = "TIME: 12 34 56"
    assert read_lines_bad_kerning(line) == 123456

def test_part_two_results():
    sample_line1 = "Time:      7  15   30"
    sample_line2 = "Distance:  9  40  200"
    assert part_two_results([sample_line1, sample_line2]) == 71503