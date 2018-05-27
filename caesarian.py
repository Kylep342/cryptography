#!/usr/bin/env python
import sys


def caesarian(shift_by, word_list):
    shifted_args = []
    for string in word_list:
        shifted = []
        for char in string:
            if char.isalpha():
                if char.isupper():
                    shifted.append(chr((ord(char) - ord('A') + shift_by) % 26 + ord('A')))
                else:
                    shifted.append(chr((ord(char) - ord('a') + shift_by) % 26 + ord('a')))
        else:
            shifted.append(char)
        shifted_word = ''.join(shifted)
        shifted_args.append(shifted_word)
    return shifted_args


if __name__ == '__main__':
    for shift in range(26):
        print(str(shift) + ': ' + ' '.join(caesarian(shift, sys.argv[1:])))
