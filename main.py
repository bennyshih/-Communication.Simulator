from sender import text_to_binary
from receiver import binary_to_text
from channel import channel
from ber import calculate_ber

message =input("輸入文字:")

sent= text_to_binary(message)

print("Sender :")
print(sent)

error_rate =float (input("請輸入錯誤率(例如 0.1代表 10%):"))



received=channel(sent,error_rate)

print ("Channel:")
print(received)

error,ber=calculate_ber(sent,received)
print("Bit Error:",error)
print("BER:",ber)

total_bits=len(sent)
accuracy =(total_bits-error)/total_bits*100

print("===================")
print("Total Bits:",total_bits)
print("Error Bits:",error)
print("BER   :",ber)
print("Accuracry :",round(accuracy,2),"%")
print("====================")

result=binary_to_text(received)
 
print("Receiver :")
print(result)

print(" \n ========== Compare ============")
print("Original :"  , message)
print("Received :"  , result)


if message == result:
    print("Transmission :SUCCESS")
else:
      print("Transmission: FAILED")
print("===================================")