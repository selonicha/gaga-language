print('Welcome to Planet Language')
print("="*30)
phrase = print("Input the word : ")

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "bcdfghjklmnpqrstvwxyz":
            if letter.isupper():
                translation = translation + "G"
            else :
                translation = translation + "g"
        else:
            translation = translation + letter

    return translation

alfabet =[]
def nilai(kata):
    translation = " "
    for letter in kata:
        if letter in  "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
            alfabet.append(letter)
            for consonant in alfabet:
                print(alfabet.index(consonant))
        
# for huruf in kata:
#     print(kata.index(huruf)+1)

            
