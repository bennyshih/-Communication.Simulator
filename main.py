from sender import text_to_binary
from receiver import binary_to_text
from channel import channel
from ber import calculate_ber

message =input("輸入文字:")

sent= text_to_binary(message)

print("Sender :")
print(sent)

error_count =int (input("請問要翻幾個 bit:"))



received=channel(sent,error_count)

print ("Channel:")
print(received)

error,ber=calculate_ber(sent,received)
print("Bit Error:",error)
print("BER:",ber)

result=binary_to_text(received)
 
print("Receiver :")
print(result)