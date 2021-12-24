def encryption():
    text =  input("Enter Text to Encrypt: ")
    e_text = ""
    for char in text:
      if (char.isupper()):
        e_text += chr((ord(char) + 1-65) % 26 + 65)
      else:
        e_text += chr((ord(char) + 1 - 97) % 26 + 97)
    print("\nInput Plain Text: " + text)    
    print("\nCipher Text is: " + e_text)

def decryption():
    c_text = input("Enter Cipher Text to Decrypt: ")
    d_text = ""
    for char in c_text:
      if (char.isupper()):
        d_text += chr((ord(char) - 1 + 65) % 26 + 65)
      else:
        d_text += chr((ord(char) - 1 + 97) % 26 + 97)
    print("\nInput Cipher Text: " + c_text)
    print("\/Plain Text is: " + d_text)

print("Select Operation.")
print("Press 1 to Encrypt.")
print("Press 2 to Decrypt.")
choice = int(input("Enter Choice(1/2): "))
if choice == 1:
    encryption()
elif choice == 2:
    decryption()
else:
    print("Invalid Input!")
