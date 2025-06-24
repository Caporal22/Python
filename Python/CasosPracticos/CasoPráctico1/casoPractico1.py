"""
Caso práctico número 1
Tabla Hash
"""
import hashlib


def data_input():
    return input("Enter the message: ")

def data_hash(texto):
    return hashlib.sha256(texto.encode()).hexdigest()

def data_normal_hash(texto):
    return hash(texto)


def main():
    texto = data_input()
    hash_table_256 = data_hash(texto)
    hash_table_normal = data_normal_hash(texto)

    print("----- Results -----\n")
    print(f"Texto: {texto}\n")
    print(f"Normal table hash: {hash_table_normal}\n")
    print(f"Table hash: {hash_table_256}\n")



if __name__ == "__main__":
    main()

