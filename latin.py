word = input("Enter a word: ")
vowel = ["a", "e", "i", "o", "u"]

def word_to_pig(word):
    if word[0] in vowel:
        new_word = word + "yay"
    else:
        new_word = word[1:] + word[0] + "ay"
    return(new_word)



def name_to_pig():
    full_name = input("Enter first and last name: ")
    split = full_name.split()
    first_name = split[0]
    last_name = split[1]
    print(word_to_pig(first_name) + " " + word_to_pig(last_name))


print(word_to_pig(word))
name_to_pig()
