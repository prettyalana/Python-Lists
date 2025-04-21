sentence = "I like traveling to foreign countries"

empty_list = []

for letter in sentence :
    empty_list.append(letter)
    empty_list = list(reversed(empty_list))

print(empty_list)