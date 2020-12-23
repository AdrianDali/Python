import os

KEYS = {
    "a" :"d",
    "b" :"J",
    "c" :"g",
    "d" :"j",
    "e" :"K",
    "f" :"D",
    "g" :"a",
    "h" :"d",
    "i" :"w",
    "j" :"t",
    "k" :"u",
    "l" :"o",
    "m" :"ñ",
    "n" :"Q",
    "o" :"W",
    "p" :"R",
    "q" :"U",
    "r" :"O",
    "s" :"M",
    "t" :"M",
    "u" :"-",
    "v" :"_",
    "w" :".",
    "x" :"H",
    "y" :"h",
    "z" :"s",
    "A" :"t",
    "B" :"e",
    "C" :"d",
    "D" :"h",
    "E" :"n",
    "F" :"b",
    "G" :"v",
    "H" :"c",
    "I" :"x",
    "J" :"z",
    "K" :"J",
    "L" :"H",
    "M" :"G",
    "N" :"F",
    "O" :"D",
    "P" :"S",
    "Q" :"A",
    "R" :"1",
    "S" :"2",
    "T" :"3",
    "U" :"4",
    "V" :"5",
    "W" :"6",
    "X" :"7",
    "Y" :"8",
    "Z" :"9",

}

def cypher(message):
    words = message.split(' ')
    cypher_message = []

    for word in words:
        cypher_word=''
        for letter in word:
            cypher_word += KEYS[letter]
        cypher_message.append(cypher_word)

    return ' '.join(cypher_message)          

def decipher(message):
    pass

def run():
    while True:
        os.system('clrs')
        command = str(input("""
        _______________________________
        |   C R I P T O G R A F I A    |
        | ¿Que deseas hacer?           |
        |                              |
        |   [c]cifrar mensaje          |
        |   [d]decifrar mensaje        |
        |   [s]salir                   |
        |______________________________|
        : 
         """))

        if command == 'c':
            message = str(input("Escribe tu mensaje: "))
            cypher_messge = cypher(message)
            print(cypher_messge)
        elif command == 'd':
            
        elif command == 's':
            print("salir")
        else:
            print("comando no encontrado!!")

    
if __name__ == '__main__':
    run()


