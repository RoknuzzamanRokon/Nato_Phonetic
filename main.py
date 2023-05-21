from alphabet import nato_phonetic

nato_name = nato_phonetic()

print(nato_name['A'])

user_input = input("Write your massage: ").upper()


empty_list =' '.join([nato_name[char] for char in user_input if char in nato_name])
new = []

print(empty_list)
