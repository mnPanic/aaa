from typing import List


def recognize(word: str) -> bool:
    """
    Reconoce una cadena solo si es un prefijo que coincide con un fin de un
    "bloque" de una cadena "a la Champernowne".
    """

    n = 0
    current_champ = ""
    while len(current_champ) <= len(word):
        if word == current_champ:
            return True
        
        n += 1
        current_champ = champ_up_to(n)
    
    return False

def champ_up_to(n: int) -> str:
    """Genera la secuencia "a la Champernowne" hasta el bloque de tamaño n."""

    seq = ""
    for n in range(1, n+1):
        seq += ''.join(all_words_of_length(n))
    
    return seq

def all_words_of_length(n: int) -> List[str]:
    """Genera todas las cadenas de longitud n en orden lexicográfico"""
    
    if n == 1:
        return ["0", "1"]

    prev = all_words_of_length(n - 1)
    adding_zero = map(lambda word: word + "0", prev)
    adding_one = map(lambda word: word + "1", prev)
    return sorted(list(adding_zero) + list(adding_one))

def main():
    print(champ_up_to(4))

    print("should be false:", recognize("0"))
    print("should be true:", recognize("01"))
    print("should be true:", recognize("0100011011"))
    print("should be false:", recognize("010001101"))
    print("should be true:", recognize("0100011011000001010011100101110111"))
    print("should be true:", recognize("01000110110000010100111001011101110000000100100011010001010110011110001001101010111100110111101111"))

if __name__ == "__main__":
    main()