alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
user_input=input("Enter sth: ").lower()
for letter in range(len(alphabet)):
    if alphabet[letter] in user_input:
        print(alphabet[letter],user_input.count(alphabet[letter]))