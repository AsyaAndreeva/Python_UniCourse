import sys

input_list = [1, 2, 2]

for index, el in enumerate(input_list, start=1):
  if(el>input_list[index-1]):
        print("Not sorted")
        break
else:
    print("Sorted")