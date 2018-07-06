alphabet = "abcdefghijklmnopqrstuvwxyz"
partialOne = ""
partialTwo = ""
newAlphabet = ""

on = True

while on:

    #Gets message and key to shift by
    message = input("Enter a message ").lower()
    key = int(input("Shift amount "))

    #Makes sure the shift does not go over 26
    if key > 26:
        print("ERROR! SHIFT CANNOT EXCED 26")
    elif key < -26:
        print("ERROR! SHIFT CANNOT GO UNDER -26")
    elif key > 0:
        #Moves a part of the alphabet to the front or back
        partialOne = alphabet[:key]
        partialTwo = alphabet[key:]
        newAlphabet = partialTwo + partialOne
    elif key < 0:
        partialOne = alphabet[:(26 + key)]
        partialTwo = alphabet[(26 + key):]
        newAlphabet = partialTwo + partialOne
    elif key == 0:
        newAlphabet = alphabet

    newMessage = ""

     #Encrypts message with the shift
    for i in range(0, len(message)):
        index = alphabet.find(message[i])
 
        if index < 0:
            newMessage += message[i]
        else:
            newMessage += newAlphabet[index]

    print(newMessage)
