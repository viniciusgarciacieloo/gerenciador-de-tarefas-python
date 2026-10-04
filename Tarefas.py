from dataclasses import dataclass
import json

@dataclass
class Tarefa:
    id: int
    titulo: str
    status: str 
    
def main():
    lista_tarefas = carregarTarefas()
    
    opcao = -1
    while opcao != 5:
        print("=" * 30)
        print("             TAREFAS             ")
        print("[1] Adicionar Tarefa ")
        print("[2] Listar Tarefas ")
        print("[3] Concluir Tarefa ")
        print("[4] Remover Tarefa ")
        print("[5] Sair ")
        print("=" * 30)
        
        try:
            opcao = int(input("Digita a opção que deseja realizar: "))
        except ValueError:
            print("Digite apenas os valores indicados! ")
            
        if opcao == 1:
            titulo = input("Digite a tarefa que deseja adicionar: ")
            novo_id = gerarID(lista_tarefas)
            status = "Pendente"
            nova_tarefa = Tarefa(novo_id, titulo, status)
            adicionarTarefa(lista_tarefas, nova_tarefa)
            salvarTarefas(lista_tarefas)
        elif opcao == 2:
            listarTarefas(lista_tarefas)
        
        elif opcao == 3:
            id_desejado = int(input("Digite o ID que deseja concluir: "))
            concluirTarefa(lista_tarefas, id_desejado)
            salvarTarefas(lista_tarefas)
        
        elif opcao == 4:
            id_remover = int(input("Digite o ID da tarefa que deseja remover: "))
            removerTarefa(lista_tarefas, id_remover)
            salvarTarefas(lista_tarefas)
            
        elif opcao == 5:
            print("Programa encerrado! ")
        
        else:
            print("Valor inválido! ")
             
#region AUXILIAR 
def existeTarefa(lista_tarefas: list[Tarefa], novaTarefa: Tarefa)-> bool:

    '''retorna False caso a tarefa seja a mesma, evitando duplicatas'''
    
    for i in range(len(lista_tarefas)):
        if lista_tarefas[i].titulo == novaTarefa.titulo:
            return True
    return False

def gerarID(lista_tarefas: list[Tarefa]):
    maior_id = 1
    if not lista_tarefas:
        return 1
        
    for tarefa in lista_tarefas:
        if tarefa.id >= maior_id:
            maior_id = tarefa.id                 
    
    return maior_id + 1

#end region

#region CRUD       
def adicionarTarefa(lista_tarefas: list[Tarefa], novaTarefa: Tarefa) -> None:
    if existeTarefa(lista_tarefas, novaTarefa) == True:
        print("Essa tarefa ja existe")
    else:
        lista_tarefas.append(novaTarefa)
        print("Tarefa adiciona com sucesso! ")
        
def listarTarefas(lista_tarefas:list[Tarefa]):
    if lista_tarefas == []: #if not lista_tarefa: (é a mesma coisa e melhor desse jeito)
        print("Nunhuma tarefa por aqui")
        
    for tarefa in lista_tarefas:
        print(f" ID: {tarefa.id}\n Título: {tarefa.titulo}\n Status: {tarefa.status}\n")
   
def concluirTarefa(lista_tarefas: list[Tarefa], id_tarefa: int):
    
    for i in range(len(lista_tarefas)):
        if lista_tarefas[i].id == id_tarefa:
            lista_tarefas[i].status =  "Concluído"
            print("Tarefa concluída com sucesso! ")
            return  
        
    print("Tarefa não foi não encontrada/concluida ")
    return 

               
def removerTarefa(lista_tarefas: list[Tarefa], id_tarefa: int):
    
    for tarefa in lista_tarefas:
        if tarefa.id == id_tarefa:
            lista_tarefas.remove(tarefa)
            print("Tarefa removida com sucesso! ")
            return
        
    print ("Tarefa não encontrada ou ja foi removida/realizada! ")
    return
#end region

#region JSON
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
    try:
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        return converterParaTarefa(dados)

    except FileNotFoundError:
        return []
    
#end region

if __name__ == '__main__':
    main()
    