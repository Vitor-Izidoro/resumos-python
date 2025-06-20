# ==========================================================
# Exercícios Focados em Funções e Listas
# ==========================================================

# -------------------------------
# 1. Completar a Função: Média de Notas
# -------------------------------

# Complete a função abaixo para calcular e retornar a média de uma lista de notas

def calcular_media(notas):
    soma = 0
    # COMPLETE AQUI:
    for nota in notas:
        soma += nota
    return soma / len(notas)

# notas = [7.5, 8.0, 6.5, 9.0, 5.5]
# print("Média:", calcular_media(notas))

# -------------------------------
# 2. Função: Retornar maior valor de uma lista
# -------------------------------

def encontrar_maior(lista):
    maior = lista[0]
    for valor in lista:
        if valor > maior:
            maior = valor
    return maior

# numeros = [4, 9, 2, 15, 8]
# print("Maior valor:", encontrar_maior(numeros))

# -------------------------------
# 3. Completar: Inserir elementos e mostrar acima da média
# -------------------------------

def acima_da_media():
    notas = []
    # COMPLETE: ler 5 notas e adicionar à lista
    for i in range(5):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)

    media = calcular_media(notas)
    print("Média:", media)

    # Mostrar somente notas acima da média
    for nota in notas:
        if nota > media:
            print("Nota acima da média:", nota)

# acima_da_media()

# -------------------------------
# 4. Buscar elemento: Complete a lógica
# -------------------------------

def buscar_elemento(lista, elemento):
    # COMPLETE: retorne True se o elemento estiver na lista
    if elemento in lista:
        return True
    else:
        return False

# nomes = ["Ana", "Carlos", "Marina", "Lucas"]
# nome_busca = input("Digite o nome para busca: ")
# if buscar_elemento(nomes, nome_busca):
#     print("Nome encontrado!")
# else:
#     print("Nome não está na lista.")

# -------------------------------
# 5. Função: Inserir nome de aprovados e procurar nome
# -------------------------------

def lista_aprovados():
    aprovados = []

    for i in range(5):
        nome = input(f"Digite o nome do aluno {i+1} aprovado: ")
        aprovados.append(nome)

    busca = input("Digite o nome que deseja buscar: ")
    if buscar_elemento(aprovados, busca):
        print("Aluno aprovado!")
    else:
        print("Aluno não encontrado.")

# lista_aprovados()

# ==========================================================
# FIM DOS EXERCÍCIOS
# ==========================================================
