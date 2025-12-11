alphabet = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#! Making a type of Caesar Cipher

# TODO 1) Create a function called "encrypt()" that takes 'text' and 'amount' as 2 inputs

# TODO 2) Inside the "encrypt()" function, shift each letter of the 'text' forward in the alphabet by
#?          the 'amount' and print the encrypted text.

# TODO 3) Call the "encrypt()" function and pass in the user inputs.

# TODO 4) Fix the issue of when shifting the letters, if shift amount goes past the last letter,
#?         allow the shift amount to start from beginning of the alphabet with remaining shift amount.

# TODO 5) Create a function called "decrypt()" that takes 'text' and 'amount

# TODO 6) Inside "decrypt()" function, shift each letter of the 'text' backwards by 'amount' and 
#?          print the decrypted text.

# TODO 7) Combine "encrypt()" and "decrypt()" into single function called "cipher()".

# Todo 8) Deal with random inputs.

# TODO 9) Have the Cipher program be capable of restarting and ending when you want, so you dont have to hit Run program.



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



again = True

while again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
   
    cipher(text=text, amount=shift, done=direction)
    
    encrypt_again = input("Type 'yes' if you need to continue using cipher program. Otherwise, type 'no'.\n").lower()
    
    if encrypt_again == "no":
        again = False
        print("See you again!")     