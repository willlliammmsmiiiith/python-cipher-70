def encrypt(text, shift):
    res = ''
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')