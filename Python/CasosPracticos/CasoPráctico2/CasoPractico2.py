from math import e

def relu(x):
    return max(0, x)

def sigmoid(x):
    return 1 / (1 + e ** (-x))

def tanh(x):
    return 1 / (1 + 2 * e ** (-x))


entrada_datos = int(input("Ingrera el valor numerico: "))
entrada = relu(entrada_datos)
print(f"El valor ReLu es: {entrada}")

entrada_sigmoid = sigmoid(entrada_datos)
print(f"El valor Sigmoid es: {entrada_sigmoid}")

entrada_tanh = tanh(entrada_datos)
print(f"El valor Tanh es: {entrada_tanh}")

