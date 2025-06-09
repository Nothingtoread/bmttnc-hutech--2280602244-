import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.vigenere import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    """
    Main application window for the Vigenère cipher GUI.
    Handles encryption and decryption via API calls.
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Connect buttons to their respective methods
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self) -> None:
        """
        Encrypts the plaintext using the Vigenère cipher by calling the API.
        Performs error checking for empty fields.
        """
        plain_text = self.ui.txt_plain_text.toPlainText()
        key = self.ui.txt_key.text()
        if not plain_text or not key:
            self.show_error("Plaintext and key must not be empty.")
            return
        url = "http://127.0.0.1:5000/api/vigenere/encrypt"
        payload = {
            "plain_text": plain_text,
            "key": key
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setText(data.get("encrypted_text", ""))
                self.show_info("Encrypted Successfully")
            else:
                self.show_error("Error while calling API: {}".format(response.status_code))
        except requests.exceptions.RequestException as e:
            self.show_error(f"Error: {str(e)}")

    def call_api_decrypt(self) -> None:
        """
        Decrypts the ciphertext using the Vigenère cipher by calling the API.
        Performs error checking for empty fields.
        """
        cipher_text = self.ui.txt_cipher_text.toPlainText()
        key = self.ui.txt_key.text()
        if not cipher_text or not key:
            self.show_error("Ciphertext and key must not be empty.")
            return
        url = "http://127.0.0.1:5000/api/vigenere/decrypt"
        payload = {
            "cipher_text": cipher_text,
            "key": key
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setText(data.get("decrypted_text", ""))
                self.show_info("Decrypted Successfully")
            else:
                self.show_error("Error while calling API: {}".format(response.status_code))
        except requests.exceptions.RequestException as e:
            self.show_error(f"Error: {str(e)}")

    def show_error(self, message: str) -> None:
        """
        Displays an error message box.
        """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    def show_info(self, message: str) -> None:
        """
        Displays an information message box.
        """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Info")
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
