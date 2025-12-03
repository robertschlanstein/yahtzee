import os
import random

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
            return
        if score < 0 or score > 50:
            print("Impossible score...")
            return
        if self.match_scores[game_num][comb_num] != 0:
            print("Combination already filled in...")
            return
        self.match_scores[game_num][comb_num] = score

    #functions for calculating sums, totals, bonus
    def calc_upper_sum(self, game_num):
        game_sums = self.match_sums[game_num]
        upper_section = self.match_scores[game_num][0:6]
        game_sums["upper_sum"] = sum(upper_section)

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
        game_sums["lower_sum"] = sum(lower_section)

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
        print("Upper Section\t", end='')
        for i in range(self.num_of_games):
            print("    #{}".format(i + 1), end='\t')
        print()
        print("1. Aces\t\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[0]), end='\t')
        print()
        print("2. Twos\t\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[1]), end='\t')
        print()
        print("3. Threes\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[2]), end='\t')
        print()
        print("4. Fours\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[3]), end='\t')
        print()
        print("5. Fives\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[4]), end='\t')
        print()
        print("6. Sixes\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[5]), end='\t')
        print()
        print("Sum\t\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[5]), end='\t')
        print()
        print("Bonus\t\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[5]), end='\t')
        print()
        print("Upper\t\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[5]), end='\t')
        print()
        print()
        print("Lower Section")
        print("7. 3 of a Kind\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[6]), end='\t')
        print()
        print("8. 4 of a Kind\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[7]), end='\t')
        print()
        print("9. Full House\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[8]), end='\t')
        print()
        print("10. Sm. Straight", end='')
        for game in self.match_scores:
            print("    {}".format(game[9]), end='\t')
        print()
        print("11. Lg. Straight", end='')
        for game in self.match_scores:
            print("    {}".format(game[10]), end='\t')
        print()
        print("12. Yahtzee\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[11]), end='\t')
        print()
        print("13. Chance\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[12]), end='\t')
        print()
        print("Lower\t\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[5]), end='\t')
        print()
        print("Upper\t\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[5]), end='\t')
        print()
        print("Total\t\t", end='')
        for game in self.match_scores:
            print("    {}".format(game[5]), end='\t')
        print()

#game flow printing functions
def print_game_num(game_num, total_games):
    print("GAME {} of {}".format(game_num + 1, total_games))

def print_turn_num(turn_num, total_turns):
    print("TURN {} of {}".format(turn_num + 1, total_turns))

def print_roll_num(roll_num, total_rolls):
    print("ROLL {} of {}".format(roll_num + 1, total_rolls))

#game flow reading functions
def read_keep_dice():
    valid_dice = "123456"
    keep_list = []
    keep_string = input("Which dice do you keep?\n")
    for n in keep_string:
        if n in valid_dice:
            keep_list.append(int(n))
    return keep_list

def read_comb_score():
    print("Choose your combination number (1 - 13) and the score to enter.")
    
    input_string = input("Combination: ")
    comb_string = ""
    for n in input_string:
        if n in "1234567890":
            comb_string += n
    comb_num = int(comb_string) - 1

    input_string = input("Score: ")
    score_string = ""
    for n in input_string:
        if n in "1234567890":
            score_string += n
    score = int(score_string)

    return comb_num, score

def new_roll(current_game_num, current_turn_num, current_roll_num):
    os.system("clear")
    sc.print_score_card()
    print()
    print_game_num(current_game_num, num_of_total_games)
    print_turn_num(current_turn_num, 13)
    print_roll_num(current_roll_num, 3)
    dc.roll_dice()
    dc.print_roll()

    dc.keep_dice(read_keep_dice())

def new_turn(current_game_num, current_turn_num):
    os.system("clear")
    sc.print_score_card()
    print()
    print_game_num(current_game_num, num_of_total_games)
    print_turn_num(current_turn_num, 13)
    dc.discard_kept_dice()
    for n in range(3):
        new_roll(current_game_num, current_turn_num, n)
    comb_num, score = read_comb_score()
    sc.add_score(comb_num, score, current_game_num)
    sc.update_match_sums(current_game_num)
    print(sc.match_scores)
    print(sc.match_sums)
    input()

def new_game(current_game_num):
    os.system("clear")
    sc.print_score_card()
    print()
    print_game_num(current_game_num, num_of_total_games)
    for n in range(13):
        new_turn(current_game_num, n)

#main program
num_of_total_games = 6
current_game_num = 0

dc = Dice_cup()
sc = Score_card()

new_game(current_game_num)
