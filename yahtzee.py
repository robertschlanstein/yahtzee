import os
import random

cross_out_char = 'X'

class Dice_cup:
    def __init__(self, num_of_dice = 5):
        self.num_of_dice = num_of_dice
        self.roll = []
        self.keep = []

    def roll_dice(self):
    #make self.roll a new list of rolled dice containing self.keep
        self.roll.clear()
        for d in self.keep:
            self.roll.append(d)
        while len(self.roll) < self.num_of_dice:
            self.roll.append(random.randint(1, 6))

    def keep_dice(self, keep_input):
    #create a list of dice from last roll to keep for next roll
        self.keep.clear()
        for d in self.roll:
            if d in keep_input:
                self.keep.append(d)
                keep_input.remove(d)

    def discard_kept_dice(self):
        self.keep.clear()

    def print_roll(self):
        for die in self.roll:
            print(die, end=' ')
        print()

class Score_card:
    def __init__(self, num_of_games = 6):
        self.num_of_games = num_of_games
        self.current_game_num = 0
        self.match_scores = []  #list of lists per game containing
                                #the individual scores per turn
        self.match_sums = []    #list of dicts per game containing
                                #score sums, totals, and the bonus
        for i in range(num_of_games):   #initialize match_scores and match_sums
            self.match_scores.append([0 for score in range(13)])
            self.match_sums.append({"upper_sum": 0,
                                    "upper_bonus": 0,
                                    "upper_total": 0,
                                    "lower_sum": 0,
                                    "game_total": 0})
        self.match_total = 0

    def add_score(self, comb_num, score, game_num):
    #add score for a single turn to match_scores
        if comb_num < 0 or comb_num > 12:
            print("Invalid combination number...")
            return False
        if score != cross_out_char and (score < 0 or score > 50):
            print("Impossible score...")
            return False
        if self.match_scores[game_num][comb_num] != 0:
            print("Combination already filled in...")
            return False

        self.match_scores[game_num][comb_num] = score
        return True

    #functions for calculating sums, totals, bonus
    def sum_scores(self, score_list):
        result = 0
        for n in score_list:
            if isinstance(n, int):
                result += n
        return result

    def calc_upper_sum(self, game_num):
        game_sums = self.match_sums[game_num]
        upper_section = self.match_scores[game_num][0:6]
        game_sums["upper_sum"] = self.sum_scores(upper_section)

    def calc_upper_bonus(self, game_num):
        game_sums = self.match_sums[game_num]
        if game_sums.get("upper_sum", 0) >= 63:
            game_sums["upper_bonus"] = 35
        else:
            game_sums["upper_bonus"] = 0

    def calc_upper_total(self, game_num):
        game_sums = self.match_sums[game_num]
        game_sums["upper_total"] = game_sums["upper_sum"] + game_sums["upper_bonus"]

    def calc_lower_sum(self, game_num):
        game_sums = self.match_sums[game_num]
        lower_section = self.match_scores[game_num][6:13]
        game_sums["lower_sum"] = self.sum_scores(lower_section)

    def calc_game_total(self, game_num):
        game_sums = self.match_sums[game_num]
        game_sums["game_total"] = game_sums["upper_total"] + game_sums["lower_sum"]

    def update_match_sums(self, game_num):
        self.calc_upper_sum(game_num)
        self.calc_upper_bonus(game_num)
        self.calc_upper_total(game_num)
        self.calc_lower_sum(game_num)
        self.calc_game_total(game_num)

    #printing function
    def print_score_card(self):
        comb_labels = ["1. Aces\t\t", "2. Twos\t\t", "3. Threes\t", "4. Fours\t",
                       "5. Fives\t", "6. Sixes\t", "7. 3 of a Kind\t",
                       "8. 4 of a Kind\t", "9. Full House\t", "10. Sm. Straight",
                       "11. Lg. Straight", "12. Yahtzee\t", "13. Chance\t"]

        print("Upper Section\t", end='')
        for i in range(self.num_of_games):
            print("    #{}".format(i + 1), end='\t')
        print()
        for i in range(6):
            print(comb_labels[i], end='')
            for game in self.match_scores:
                print("    {}".format(game[i]), end='\t')
            print()
        print("Sum\t\t", end='')
        for game in self.match_sums:
            print("    {}".format(game["upper_sum"]), end='\t')
        print()
        print("Bonus\t\t", end='')
        for game in self.match_sums:
            print("    {}".format(game["upper_bonus"]), end='\t')
        print()
        print("Upper Total\t", end='')
        for game in self.match_sums:
            print("    {}".format(game["upper_total"]), end='\t')
        print()
        print()
        print("Lower Section")
        for i in range(6, 13):
            print(comb_labels[i], end='')
            for game in self.match_scores:
                print("    {}".format(game[i]), end='\t')
            print()
        print("Sum\t\t", end='')
        for game in self.match_sums:
            print("    {}".format(game["lower_sum"]), end='\t')
        print()
        print("Upper Sum\t", end='')
        for game in self.match_sums:
            print("    {}".format(game["upper_total"]), end='\t')
        print()
        print("Game Total\t", end='')
        for game in self.match_sums:
            print("    {}".format(game["game_total"]), end='\t')
        print()

