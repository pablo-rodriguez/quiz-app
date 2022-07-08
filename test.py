def word(string):
  upper_count=0
  lower_count=0
  for i in string:
    if ord(i) >= 65 and ord(i) <= 90:
      upper_count += 1
    elif ord(i) >= 97 and ord(i) <= 122:
      lower_count += 1
  final="Number of uppercase letters = " + str(upper_count)
  final2="Number of lowercase letters = " + str(lower_count)
  return final+" "+" "+final2

result = word("My Name Is Pablo")
print(result)