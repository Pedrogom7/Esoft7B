# Sistema de Clusterização K-means com Limite Dinâmico

Projeto desenvolvido para a disciplina **Tópicos em Engenharia de Software**, ministrada pelo professor **Ricardo Satin**, na Unicesumar.

---

## Descrição

Este sistema implementa uma clusterização K-means com limite dinâmico para agrupamento de elementos, suportando dados numéricos e categóricos. O usuário pode cadastrar, editar e remover elementos (alunos), além de visualizar o resultado dos clusters em tempo real. O limite dinâmico permite a criação automática de novos clusters conforme a dispersão dos dados.

---

## Funcionalidades

- Cadastro de novos elementos com atributos (nome, idade, falta, nota)
- Suporte a elementos categóricos mapeados para valores numéricos
- Edição e remoção de elementos existentes
- Clusterização sequencial K-means com atualização dinâmica dos centróides
- Análise de dispersão para criação de novos clusters quando necessário
- Interface simples via terminal com menu de ações
- Limpeza automática da tela para melhor experiência do usuário

---

## Requisitos

- Python 3.6 ou superior
- Sistema operacional Windows, Linux ou macOS (funciona em terminal/console)

---

## Como executar

1. Clone este repositório:
    ```bash
    git clone <URL_DO_REPOSITORIO>
    ```
2. Navegue até a pasta do projeto:
    ```bash
    cd nome_do_projeto
    ```
3. Execute o programa:
    ```bash
    python main.py
    ```

---

## Estrutura do projeto

- `src/controllers/` — Controladores principais para cadastro e clusterização
- `src/models/` — Definição dos modelos Elemento, ElementoCateg e Cluster
- `src/services/` — Implementação do algoritmo K-means e análise de dispersão
- `src/utils/` — Funções utilitárias, como limpeza de tela e menu de ações
- `main.py` — Arquivo principal para executar o sistema

---

## Alunos

- **Pedro Henrique Magalhães Gomes** (22087525-2)
- **Eduardo Voltatone Ribeiro das Neves** (22207439-2)
- **Eduardo Silvestre Navarro** (22014553-2)



---

## Professor

Ricardo Satin — disciplina de Tópicos em Engenharia de Software, Unicesumar.
