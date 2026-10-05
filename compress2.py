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
    offset = 0
    length = 0
    next_symbol = ''
    compressed = []
    i = 0
    while i < len(message):
        best_match = 0
        best_j = 0
        for j in range(i):
            if (message[i] == message[j]):
                match_length = 1
                while i + match_length < len(message) and j + match_length < len(message):
                    if(message[i + match_length] == message[j + match_length]):
                        match_length += 1
                    else:
                        break
                if match_length > best_match or ( match_length == best_match and j > best_j ):
                    best_match = match_length
                    best_j = j
        if (best_match == 0):
            compressed.append([0, 0, message[i]])
            i += 1
        else:
            offset = i - best_j
            length = best_match
            if(i + best_match >= len(message)):
                next_symbol = ''
            else:
                next_symbol = message[i + best_match]
            tag = [offset, length, next_symbol]
            compressed.append(tag)
            i += best_match + 1
    return compressed

def write_compressed(compressed, name):
    folder = os.path.dirname(__file__)
    filepath = os.path.join(folder, name)
    with open(filepath, 'w') as file:
        for tag in compressed:
            file.write(str(tag) + "\n")

first_window = True
while True:
    if (first_window == True):
        print("\n=========================" \
        "\n======== Welcome ========"\
        "\n===== Compressy App =====" \
        "\n=========================")
        first_window = False
    print("\n----------------"
    "\n|     Menu     |" \
    "\n----------------" \
    "\n[1]: Compression" \
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
            print("File created successfully!")
    elif (choice == 2):
        filename = input("Please enter file name (include extension): ")
        # compressed = read_compressed(filename)
        # message = lz77_decompression(compressed)
        # write_message(message)
    elif (choice == 0): 
        break
    else:
        print("Invalid choice, please try again")
