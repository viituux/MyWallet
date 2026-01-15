# 💰 MyWallet - Controle Financeiro Pessoal

Aplicação web desenvolvida em Python com Flask para gerenciamento de finanças pessoais. O sistema permite lançar receitas e despesas, calculando automaticamente o saldo atual e formatando os valores para o padrão brasileiro (R$).

Este projeto foi desenvolvido como parte do portfólio de estudos em **Análise e Desenvolvimento de Sistemas (ADS)**, focando em lógica de backend e manipulação de banco de dados.

## 🚀 Funcionalidades

* **Dashboard em Tempo Real:** Visualização imediata do total de Entradas, Saídas e Saldo Final.
* **Indicadores Visuais:** O saldo muda de cor (Azul para positivo, Preto para negativo) automaticamente.
* **Lançamento de Transações:** Cadastro simples de descrição, valor e tipo (Entrada/Saída).
* **Extrato Detalhado:** Tabela com histórico de transações, incluindo a data do lançamento.
* **Formatação Brasileira:** Valores monetários exibidos corretamente com vírgula e ponto (ex: R$ 1.250,00).
* **Exclusão:** Possibilidade de remover lançamentos errados.

## 🛠️ Tecnologias Utilizadas

* **Python 3:** Lógica do backend e cálculos matemáticos.
* **Flask:** Framework web para gerenciamento de rotas e templates.
* **SQLAlchemy:** ORM para integração com Banco de Dados SQL.
* **SQLite:** Banco de dados leve e local (arquivo `carteira.db`).
* **Bootstrap 5:** Estilização responsiva, cards e ícones (Bootstrap Icons).
* **Jinja2:** Motor de templates para exibir dados dinâmicos e formatar moeda no HTML.

## 📦 Como rodar o projeto localmente

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/viituux/mywallet.git](https://github.com/viituux/mywallet.git)
    ```

2.  **Entre na pasta do projeto:**
    ```bash
    cd mywallet
    ```

3.  **Instale as dependências:**
    ```bash
    pip install flask flask_sqlalchemy
    ```

4.  **Execute a aplicação:**
    ```bash
    python app.py
    ```

5.  **Acesse no navegador:**
    Abra o link `http://127.0.0.1:5000`

---
Desenvolvido por **João Victor Marques** 🎓
