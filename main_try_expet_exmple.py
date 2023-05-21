from alphabet import nato_phonetic

nato_name = nato_phonetic()


def generate_phonetic():
    user = input("Write a message: ").upper()

    try:
        output_list = ' '.join([nato_name[num] for num in user])
    except KeyError:
        print("Sorry, You put a number,but here need a word or a sentence")
    else:
        print(output_list)


generate_phonetic()
