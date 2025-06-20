# ==========================================================
# Exercícios de Python: Teste de Mesa, Funções e Listas
# ==========================================================

# -------------------------------
# 1. Teste de Mesa
# -------------------------------

# Simule o código abaixo e diga o que será impresso.
# Faça isso manualmente (teste de mesa).

def exercicio_1():
    var = 40
    for cont in range(10, 60, 10):
        if cont == var:
            print("Parando o laço")
            break
        var -= 10
    print("Var final =", var)

# Descomente para testar:
# exercicio_1()

# -------------------------------
# 2. Função com Parâmetro e Sem Retorno
# -------------------------------

def saudacao(nome):
    print("Olá,", nome, "! Bem-vindo(a).")

# saudacao("Ana")

# -------------------------------
# 3. Função com Retorno
# -------------------------------

def somar(a, b):
    return a + b

# resultado = somar(3, 4)
# print("Resultado da soma:", resultado)

# -------------------------------
# 4. Lista com Média
# -------------------------------

def calcular_media():
    notas = []
    for i in range(5):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)

    soma = 0
    for nota in notas:
        soma += nota

    media = soma / len(notas)
    print("Média da turma:", media)

    for nota in notas:
        if nota > media:
            print("Nota acima da média:", nota)

# calcular_media()

# -------------------------------
# 5. Procurar elemento na lista
# -------------------------------

def procurar_elemento():
    lista = []
    for i in range(5):
        valor = int(input(f"Digite o valor {i+1}: "))
        lista.append(valor)

    busca = int(input("Digite o número que deseja encontrar: "))

    if busca in lista:
        print("Número encontrado na posição:", lista.index(busca))
    else:
        print("Número não encontrado.")

# procurar_elemento()

# ==========================================================
# EXPLICAÇÕES DOS EXERCÍCIOS
# ==========================================================

# EXERCÍCIO 1:
# Simula passo a passo os valores de cont e var.
# Quando cont == var, imprime "Parando o laço" e sai.
# Depois imprime o valor final da variável var.

# EXERCÍCIO 2:
# Uma função simples com parâmetro de entrada que imprime uma mensagem.
# Não há retorno, só exibe uma saudação personalizada.

# EXERCÍCIO 3:
# A função recebe dois números, soma e retorna o resultado.
# O retorno é armazenado em uma variável e impresso.

# EXERCÍCIO 4:
# Cria uma lista com 5 notas.
# Calcula a média da turma e imprime as notas acima da média.

# EXERCÍCIO 5:
# Permite digitar 5 números e busca por um valor informado.
# Se estiver na lista, mostra a posição. Caso contrário, informa que não encontrou.

# FIM DOS EXERCÍCIOS
