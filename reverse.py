word = input("Input a word to reverse: ")

for i in range(len(word) - 1, -1, -1):
  print(word[i], end="")
print("\n.")

