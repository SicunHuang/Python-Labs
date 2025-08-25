ALPHABET = "abcdefghijklmnopqrstuvwxyz "

def encryption_up2(s):
    key = "cdefghijklmnopqrstuvwxyz ab"
    result = ""
    for i in s:
        replace = key[ALPHABET.find(i)]
        result = result + replace
    return result #question(1)
        
def decryption_up2(s):
    key = "cdefghijklmnopqrstuvwxyz ab"
    result = ""
    for i in s:
        replace = ALPHABET[key.find(i)]
        result = result + replace
    return result #question(2)

def decryption_up5(s):
    key = "fghijklmnopqrstuvwxyz abcde"
    result = ""
    for i in s:
        replace = ALPHABET[key.find(i)]
        result = result + replace
    return result #question(3)

def decryption_randomkey(s):
    key = "hvieksyrbdajqwncxmgufltp oz"
    result = ""
    for i in s:
        replace = ALPHABET[key.find(i)]
        result = result + replace
    return result #question(4)

# ALPHABET.find(letter)   question(5)

# index = ALPHABET.find(letter)
# key[index]  question(6)