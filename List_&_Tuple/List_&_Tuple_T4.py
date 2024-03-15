import sys

input_list = [int(x) for x in sys.argv[1:]]

result_list = []
for index in range(len(input_list)):
    if input_list[index] not in input_list[index+1:]:
        result_list.append(input_list[index])


result_list.sort()
for item in result_list:
  print(item)