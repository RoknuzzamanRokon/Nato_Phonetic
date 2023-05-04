from alphabet import nato_phonetic

nato_name = nato_phonetic()

print(nato_name['A'])

user_input = input("Write your massage: ").upper()

empty_list = []

for char in user_input:
    if char in nato_name:
        empty_list.append(nato_name[char])


print(empty_list)
