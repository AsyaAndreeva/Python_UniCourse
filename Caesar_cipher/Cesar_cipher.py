def ceaser_cipher(message, key):
    result = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in message:
        if letter.upper() in alphabet:
            if letter.islower():
                letter_index = (alphabet.find(letter.upper()) + key) % len(alphabet)
                result.append(alphabet[letter_index].lower())
            else:
                letter_index = (alphabet.find(letter.upper()) + key) % len(alphabet)
                result.append(alphabet[letter_index])
        else:
            result.append(letter)
    return ''.join(result)

print(ceaser_cipher("abczGh", 1))
