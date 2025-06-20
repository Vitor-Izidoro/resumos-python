
# ---------------------------------------------------------------
# Arquivo: funcoes_python_basico_intermediario.py
# Tema: Explicação completa sobre funções em Python (básico ao intermediário)
# ---------------------------------------------------------------

# O que é uma função?
# --------------------
# Uma função é um bloco de código que pode ser chamado pelo nome para realizar uma tarefa.
# Ao usar funções, você evita repetir código, melhora a organização e facilita a manutenção.

# ------------------------------------------------------
# 1. COMO DEFINIR E CHAMAR FUNÇÕES
# ------------------------------------------------------

# Sintaxe básica:
# def nome_da_funcao(parametros_opcionais):
#     instruções
#     return valor_opcional

# Exemplo 1: Função simples sem parâmetros e sem retorno
def saudacao():
    # Essa função apenas exibe uma saudação
    print("Olá! Seja bem-vindo(a).")

# Chamando a função
saudacao()

# Exemplo 2: Função com parâmetro
def exibir_nome(nome):
    # Essa função recebe um nome e exibe uma mensagem personalizada
    print("Olá,", nome)

exibir_nome("Lucas")

# Exemplo 3: Função com retorno
def soma(a, b):
    # Essa função retorna a soma de dois números
    return a + b

resultado = soma(5, 3)
print("Resultado da soma:", resultado)

# ------------------------------------------------------
# 2. PARÂMETROS PADRÃO E PARÂMETROS NOMEADOS
# ------------------------------------------------------

# Parâmetros padrão têm valores predefinidos que são usados se o argumento não for fornecido
def apresentar(nome, saudacao="Olá"):
    print(f"{saudacao}, {nome}!")

apresentar("Maria")              # Usa o padrão "Olá"
apresentar("Carlos", "Bom dia")  # Substitui o padrão

# Parâmetros nomeados permitem chamar argumentos fora da ordem, especificando o nome
apresentar(saudacao="Oi", nome="João")

# ------------------------------------------------------
# 3. RETORNANDO MÚLTIPLOS VALORES
# ------------------------------------------------------

# Funções podem retornar múltiplos valores usando tuplas
def operacoes(a, b):
    soma = a + b
    diferenca = a - b
    return soma, diferenca

# Recebendo múltiplos valores de retorno
s, d = operacoes(10, 4)
print("Soma:", s)
print("Diferença:", d)

# ------------------------------------------------------
# 4. FUNÇÕES COMO ARGUMENTOS
# ------------------------------------------------------

# Funções são objetos em Python, então podem ser passadas como argumentos
def aplicar_funcao(funcao, valor):
    return funcao(valor)

def quadrado(x):
    return x * x

print("Quadrado de 5:", aplicar_funcao(quadrado, 5))

# ------------------------------------------------------
# 5. ESCOPO DE VARIÁVEIS
# ------------------------------------------------------

# Variáveis criadas dentro de uma função são locais (não existem fora dela)
def teste_escopo():
    local = "sou local"
    print(local)

teste_escopo()

# A linha abaixo causaria erro se descomentada, pois 'local' só existe dentro da função
# print(local)

# Variáveis globais existem fora das funções e podem ser lidas dentro delas
global_var = "Sou global"

def acessar_global():
    print(global_var)

acessar_global()

# ------------------------------------------------------
# 6. FUNÇÕES RECURSIVAS
# ------------------------------------------------------

# Uma função recursiva é aquela que chama a si mesma.
# Exemplo clássico: cálculo de fatorial

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

print("Fatorial de 5:", fatorial(5))  # 5 * 4 * 3 * 2 * 1 = 120

# Atenção: funções recursivas devem ter uma condição de parada (caso base)

# ------------------------------------------------------
# CONCLUSÃO
# ------------------------------------------------------

# Funções são uma ferramenta essencial em Python para:
# - Organizar o código em blocos reutilizáveis
# - Reduzir repetição de código
# - Melhorar clareza e manutenção

# Níveis abordados:
# - Criação de funções simples
# - Parâmetros e valores de retorno
# - Escopo de variáveis
# - Funções como objetos
# - Recursividade

