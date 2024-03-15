import sys

def is_anagram(str1, str2):
  str1 = str1.replace(" ", "").lower()
  str2 = str2.replace(" ", "").lower()
  return sorted(str1) == sorted(str2)


if(is_anagram(sys.argv[1], sys.argv[2])):
  print("Is anagram")
else:
  print("Is not anagram")