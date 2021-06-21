# Towers of Hanoi
# is an ancient mathematical puzzle that starts off with three stacks and many disks
# the objective of the game is to move the stack of disks from the leftmost stack to the rightmost stack
# The game follows three rules
# 1. Only one disk can be moved at a time
# 2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
# 3. No disk may be placed on top of a smaller disk

from stack import Stack

print("\nLet's play Towers of Hanoi!")

# Create stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks += [left_stack, middle_stack, right_stack]

# Set up the game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))

for disk in range(num_disks, 0, -1):
  left_stack.push(disk)

num_optimal_moves = 2 ** num_disks -1
print(f"The fastest you can solve this game is in {num_optimal_moves} moves")
# Get user input
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  while choices:
    for choice in range(len(stacks)):
      name = stacks[choice].get_name()
      letter = choices[choice]
      print(f"Enter {letter} for {name}")
    user_input = input("").upper()
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]
    print("Invalid choice! Please enter a provided choice!")

# Play the game
num_user_moves = 0
# game ends when right stack is full
while right_stack.get_size() != num_disks:
  print("\n\n\n...Current Stacks...")
  for stack in stacks:
    stack.print_items()
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    if from_stack.get_size() == 0:
      print("\n\nCan't move from an empty stack, try again")
    elif to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\nCan't place a bigger disk on a smaller disk. Try again")
print(f"You completed the game in {num_user_moves} moves, and the optimal number of moves is {num_optimal_moves}")


