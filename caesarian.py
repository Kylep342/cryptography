import sys

def caesarian(string, shift_by):
    shifted = []
    for char in string:
        if char.isalpha():
            if char.isupper():
                shifted.append(chr((ord(char) - ord('A') + shift_by) % 26 + ord('A')))
            else:
                shifted.append(chr((ord(char) - ord('a') + shift_by) % 26 + ord('a')))
        else:
            shifted.append(char)
    return ''.join(shifted)


if __name__ == '__main__':
    for shift in range(26):
        print(str(shift) + ': ' + caesarian(sys.argv[1], shift))
