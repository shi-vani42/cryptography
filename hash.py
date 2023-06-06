import random
def custom_hash(message):
    random.seed(message) 
    hash_value = random.randint(0, 2**16-1)
    return hash_value

message=input("Enter the message:")
hash_value=custom_hash(message)

print("Original Message:", message) 
print("Hash value:", hash_value)

received_message=input("Enter the received message: ")
received_hash_value=custom_hash(received_message) 

print("Received Message:", received_message)
print("Received Hash value:", received_hash_value)

if received_hash_value == hash_value: 
    print("Integrity: The message has not been modified.")
else:
    print("Integrity: The message has been modified.")
