from alphabet import nato_phonetic

nato_name = nato_phonetic()

print(nato_name['A'])

user_input = input("Write your massage: ").upper()

# empty_list = []
#
# for char in user_input:
#     if char in nato_name:
#         empty_list.append(nato_name[char])
#
# output = ' '.join(empty_list)
# print(output)

empty_list = [nato_name[char] for char in user_input if char in nato_name]

print(empty_list)