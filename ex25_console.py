# python
import ex25
sentence= "All good things come to those who wait."
words=ex25.break_words(sentence)
print(words)
sort_words=ex25.sort_words(words)

print(sort_words)
print(ex25.sort_sentence(sentence))
print(ex25.print_first_words(words))
print(ex25.print_last_word(words))

print(ex25.print_first_words(sort_words))
print(ex25.print_last_word(sort_words))

print(ex25.print_first_and_last(sentence))
print(ex25.print_first_and_last_sorted(sentence))
