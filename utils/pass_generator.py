import string
import random

def generator(size=16, caracteres_validos = string.printable):
    return ''.join(random.choice(caracteres_validos) for _ in range(size))

if __name__ == "__main__":
    print(generator())