import random

print()

num_rolls = int(input("Enter the number of rolls: "))

rolls = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

for i in range(num_rolls):
  die1 = random.randint(1, 6)
  die2 = random.randint(1, 6)
  rolls[die1 + die2] += 1

print()

for roll, count in rolls.items():
  decimal = count / num_rolls
  percent = decimal * 100

  if roll < 10:
    print(f" {roll}: {percent:.2f}%")
  else:
    print(f"{roll}: {percent:.2f}%")
