# Reading the input data
d2_file = open("/content/drive/MyDrive/Study Materials/Data Science/Python/aoc/aoc_day2_input.txt", "r")
d2_data = d2_file.read().splitlines()
command = []
units = []
for i, line in enumerate(d2_data):
  command.append(line[:-2])
  units.append(int(line[-1:]))

# Part 1: solution
def detect_destination(cmd, unit):
  # Create two variable -
  horizontal = 0
  depth = 0
  for i in range(len(cmd)):
    if cmd[i] == 'forward':
      horizontal += unit[i]
    elif cmd[i] == 'up':
      depth -= unit[i]
    elif cmd[i] == 'down':
      depth += unit[i]
  return horizontal*depth

detect_destination(command, units)

# Part 2: Solution
def actual_destination(cmd, unit):
  # Create two variable -
  horizontal = 0
  depth = 0
  aim = 0
  for i in range(len(cmd)):
    if cmd[i] == 'forward':
      horizontal += unit[i]
      depth = (depth + (unit[i]*aim))
    elif cmd[i] == 'up':
      aim -= unit[i]
    elif cmd[i] == 'down':
      aim += unit[i]
  return horizontal*depth

actual_destination(command, units)
