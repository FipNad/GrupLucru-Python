# A = 1  // 65
# Z = 26 // 90 

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def decode(code,key):
    NEW_ALPHABET = ALPHABET[-key:] + ALPHABET[:-key]
    print(NEW_ALPHABET)

    code = code.upper()
    old_code = ''
    for letter in code:
        if(' _,.!-'.find(letter) != -1):
            new_letter = letter
        else:
            index = ALPHABET.index(letter)
            new_letter = NEW_ALPHABET[index]
        old_code = old_code + new_letter

    print('Stringul initial este: '+ old_code)


def brute_force(code):
    is_correct = 0
    key = 0
    decode(code,key)
    str = input('Este raspunsul corect? [y/n]: ')
    if(str == 'y'):
        is_correct = 1

    key = 1
    while (is_correct == 0):
        decode(code,key)
        str = input('Este raspunsul corect? [y/n]: ')
        if(str == 'y'):
            is_correct = 1
        key = key + 1

def frequency_method(code):
    print('da')
    


brute_force('')