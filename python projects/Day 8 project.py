alphabet = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#! Making a type of Caesar Cipher
#! Solution starts on line 100

# TODO 1) Create a function called "cipher()" that takes the inputs 'text' and 'amount' and 'done'

# TODO 2) For encode, shift each letter of the 'text' forward in the alphabet by 'amount'.

# TODO 3) For decode, shift each letter of the 'text' backwards in the alphabet by 'amount'.

# TODO 4) Find a way to deal with Random inputs from user.

# TODO 5) Have the Cipher program be capable of restarting and ending when you want, so you dont have to hit Run program.

















































































def cipher(text, amount, done):
    code_text = ""
    if done == "decode":
        amount *= -1

    for letter in text:       
        if letter not in alphabet:
            code_text += letter
        else:     
            code_position = alphabet.index(letter) + amount
            code_position %= len(alphabet)
            code_text += alphabet[code_position]
    print(f"This is the {done} message: {code_text}") 



# again = True

# while again:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
   
#     cipher(text=text, amount=shift, done=direction)
    
#     encrypt_again = input("Type 'yes' if you need to continue using cipher program. Otherwise, type 'no'.\n").lower()
    
#     if encrypt_again == "no":
#         again = False
#         print("See you again!")     