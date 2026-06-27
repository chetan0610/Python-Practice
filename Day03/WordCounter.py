def count_words(sentence):
    word_list = sentence.split()

    word_count = len(word_list)

    return word_count

user_sentence = input("Enter a sentence: ")

total_words = count_words(user_sentence)

print(f"The number of words in your sentence is: {total_words}")