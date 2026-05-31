import json

#made by Vedant Sonawane
def encode_message(message, json_filepath="data.json"):
    try:
        with open(json_filepath, "r") as json_file:
            letters_map = json.load(json_file)
    except FileNotFoundError:
        print(f"Error: The file {json_filepath} was not found.")
        print("Please run your file creation script first.")
        return None

    encoded_chars = []


    for char in message:

        lowercase_char = char.lower()


        if lowercase_char in letters_map:
            encoded_chars.append(letters_map[lowercase_char])

        elif char == " ":
            continue

    return " ".join(encoded_chars)


def decode_message(encoded_text, json_filepath="data.json"):
    try:
        with open(json_filepath, "r") as json_file:
            letters_map = json.load(json_file)
    except FileNotFoundError:
        print(f"Error: The file {json_filepath} was not found.")

        return None


    reverse_map = {value: key for key, value in letters_map.items()}

    decoded_chars = []

    encoded_bits = encoded_text.split()

    for bit_sequence in encoded_bits:
        if bit_sequence in reverse_map:
            decoded_chars.append(reverse_map[bit_sequence])
        else:
            decoded_chars.append("?")

    return "".join(decoded_chars)


if __name__ == "__main__":
    while True:
        print("\n=== Binary Cipher Tool ===")
        print("1. Encode text to bits")
        print("2. Decode bits to text")
        print("3. Exit")

        choice = input("Please select an option (1-3): ").strip()

        if choice == "1":
            secret_message = input("\nEnter the secret message to ENCODE: ")
            encoded_result = encode_message(secret_message)
            if encoded_result:
                print(f"Encoded Bits: {encoded_result}")

        elif choice == "2":
            bit_message = input("\nEnter the bit sequences to DECODE: ")
            decoded_result = decode_message(bit_message)
            if decoded_result is not None:
                print(f"Decoded Text: {decoded_result}")

        elif choice == "3":
            print("\nExiting program. Goodbye!")
            break

        elif choice == "how made this":
            print("010101 000100 000011 000000 001101 010011 010010 001110 001101 000000 010110 000000 001101 000100")


        else:
            print("\nInvalid option. Please type 1, 2, or 3.")
