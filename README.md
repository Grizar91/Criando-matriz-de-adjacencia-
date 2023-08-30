# Gerador de Matriz de Adjacência de Grafo

Este é um simples gerador de matriz de adjacência de um grafo usando a biblioteca Networkx em Python.

## Requisitos

Certifique-se de ter Python instalado em seu sistema. Você pode baixá-lo em https://www.python.org/downloads/.

Também, instale a biblioteca Networkx usando o seguinte comando:

pip install networkx


## Uso

1. Clone o repositório ou baixe o arquivo `gerador_grafo.py`.

2. Crie um arquivo de texto chamado `grafo.txt` no mesmo diretório que o arquivo `gerador_grafo.py`.

3. No arquivo `grafo.txt`, insira as arestas do grafo no formato "nó_origem nó_destino", uma por linha.

4. Execute o script `gerador_grafo.py` usando o seguinte comando:

python gerador_grafo.py

5. A matriz de adjacência será exibida no terminal.

## Exemplo de arquivo grafo.txt

Matriz de Adjacência:
A B
B C
C A
B D

Este exemplo representa um grafo com as arestas: (A,B), (B,C), (C,A) e (B,D).

![image](https://github.com/Grizar91/Criando-matriz-de-adjacencia-/assets/143652037/fbe6c796-533c-4802-8255-f1a9c3941a26)

## Observações

- Certifique-se de que o arquivo `grafo.txt` esteja no mesmo diretório que o arquivo `gerador_grafo.py`.
- As arestas no arquivo `grafo.txt` devem estar no formato "nó_origem nó_destino", uma por linha.




