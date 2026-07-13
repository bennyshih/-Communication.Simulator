def calculate_ber(sent,received):
    error =0
    
    for s,r in zip(sent, received):
        if s!=r:
            error +=1
            
    ber =error/len(sent)
    return error ,ber