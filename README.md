# PyCat Otimizado: Leitor de Arquivos em Stream

Uma ferramenta de interface de linha de comando (CLI) desenvolvida em Python para leitura otimizada de arquivos massivos, com foco em eficiência de memória (I/O) e tratamento rigoroso de exceções.

## 🧠 O Problema Arquitetural
Scripts tradicionais de leitura (como `with open().read()`) tentam carregar o conteúdo integral do arquivo na memória RAM. Ao lidar com datasets na casa dos gigabytes, essa abordagem gera estouro de memória (MemoryError) e travamento do sistema operacional.

## 🚀 A Solução
Este projeto substitui o carregamento em lote pelo processamento em fluxo contínuo (stream/chunks). Utilizando iteração direta e chamadas de baixo nível (`sys.stdout.write`), o consumo de memória permanece constante e linear, independentemente do tamanho do arquivo lido. 

Além disso, a ferramenta conta com:
- **Resiliência:** Blocos de `try/except` para lidar com arquivos inexistentes ou sem permissão de leitura, redirecionando falhas para `sys.stderr`.
- **Interface Visual de Ajuda:** Um painel formatado no terminal com códigos ANSI (True Color).
- **Simulador Gráfico:** Uma interface desenvolvida em `tkinter` para demonstrar o consumo em tempo real utilizando leitura por chunks assíncronos.

---

## 💻 Demonstração de Uso

### 1. Painel da Linha de Comando (CLI)
Para visualizar as opções e o painel customizado:
````bash
python cat.py -h
````
---

## 🛠️ Stacks e Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Terminal](https://img.shields.io/badge/CLI-4D4D4D?style=for-the-badge&logo=windows-terminal&logoColor=white)

