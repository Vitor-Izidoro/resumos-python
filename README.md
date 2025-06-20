# resumos-python


# Resumo de Conteúdo: Teste de Mesa, Funções com `def` e Listas em Python

##  1. Teste de Mesa

###  Conceito
Teste de mesa é como **simular a execução de um programa manualmente**, acompanhando o valor das variáveis **passo a passo**.

É útil para:
- Entender como o código funciona.
- Encontrar erros.
- Saber exatamente o que será impresso na tela.

###  Como fazer:
1. Liste as variáveis.
2. Monte uma tabela com colunas: linha, valores das variáveis e saída.
3. Atualize a cada passo.

###  Exemplo:

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
| ...    | ...         | ...          | `Var = -10`     |

---

##  2. Funções com `def`

###  Conceito
Funções são **blocos de código reutilizáveis** com **parâmetros de entrada** e **retorno opcional**.

Vantagens:
- Organiza o código.
- Evita repetição.
- Facilita manutenção.

###  Estrutura:

```python
def nome_da_funcao(param1, param2):
    # comandos
    return resultado
```

###  Exemplo 1 — sem retorno:

```python
def imprimir_boas_vindas(nome):
    print("Bem-vindo(a),", nome)

imprimir_boas_vindas("Maria")
```

**Saída:** `Bem-vindo(a), Maria`

###  Exemplo 2 — com retorno:

```python
def calcular_media(n1, n2):
    return (n1 + n2) / 2

media = calcular_media(8, 6)
print("Média:", media)
```

**Saída:** `Média: 7.0`

---

##  3. Listas (Vetores)

###  Conceito
Listas guardam **vários dados em sequência**, acessíveis por **índices** a partir do zero.

```python
notas = [7.0, 8.5, 6.0]
print(notas[0])  # 7.0
```

### 🛠 Operações comuns:

| Ação       | Código                          |
|------------|----------------------------------|
| Criar      | `lista = []`                    |
| Adicionar  | `lista.append(10)`              |
| Inserir    | `lista.insert(1, 5)`            |
| Remover    | `lista.remove(10)`              |
| Contar     | `lista.count(5)`                |
| Buscar pos | `lista.index(5)`                |
| Ordenar    | `lista.sort()`                  |
| Percorrer  | `for i in lista:`               |

### 🧪 Exemplo prático:

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

---

##  Conclusão

| Tema         | Essência                                                                  |
|--------------|---------------------------------------------------------------------------|
| Teste de mesa| Simular manualmente o código, rastreando variáveis passo a passo.         |
| Funções      | Separar tarefas em blocos, com entrada (parâmetros) e possível retorno.   |
| Listas       | Armazenar e manipular vários dados dinamicamente por índice.              |
