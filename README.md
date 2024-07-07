# Criando um Ambiente de Desenvolvimento em Python

## Passos

1. **Instale o Python**
   - Baixe e instale a versão mais recente do Python a partir do site oficial: [python.org](https://www.python.org/downloads/).

2. **Instale o `pip` (se não vier pré-instalado)**
   - O `pip` é o gerenciador de pacotes do Python. Ele geralmente vem instalado com o Python, mas se não estiver, você pode instalá-lo seguindo as instruções [aqui](https://pip.pypa.io/en/stable/installation/).

3. **Instale o `virtualenv`**
   - `virtualenv` é uma ferramenta para criar ambientes virtuais isolados em Python.
     ```bash
     pip install virtualenv
     ```

4. **Crie um ambiente virtual**
   - Navegue até o diretório onde você deseja criar seu ambiente de desenvolvimento e execute:
     ```bash
     virtualenv nome_do_ambiente
     ```

5. **Ative o ambiente de desenvolvimento**
   - No Windows:
     ```bash
     nome_do_ambiente\Scripts\activate
     ```
   - No macOS e Linux:
     ```bash
     source nome_do_ambiente/bin/activate
     ```

6. **Liste as dependências do projeto**
   - Para facilitar a instalação das dependências em outros ambientes, liste todas as dependências do seu projeto em um arquivo `requirements.txt`:
     ```bash
     pip freeze > requirements.txt
     ```

7. **Instale as dependências a partir do `requirements.txt`**
   - Em um novo ambiente, você pode instalar todas as dependências do projeto usando:
     ```bash
     pip install -r requirements.txt
     ```

Siga estes passos para configurar um ambiente de desenvolvimento Python limpo e isolado para seu projeto.
