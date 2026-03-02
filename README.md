
<p align="center">
  <img src="imagens/ufma.png" alt="UFMA" width="180">
</p>

<p align="center">
  <strong>Universidade Federal do Maranhão</strong><br>
  <strong>Centro de Ciências Exatas e Tecnologias</strong><br>
  <strong>Curso de Engenharia da Computação</strong><br>
  <strong>Disciplina: Lógica e Matemática Discreta</strong><br>
  <strong>Professor: Rondineli Seba</strong><br><br>
  <strong>Discentes:</strong><br>
  <strong>Renata Costa Rocha</strong> — Matrícula: 20240001556<br>
  <strong>Raphael Câmara Sá</strong> — Matrícula: 20240001547
</p>

<hr>

<p align="center">
  <em>
    Este projeto foi desenvolvido como parte das atividades avaliativas da disciplina de 
    <strong>Lógica e Matemática Discreta</strong>, do curso de Engenharia da Computação 
    da Universidade Federal do Maranhão.
    <br><br>
    O objetivo do projeto é implementar um analisador automatizado de sentenças 
    lógicas, aplicando os fundamentos da <strong>Lógica Proposicional e de Predicados</strong> 
    por meio do desenvolvimento de um sistema computacional em Python.
    <br><br>
    O desenvolvimento do código, aliado à documentação técnica apresentada neste 
    repositório, corresponde às atividades avaliativas da disciplina.
  </em>
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=flat-square" alt="Python">
  <img src="https://img.shields.io/badge/Git-Version_Control-orange?style=flat-square" alt="Git">
  <img src="https://img.shields.io/badge/GitHub-Repositório-black?style=flat-square" alt="GitHub">
</p>

---

## 1. Descrição do Projeto

Este repositório contém a implementação de um **Analisador de Lógica Formal**, capaz de:

- Identificar proposições atômicas;
- Mapear conectivos lógicos;
- Construir a estrutura sintática da expressão (AST);
- Gerar automaticamente a Tabela-Verdade completa (2ⁿ linhas).

O sistema foi desenvolvido em **Python**, utilizando estrutura modular para organização do código.

---

## 2. Objetivo

O principal objetivo deste trabalho é:

- Aplicar os fundamentos da Lógica Proposicional;
- Implementar parsing de expressões lógicas;
- Gerar automaticamente Tabelas-Verdade;
- Desenvolver código modular e bem estruturado;
- Produzir documentação técnica clara e coerente com a teoria estudada.

---

## 3. Especificação do Problema

O programa recebe como entrada uma sentença lógica em formato restrito, contendo:

- Proposições atômicas (p, q, r, ...);
- Conectivos lógicos:
  - Negação (~)
  - Conjunção (&)
  - Disjunção (|)
  - Implicação (->)
  - Bicondicional (<->)
- Parênteses para organização da precedência.

A partir da expressão fornecida, o sistema:

1. Realiza a tokenização da entrada;
2. Constrói a árvore sintática (AST);
3. Identifica proposições e conectivos utilizados;
4. Gera a Tabela-Verdade correspondente.

---

## 4. Fundamentos Teóricos

A implementação baseia-se nos seguintes conceitos formais:

- Proposições atômicas;
- Conectivos lógicos (¬, ∧, ∨, →, ↔);
- Precedência de operadores;
- Avaliação semântica de fórmulas;
- Geração de Tabelas-Verdade (2ⁿ combinações possíveis).

O algoritmo de parsing utiliza o método **Shunting-yard**, garantindo o respeito à precedência dos operadores.

---

## 5. Organização do Código

O projeto está estruturado da seguinte forma:

```

src/
├── tokenizer.py
├── parser.py
├── ast_nodes.py
├── evaluator.py
├── truth_table.py
└── cli.py

````

Cada módulo possui responsabilidade específica:

- **tokenizer.py** → análise léxica
- **parser.py** → construção da AST
- **evaluator.py** → avaliação lógica
- **truth_table.py** → geração da tabela-verdade
- **cli.py** → interface de execução

Essa organização garante modularidade, legibilidade e manutenção facilitada.

---

## 6. Como Executar o Programa

### Pré-requisitos
- Python 3.x instalado
- Terminal de comandos (CMD, PowerShell ou terminal do VS Code)

### Execução

1. Clone o repositório:

```bash
git clone https://github.com/ahcorataner/analisador_logica_formal.git
````

2. Acesse o diretório:

```bash
cd analisador_logica_formal
```

3. Execute o programa:

```bash
python -m src.cli
```

4. Digite a expressão lógica desejada, por exemplo:

```
(p & q) -> (~r | p)
```

---

## 7. Exemplo de Execução

Entrada:

```
(p & q) -> r
```

Saída:

* Lista de proposições identificadas;
* Lista de conectivos utilizados;
* Tabela-Verdade completa com 2ⁿ linhas.

---

## 8. Tratamento de Erros

O sistema valida:

* Parênteses desbalanceados;
* Operadores em posições inválidas;
* Caracteres não reconhecidos;
* Expressões mal formadas.

---

## 9. Considerações Finais

O desenvolvimento deste projeto permitiu integrar fundamentos teóricos da Lógica Formal com práticas de Engenharia de Software, reforçando a importância da automação na análise de estruturas matemáticas.

---

## 10. Licença

Este projeto possui finalidade **exclusivamente acadêmica**, sendo desenvolvido para fins educacionais no contexto da disciplina de Lógica e Matemática Discreta da UFMA.

---

## 11. Contato

* **Renata Costa Rocha** — [renata.rocha@discente.ufma.br](mailto:renata.rocha@discente.ufma.br)
* **Raphael Câmara Sá**

````

