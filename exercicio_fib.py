def fibonacci(n):
    # Inicializando a sequência de Fibonacci
    sequencia_fib = [0, 1]

    # Calculando a sequência de Fibonacci até o número informado
    while sequencia_fib[-1] < n:
        next_value = sequencia_fib[-1] + sequencia_fib[-2]
        sequencia_fib.append(next_value)

    return sequencia_fib


def verifica_fibonacci(n):
    # Calcula a sequência de Fibonacci até o número informado
    sequencia_fib = fibonacci(n)

    # Verifica se o número está na sequência
    if n in sequencia_fib:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."


numero = int(input("Informe um número: "))

resultado = verifica_fibonacci(numero)
print(resultado)
