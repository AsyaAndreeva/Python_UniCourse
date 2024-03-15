import sys

input_list = [int(x) for x in sys.argv[1:]]

for index in range(len(input_list)):
  if input_list[index] in input_list[index+1:]:
    print("There are duplicates")
    break
else:
  print("There are no duplicates")