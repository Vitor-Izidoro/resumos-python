
# Resumo: Teste de Mesa, Funções e Listas em Python

## 1. Teste de Mesa

### O que é?
O teste de mesa é uma simulação manual da execução de um código, onde acompanhamos linha por linha a evolução das variáveis e o que o programa imprime.

Ele serve para:
- Entender melhor o funcionamento de um algoritmo.
- Detectar erros lógicos.
- Prever saídas com segurança.

### Como fazer:
1. Identifique as variáveis usadas.
2. Crie uma tabela com colunas para linha, variáveis e saídas.
3. Vá preenchendo conforme o código "executa".

### Exemplo:

```python
var = 30
for cont in range(20, 100, 10):
    if cont == var:
        print("Saindo antes")
        break
    var = var - 10
print("Var = ", var)
```

**Simulação parcial:**

| `cont` | `var` antes | `var` depois | Impressão       |
|--------|-------------|--------------|-----------------|
| 20     | 30          | 20           |                 |
| 30     | 20          | 10           |                 |
| 40     | 10          | 0            |                 |
| 50     | 0           | -10          |                 |
| ...    | ...         | ...          | Var = -10       |

Observação: o `if cont == var` nunca é verdadeiro, então o `break` não ocorre. O loop segue até o fim.

---

## 2. Funções com `def`

### Para que servem?
Funções são blocos de código reutilizáveis que recebem dados (parâmetros), executam tarefas e podem (ou não) retornar resultados.

Por que usar funções?
- Deixam o código mais organizado e legível.
- Evitam repetições.
- Facilitam manutenção e testes.

### Estrutura básica:

```python
def nome_funcao(parametros):
    # instruções
    return resultado  # opcional
```

### Exemplo 1 – sem retorno:

```python
def imprimir_boas_vindas(nome):
    print("Bem-vindo(a),", nome)

imprimir_boas_vindas("Maria")
```

Saída: `Bem-vindo(a), Maria`

### Exemplo 2 – com retorno:

```python
def calcular_media(n1, n2):
    return (n1 + n2) / 2

media = calcular_media(8, 6)
print("Média:", media)
```

Saída: `Média: 7.0`

---

## 3. Listas (Vetores)

### O que são?
Listas são estruturas que armazenam vários valores em sequência, acessados por índices numéricos (a partir do 0).

```python
notas = [7.0, 8.5, 6.0]
print(notas[0])  # exibe 7.0
```

### Operações úteis:

| Ação             | Comando                          |
|------------------|----------------------------------|
| Criar lista      | `lista = []`                    |
| Adicionar        | `lista.append(valor)`           |
| Inserir em pos   | `lista.insert(índice, valor)`   |
| Remover          | `lista.remove(valor)`           |
| Contar repetições| `lista.count(valor)`            |
| Achar posição    | `lista.index(valor)`            |
| Ordenar          | `lista.sort()`                  |
| Percorrer        | `for item in lista:`            |

### Exemplo prático:

```python
notas = []

for i in range(5):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

soma = 0
for nota in notas:
    soma += nota

media = soma / len(notas)
print("Média:", media)

for nota in notas:
    if nota > media:
        print("Nota acima da média:", nota)
```

Esse código mostra como coletar dados, calcular média e identificar valores acima dela — tudo usando listas e laços.

---

## Resumo Final

| Tema         | Conceito-Chave                                                            |
|--------------|---------------------------------------------------------------------------|
| Teste de Mesa| Simular a execução do código e acompanhar o valor das variáveis.          |
| Funções      | Reaproveitar código com parâmetros e (opcionalmente) retorno.             |
| Listas       | Guardar vários dados de forma organizada e acessível por índices.         |
