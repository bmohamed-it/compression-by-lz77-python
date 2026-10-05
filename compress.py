import os

def read_message(filename):
    message = []
    try:
        folder = os.path.dirname(__file__)
        filepath = os.path.join(folder, filename)
        with open(filepath, "r") as file:
            while True:
                char = file.read(1)
                if (char == ""):
                    break
                else:
                    message.append(char)
        return message
    except FileNotFoundError:
        return None

def lz77_compression(message):
    test = "test"

def write_compressed(compressed, name):
    test = "test"

first_window = True
while True:
    if (first_window == True):
        print("=========================" \
        "\n======== Welcome ========"\
        "\n===== Compressy App =====" \
        "\n=========================")
        first_window = False
    print("[1]: Compression" \
    "\n[2]: Decompression" \
    "\n[0]: Exit")
    choice = int(input("Please enter your chioce: "))
    if (choice == 1):
        filename = input("Please enter file name (include extension): ")
        message = read_message(filename)
        if message is None:
            print("File not found, please enter a valid file name")
        else:
            compressed = lz77_compression(message)
            name = input("Enter new file name (include extension): ")
            write_compressed(compressed, name)
    elif (choice == 2):
        filename = input("Please enter file name (include extension): ")
        # compressed = read_compressed(filename)
        # message = lz77_decompression(compressed)
        # write_message(message)
    elif (choice == 0): 
        break
    else:
        print("Invalid choice, please try again!")