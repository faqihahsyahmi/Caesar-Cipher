#import caesar cipher art logo from art.py
import art

print(art.logo)

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

#input from user
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: to encode: decrypt() func  takes 'original_text' and 'shift_amount' as inputs
# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")

# TODO-2: to decode: encrypt() func (decode the encoded message to readable text)
# def decrypt(original_text, shift_amount):
#     decode_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         decode_text += alphabet[shifted_position]
#     print(f"Here is the decoded result: {decode_text}")

# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  user input 'direction' variable to determine the func to use 

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


#encrypt(text, shift)
#decrypt(text, shift)
caesar(text, shift, direction)
