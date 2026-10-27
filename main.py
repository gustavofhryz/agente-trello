import os
from dotenv import load_dotenv
from trello import TrelloClient

# Carrega as variáveis do ficheiro .env
load_dotenv()

api_key = os.getenv("TRELLO_API_KEY")
token = os.getenv("TRELLO_TOKEN")

# Inicializa o cliente do Trello
client = TrelloClient(
    api_key=api_key,
    token=token
)

# Testa a conexão listando os quadros (boards) do seu Trello
print("A ligar ao Trello...")
boards = client.list_boards()

print("\nQuadros encontrados na sua conta:")
for board in boards:
    print(f"- {board.name} (ID: {board.id})")