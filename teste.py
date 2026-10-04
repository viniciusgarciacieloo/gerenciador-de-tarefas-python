from dataclasses import dataclass
import json

@dataclass
class Tarefa:
    id: int
    titulo: str
    status: str

def converter(lista: list[Tarefa]):
    dados = []
    for tarefa in lista:
        dados_tarefa = {
            "id": tarefa.id,
            "titulo": tarefa.titulo,
            "status": tarefa.status
        }
        dados.append(dados_tarefa)
    return dados

def salvarTarefas(lista_tarefas: list[Tarefa]):
    conv = converter(lista_tarefas)
    with open("tarefas.json", "w") as arquivo:
        json.dump(conv, arquivo, indent=4)
        
def converterParaTarefa(dados: list[dict]) -> list[Tarefa]:
    lista_tarefas = []

    for item in dados:
        tarefa = Tarefa(
            item["id"],
            item["titulo"],
            item["status"]
        )

        lista_tarefas.append(tarefa)

    return lista_tarefas

def carregarTarefas():
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        tarefas = converterParaTarefa(dados)
    return tarefas  
    

