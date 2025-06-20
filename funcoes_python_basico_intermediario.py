
# ----------------------------------------------
# Tópico: Funções em Python (Básico ao Intermediário)
# ----------------------------------------------

# O que é uma função?
# Uma função é um bloco de código reutilizável que realiza uma tarefa específica.

# ------------------------------------------------------
# 1. DEFININDO E CHAMANDO FUNÇÕES BÁSICAS
# ------------------------------------------------------

# Exemplo 1: Função sem parâmetros e sem retorno
def saudacao():
    print("Olá! Seja bem-vindo(a).")

# Chamando a função
saudacao()

# Exemplo 2: Função com parâmetros
def exibir_nome(nome):
    print("Olá,", nome)

exibir_nome("Lucas")

# Exemplo 3: Função com retorno
def soma(a, b):
    return a + b

resultado = soma(5, 3)
print("Resultado da soma:", resultado)

# ------------------------------------------------------
# 2. PARÂMETROS PADRÃO E NOMEADOS
# ------------------------------------------------------

# Podemos definir valores padrão para parâmetros
def apresentar(nome, saudacao="Olá"):
    print(f"{saudacao}, {nome}!")

apresentar("Maria")
apresentar("Carlos", "Bom dia")

# ------------------------------------------------------
# 3. RETORNANDO VÁRIOS VALORES
# ------------------------------------------------------

def operacoes(a, b):
    soma = a + b
    diferenca = a - b
    return soma, diferenca

s, d = operacoes(10, 4)
print("Soma:", s)
print("Diferença:", d)

# ------------------------------------------------------
# 4. FUNÇÕES COMO ARGUMENTOS
# ------------------------------------------------------

def aplicar_funcao(funcao, valor):
    return funcao(valor)

def quadrado(x):
    return x * x

print("Quadrado de 5:", aplicar_funcao(quadrado, 5))

# ------------------------------------------------------
# 5. ESCOPO DE VARIÁVEIS
# ------------------------------------------------------

# Variável local (existe só dentro da função)
def teste_escopo():
    local = "sou local"
    print(local)

teste_escopo()
# print(local)  # Isso daria erro: 'local' não está definido fora da função

# ------------------------------------------------------
# 6. FUNÇÕES RECURSIVAS (chamam a si mesmas)
# ------------------------------------------------------

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

print("Fatorial de 5:", fatorial(5))

# ------------------------------------------------------
# 7. FUNÇÕES ANÔNIMAS (lambda)
# ------------------------------------------------------

dobro = lambda x: x * 2
print("Dobro de 7:", dobro(7))

# Usando lambda com sorted()
nomes = ["ana", "JOÃO", "Carlos"]
nomes_ordenados = sorted(nomes, key=lambda nome: nome.lower())
print("Nomes ordenados:", nomes_ordenados)

# ------------------------------------------------------
# Fim do arquivo de explicação sobre funções
# ------------------------------------------------------
