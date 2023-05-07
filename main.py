from alphabet import nato_phonetic

nato_name = nato_phonetic()


user_input = input("Write your massage: ").upper()

empty_list = []

for char in user_input:
    if char in nato_name:
        empty_list.append(nato_name[char])

output = ' '.join(empty_list)
big_word = []
for lan in empty_list:
    if lan(lan) > 5:
        big_word.append(lan)
print(empty_list)
print("\n")
print(big_word)