def ceaser_cipher(letter, key):
    letter = letter.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter in alphabet:
        letter_index = (alphabet.find(letter) + key) % len(alphabet)
        return alphabet[letter_index]
    else:
        return letter

def vigenere_cipher(message, keyword):
    result = []
    keyword_length = len(keyword)
    keyword = keyword.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i, letter in enumerate(message):
        key_char = keyword[i % keyword_length]
        key_num = alphabet.find(key_char)
        result.append(ceaser_cipher(letter, key_num))
    return ''.join(result)

print(vigenere_cipher("ATTACKATDAWN", "LEMON"))
