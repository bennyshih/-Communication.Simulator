import random
def channel(binary,error_count):
    binary =list(binary)
    index_list=random.sample(range(len(binary)),error_count)
    for index in index_list:
        
        
     if binary[index] == "0":
        binary[index] ="1"
     else :
        binary[index] ="0"
        
        
        
    return "".join(binary)