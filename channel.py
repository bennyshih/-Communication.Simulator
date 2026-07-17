import random
def channel(binary,error_rate):
    binary =list(binary)
    
    for i in range(len(binary)):
       if random.random() < error_rate:
        
        
        if binary[i] == "0":
           binary[i] ="1"
        else :
            binary[i] ="0"
        
        
        
    return "".join(binary)