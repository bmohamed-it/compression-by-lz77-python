import ast
import os

WINDOW_SIZE = 10

def read_message(filename):
    message = []
    try:
        folder = os.path.dirname(__file__)
        filepath = os.path.join(folder, filename + ".txt")
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
    compressed = []
    offset, length, next_symbol = 0, 0, ''
    i = 0
    while i < len(message):
        best_match, best_j = 0, 0
        search_window = max(0, i - WINDOW_SIZE)
        for j in range(search_window, i):
            if (message[i] == message[j]):
                match_length = 1
                while (i + match_length < len(message) and j + match_length < len(message)):
                    if (message[i + match_length] == message[j + match_length]):
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
            if (i + best_match >= len(message)):
                next_symbol = ''
            else:
                next_symbol = message[i + best_match]
            tag = [offset, length, next_symbol]
            compressed.append(tag)
            i += best_match + 1
    return compressed

def write_compressed(compressed, newname):
    folder = os.path.dirname(__file__)
    filepath = os.path.join(folder, newname + ".txt")
    with open(filepath, 'w') as file:
        for tag in compressed:
            file.write(str(tag) + "\n")

def read_compressed(filename):
    compressed = []
    try:
        folder = os.path.dirname(__file__)
        filepath = os.path.join(folder, filename + ".txt")
        with open(filepath, 'r') as file:
            for line in file:
                tag = ast.literal_eval(line)
                compressed.append(tag)
        return compressed
    except FileNotFoundError:
        return None

def lz77_decompression(compressed):
    message = []
    for i in range(len(compressed)):
        if (compressed[i][0] == 0 and compressed[i][1] == 0):
            message.append(compressed[i][2])
        else:
            offset = compressed[i][0]
            length = compressed[i][1]
            start_index = len(message) - offset
            for j in range(start_index, start_index + length):
                message.append(message[j])
            message.append(compressed[i][2])
    return message

def write_message(message, newname):
    folder = os.path.dirname(__file__)
    filepath = os.path.join(folder, newname + ".txt")
    with open(filepath, 'w') as file:
        for item in message:
            file.write(str(item))

first_window = True
while True:
    if (first_window == True):
        print("\n=========================" \
        "\n======== Welcome ========"\
        "\n===== Compressy App =====" \
        "\n=========================")
        first_window = False
    print("\n----------------------"
    "\n|        MENU        |" \
    "\n----------------------" \
    "\n[1]. Compression" \
    "\n[2]. Decompression" \
    "\n[0]. Exit" \
    "\n----------------------")
    choice = int(input("Please enter your choice: "))
    if (choice == 1):
        filename = input("Please enter file name: ")
        message = read_message(filename)
        if message is None:
            print("File not found, please enter a valid file name")
        else:
            compressed = lz77_compression(message)
            newname = input("Enter new file name: ")
            write_compressed(compressed, newname)
            print("File created successfully!")
    elif (choice == 2):
        
        filename = input("Please enter file name: ")
        compressed = read_compressed(filename)
        if compressed is None:
            print("File not found please enter a valid file name.")
        else:
            message = lz77_decompression(compressed)
            newname = input("Enter new file name: ")
            write_message(message, newname)
            print("File created successfully!")
    elif (choice == 0): 
        break
    else:
        print("Invalid choice please try again.")
