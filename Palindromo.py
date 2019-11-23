# -*- coding: utf-8 -*-


def palindrome(word):
    reversed_letters = []

    for letter in word:
        reversed_letters.insert(0, letter)

    reversed_word = ''.join(reversed_letters)

    if reversed_word == word:
        return True
    return False


if __name__ == "__main__":
    word = input('Digite una palabra')

   result= palindrome(word)

   if result is True:
       print('{}si es un Palindromo'.format(word))
    else:
        print('{}no es un Palindromo'.format(word))
      
