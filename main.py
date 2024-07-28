vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

def find_first_vowel(input_string):
    vowels = 'aeiouAEIOU'  # Both lowercase and uppercase vowels
    for i, char in enumerate(input_string):
        if char in vowels:
            return i  # Return the index of the first vowel found
    return -1  # Return -1 if no vowel is found

def to_piglatin_word(word):
    output = ""
    first_vowel_index = find_first_vowel(word)
    if word[0] in consonants:
        if first_vowel_index == -1:
            output = word[1:len(word)] + word[0] + "ay"
        else:
            output = word[first_vowel_index:len(word)] + word[0:first_vowel_index] + "ay"
    else:
        output = word + "way"

    return output

def to_pigLatin_sentence(sentence):
    word_array = sentence.lower().split()
    output = []
    for word in word_array:
        output.append(to_piglatin_word(word))
    return " ".join(output)

while True:
    statement = input("Enter: ")
    print(to_pigLatin_sentence(statement))
