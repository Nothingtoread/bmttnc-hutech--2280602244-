from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher

app = Flask(__name__)

# Initialize cipher instances
caesar = CaesarCipher()
vigenere = VigenereCipher()
railfence = RailFenceCipher()
playfair = PlayfairCipher()

@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt_api():
    data = request.get_json()
    plain_text = data.get('plain_text', '')
    key = int(data.get('key', 0))
    encrypted_text = caesar.encrypt_text(plain_text, key)
    return jsonify({"encrypted_text": encrypted_text})

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt_api():
    data = request.get_json()
    cipher_text = data.get('cipher_text', '')
    key = int(data.get('key', 0))
    decrypted_text = caesar.decrypt_text(cipher_text, key)
    return jsonify({"decrypted_text": decrypted_text})

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt_api():
    data = request.get_json()
    plain_text = data.get('plain_text', '')
    key = data.get('key', '')
    encrypted_text = vigenere.vigenere_encrypt(plain_text, key)
    return jsonify({"encrypted_text": encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt_api():
    data = request.get_json()
    cipher_text = data.get('cipher_text', '')
    key = data.get('key', '')
    decrypted_text = vigenere.vigenere_decrypt(cipher_text, key)
    return jsonify({"decrypted_text": decrypted_text})

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt_api():
    data = request.get_json()
    plain_text = data.get('plain_text', '')
    key = int(data.get('key', 0))
    encrypted_text = railfence.rail_fence_encrypt(plain_text, key)
    return jsonify({"encrypted_text": encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt_api():
    data = request.get_json()
    cipher_text = data.get('cipher_text', '')
    key = int(data.get('key', 0))
    decrypted_text = railfence.rail_fence_decrypt(cipher_text, key)
    return jsonify({"decrypted_text": decrypted_text})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt_api():
    data = request.get_json()
    plain_text = data.get('plain_text', '')
    key = data.get('key', '')
    # Generate the Playfair matrix from the key
    playfair_matrix = playfair.create_playfair_matrix(key)
    # Pass the generated matrix to the encryption function
    encrypted_text = playfair.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({"encrypted_text": encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt_api():
    data = request.get_json()
    cipher_text = data.get('cipher_text', '')
    key = data.get('key', '')
    # Generate the Playfair matrix from the key
    playfair_matrix = playfair.create_playfair_matrix(key)
    # Pass the generated matrix to the decryption function
    decrypted_text = playfair.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({"decrypted_text": decrypted_text})

if __name__ == '__main__':
    app.run(debug=True)

