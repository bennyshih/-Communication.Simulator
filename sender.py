def text_to_binary(text):
    binary =""
    
    for ch in text:
        binary += format(ord(ch),"08b")
        
        
    return binary