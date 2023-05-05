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

empty_list =' '.join([nato_name[char] for char in user_input if char in nato_name])
new = []
for i in empty_list:
    print(i)
#     if len(empty_list[i]) > 5:
#         new.append(empty_list[i])
# print(new)
print(empty_list)