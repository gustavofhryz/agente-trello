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

print("A ligar ao Trello...")
boards = client.list_boards()
my_board = boards[0]  # Seleciona o primeiro quadro encontrado
print(f"Quadro selecionado: {my_board.name}")

# 1. LISTAR AS LISTAS DO QUADRO
lists = my_board.list_lists()
print("\n--- Listas encontradas no Quadro ---")
for lst in lists:
    print(f"- {lst.name} (ID: {lst.id})")

# Garante que existem pelo menos duas listas para testar a movimentação
if len(lists) >= 2:
    lista_origem = lists[0]
    lista_destino = lists[1]

    # 2. CRIAR UM CARTÃO
    print(f"\n[AÇÃO] A criar um novo cartão na lista '{lista_origem.name}'...")
    novo_cartao = lista_origem.add_card('Tarefa Automatizada pelo Agente')
    print(f"Cartão criado com sucesso: '{novo_cartao.name}'")

    # 3. MOVER O CARTÃO
    print(f"\n[AÇÃO] A mover o cartão para a lista '{lista_destino.name}'...")
    novo_cartao.change_list(lista_destino.id)
    print("Cartão movido com sucesso entre as listas!")
else:
    print("\n[Aviso] Certifique-se de que tem pelo menos 2 listas criadas no seu quadro do Trello (ex: 'A Fazer' e 'Concluído').")