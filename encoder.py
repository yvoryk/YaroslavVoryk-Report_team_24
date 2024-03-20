# Yaroslav Voryk

def encode_password(password):
    encoded = ""
    for char in password:
        encoded += str((int(char) + 3) % 10)
    return encoded


def decode_password(encoded_password):
    decoded = ""
    for char in encoded_password:
        decoded += str((int(char) - 3) % 10)
    return decoded



def main():
    encoded_password = ""
    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        option = input("Please enter an option: ")
        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode_password(password)
            print("Your password has been encoded and stored!")
        if option == "2":
            print(f"The encoded password is {encoded_password}, and the original password is {decode_password(encoded_password)}.")
        elif option == "3":
            break


if __name__ == "__main__":
    main()
