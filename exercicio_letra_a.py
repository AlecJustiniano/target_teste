def conta_letra(palavra):
    letra_minuscula = palavra.count("a")
    letra_maiuscula = palavra.count("A")
    total_letra = (letra_minuscula + letra_maiuscula)
    if total_letra > 0:
        return f"A letra 'a' aparece {total_letra} vezes na string."
    else:
        return "A letra 'a' não foi encontrada na string."


palavras = input("Digite uma palavra: ")
print(conta_letra(palavras))
