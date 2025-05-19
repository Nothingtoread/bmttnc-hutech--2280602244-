class PlayfairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.replace('J', 'I')
        key = key.upper()
        key_set = ''
        for letter in key:
            if letter not in key_set and letter.isalpha():
                key_set += letter
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        remaining_letters = [letter for letter in alphabet if letter not in key_set]
        matrix = list(key_set)
        for letter in remaining_letters:
            matrix.append(letter)
        playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        return None, None

    def playfair_encrypt(self, plain_text, matrix):
        # Chuyển văn bản về chuẩn
        plain_text = plain_text.replace('J', 'I')
        plain_text = plain_text.replace(' ', '')
        plain_text = plain_text.upper()
        encrypted_text = ''
        # Xử lý cặp ký tự
        i = 0
        while i < len(plain_text):
            pair = plain_text[i:i+2]
            if len(pair) < 2:
                pair += 'X'
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]
            i += 2
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        decrypted_text = ''
        i = 0
        while i < len(cipher_text):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]
            i += 2
        return decrypted_text