#game flow printing functions
def print_game(game_num, total_games):
    os.system("clear")
    sc.print_score_card()
    print()
    print("GAME {} of {}".format(game_num + 1, total_games))

def print_turn(game_num, total_games, turn_num, total_turns):
    print_game(game_num, total_games)
    print("TURN {} of {}".format(turn_num + 1, total_turns))

def print_roll(game_num, total_games, turn_num, total_turns,
               roll_num, total_rolls):
    print_turn(game_num, total_games, turn_num, total_turns)
    print("ROLL {} of {}".format(roll_num + 1, total_rolls))

#game flow input reading functions
def read_keep_dice():
    valid_dice = "123456"
    keep_list = []
    keep_string = input("Which dice do you keep?\n")
    for n in keep_string:
        if n in valid_dice:
            keep_list.append(int(n))
    return keep_list

def read_comb_input():
    input_string = input("Combination: ")
    comb_string = ""
    for n in input_string:
        if n.isdigit():
            comb_string += n
    return comb_string

def read_score_input():
    cross_out_input_chars = "xX"
    input_string = input("Score: ")
    score_string = ""
    if input_string != "" and input_string[0] in cross_out_input_chars:
        score_string = cross_out_char
        return score_string
    for n in input_string:
        if n.isdigit():
            score_string += n
    return score_string

def read_comb_score():
    print("Choose your combination number (1 - 13) and the score to enter.")
    
    #read combination field
    comb_input = read_comb_input()
    while comb_input == "":
        comb_input = read_comb_input()
    comb_num = int(comb_input) - 1

    #read score to enter
    score_input = read_score_input()
    while score_input == "":
        score_input = read_score_input()
    if score_input == cross_out_char:
        score = cross_out_char
    else:
        score = int(score_input)

    return comb_num, score

#game flow execution functions
def new_roll(current_game_num, current_turn_num, current_roll_num):
    #print match info
    print_roll(current_game_num, games_per_match,
               current_turn_num, turns_per_game,
               current_roll_num, rolls_per_turn)

    #execute roll
    dc.roll_dice()
    dc.print_roll()

    #let user keep dice for next roll
    dc.keep_dice(read_keep_dice())

def new_turn(current_game_num, current_turn_num):
    #print match info
    print_turn(current_game_num, games_per_match,
               current_turn_num, turns_per_game)

    #execute turn
    dc.discard_kept_dice()
    for roll_num in range(rolls_per_turn):
        new_roll(current_game_num, current_turn_num, roll_num)

    #let user fill score into chosen combination field
    comb_num, score = read_comb_score()
    while not sc.add_score(comb_num, score, current_game_num):
        comb_num, score = read_comb_score()
    sc.update_match_sums(current_game_num)

def new_game(current_game_num):
    #print match info
    print_game(current_game_num, games_per_match)

    #execute game
    for turn_num in range(turns_per_game):
        new_turn(current_game_num, turn_num)

#match constants
games_per_match = 6
turns_per_game = 13
rolls_per_turn = 3

#instantiate class objects
dc = Dice_cup()
sc = Score_card()

#the match itself
for game_num in range(games_per_match):
    new_game(game_num)
