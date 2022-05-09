# Aidan Henry
# this program offers encoding and decoding of a given message
encode_mode = "E"
decode_mode = "D"


def key_match(cipher, char, mode):
    if mode == encode_mode:
        if char in cipher:
            return cipher.get(char)
        return char
    elif mode == decode_mode:
        for key in cipher:
            if char in cipher.get(key):
                return key
        return char


def encode(message, cipher_key):
    encrypted_message = ""
    for char in message:
        encrypted_message += key_match(cipher_key, char, encode_mode)
        # print(char + " encrypted: " + encrypted_char)
    print(encrypted_message)


def decode(message, cipher_key):
    decrypted_message = ""
    for char in message:
        decrypted_message += key_match(cipher_key, char, decode_mode)
    print(decrypted_message)


def main():
    cipher_key = {
        "a": "0",
        "b": "1",
        "c": "2",
        "d": "3",
        "e": "4",
        "f": "5",
        "g": "6",
        "h": "7",
        "i": "8",
        "j": "9",
        "k": "!",
        "l": "@",
        "m": "#",
        "n": "$",
        "o": "%",
        "p": "^",
        "q": "&",
        "r": "*",
        "s": "(",
        "t": ")",
        "u": "-",
        "v": "+",
        "w": "<",
        "x": ">",
        "y": "?",
        "z": "="
    }
    while True:
        print("Welcome to the Secret Message Encoder/Decoder")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit\n")
        try:
            message_select = int(input("What would you like to do? "))
            if message_select == 1:
                encode_message = input("Enter a message to encode: ")
                encode(encode_message, cipher_key)
            elif message_select == 2:
                decode_message = input("Enter a message to decode: ")
                decode(decode_message, cipher_key)
            elif message_select == 3:
                break
            else:
                print(str(message_select) + " is not a valid choice")
        except ValueError:
            print("Please enter a number between 1 and 3.")


main()
