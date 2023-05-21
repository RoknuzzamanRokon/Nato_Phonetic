from alphabet import nato_phonetic

nato_name = nato_phonetic()

user_input = input("Write your massage: ").upper()

# empty_list = []
empty_list = [nato_name[char] for char in user_input if char in nato_name]

# for char in user_input:
#     if char in nato_name:
#         empty_list.append(nato_name[char])

output = ' '.join(empty_list)
print(output)

big_word = []
big_word = ' '.join([x.upper() for x in empty_list if len(x) > 5])

# for lan in empty_list:
#     if len(lan) > 5:
#         big_word.append(lan)

print("\n")
print(big_word)
