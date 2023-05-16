def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    positions = []

    for char in text.lower():
        if char.isalpha():
            positions.append(str(alphabet.index(char) + 1))

    return ' '.join(positions)
