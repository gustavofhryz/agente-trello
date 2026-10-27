# Agente de Automação de Fluxo de Trabalho com Trello e Python

Este projeto consiste em um agente desenvolvido em Python para automatizar a criação, listagem e gerenciamento de tarefas em um quadro do Trello utilizando a API.

## 🛠️ O que o agente faz e ferramentas utilizadas
- Conecta-se à API do Trello de forma segura.
- Lista quadros, listas e gerencia cartões de tarefas de forma automatizada.
- **Ferramentas:** Python 3.x, `requests`, `python-dotenv`.

## 🚀 Como configurar e rodar

### 1. Clone este repositório
```bash
git clone https://github.com/gustavofhryz/agente-trello.git
cd agente_trello
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configuração do Trello e Credenciais
1. Acesse o portal do desenvolvedor do Trello e obtenha sua **API Key** e **Token**.
2. Crie um arquivo chamado `.env` na raiz do projeto (este arquivo já está no `.gitignore` para sua segurança).
3. Adicione as seguintes variáveis no arquivo `.env`:
```env
TRELLO_API_KEY=sua_api_key_aqui
TRELLO_TOKEN=seu_token_aqui
```

### 4. Como Executar
```bash
python main.py
```

## 🌟 Demonstrações

<img width="675" height="130" alt="1" src="https://github.com/user-attachments/assets/cd1184c4-7504-463d-817b-0e641ba24410" />

<img width="514" height="237" alt="2" src="https://github.com/user-attachments/assets/75882f76-4114-4c39-902a-8ef1c211bbe1" />



