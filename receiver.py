def binary_to_text(binary):

    text = ""

    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        text += chr(int(byte, 2))

    return text