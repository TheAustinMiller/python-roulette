import random
import time
# random.randrange(30)
# Print random num 0 through 29
probability = -1
bet = 0
money = 500
colors = ["green", "red", "black"]
bet_count = 0
b = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
r = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
g = [0, 37]

def print_statement(m, b):
  print("\nMoney: " + str(m))
  if b > 0:
    print("Bets: " + str(b))

def pick_color():
  color = input("Place a bet (Black, Red, or Green): ")
  ans = color.upper()
  probability = -1
  while probability == -1:
    if ans == "GREEN":
      probability = 0
    if ans == "RED":
      probability = 1
    if ans == "BLACK":
      probability = 2
    if probability == -1:
      print("Please enter a valid color")
      color = input("Place a bet (Black, Red, or Green): ")
      ans = color.upper()
  return probability

def check_game(money):
  if money <= 0:
    return True
  elif money >= 1000:
    return True
  else:
    return False

# 0 = green
# 1 = red
# 2 = black

def pick_bet(m):
  bet = input("How much money will you place on this color: ")
  bets = int(bet)
  while bets <= 0 or bets > m:
    print("Insufficient Funds! - Money: " + str(m))
    bet = input("How much money will you place on this color: ")
    bets = int(bet)
  return bets



print("Welcome to AJ's Roulette Game of Doubling Money")
print("Objective: double your money!")
print_statement(money, bet_count)
bet_count += 1
while not check_game(money):
  probability = pick_color()
  bet = pick_bet(money)
  money -= bet # subtract money for bet
  print("You are making a $" + str(bet) + " bet on " + colors[probability] + "\n")
  print("AND THE NUMBER IS")
  time.sleep(2)
  number = random.randrange(38)
  hit = False
  if number in b:
    print("BLACK " + str(number))
    if probability == 2:
      print("YOU HIT")
      money += bet * 2
    else:
      print("YOU DID NOT HIT")
  if number in g:
    if number == 37:
      print("GREEN 00")
    else:
      print("GREEN 0")
    if probability == 0:
      print("YOU HIT")
      money += bet * 10
    else:
      print("YOU DID NOT HIT")
  if number in r:
    print("RED " + str(number))
    if probability == 1:
      print("YOU HIT")
      money += bet * 2
    else:
      print("YOU DID NOT HIT")
  print_statement(money, bet_count)
  bet_count += 1

if money <= 0:
  print("\nBetter luck next time :(")
else:
  print("LETS GO - You doubled your money")
print("thanks for playing")
