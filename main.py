from models import Creat,Read,Update,Delete
from test import verificar_id,verificar_email
try:
    res = int(input(f"{'='*30}MENU DB{'='*30}\n1- novo usuário\n2- pesquisar_usuario(id)\n3- listar todos os usuários\n4- atualizar usuario(id)\n5- excluir usuario(id)"))
    resposta_requisicao = ""
    match res:
        case 1:
            nome = input("Digite o nome do novo usuário: ")
            while True:
                email = input("Digite o email do usuário: ")
                if verificar_email(email):
                    telefone = input("Digite o telefone do usuário: ")
                    criar_usuario = Creat(nome,email,telefone)
                    resposta_requisicao = criar_usuario.salvar()
                    break
                else:
                    print("Digite um email válido!")
                    continue
        case 2:
            id_ = int(input("Digite o id do usuário: "))
            buscar_usuario = Read()
            resposta_requisicao = buscar_usuario.pesquisar_unico(id_)
        case 3:
            buscar_todos = Read()
            resposta_requisicao = buscar_todos.pesquisar_todos()
        case 4:
                id_ = int(input("Digite o id do usuário: "))
                if verificar_id(id_):
                    nome = input("Digite o nome do usuário: ")
                    while True:
                        email = input("Digite o email do usuário: ")
                        if verificar_email(email):
                            telefone = input("Digite o telefone do usuário: ")
                            atualizar_dados = Update(id_, nome, email, telefone)
                            resposta_requisicao = atualizar_dados.alterar_info()
                            break
                        else:
                            print("Digite um email válido!")
                            continue
                else:
                    print("O id que você digitou não existe!")
        case 5:
                id_ = int(input("Digite o id do usuário: "))
                if verificar_id(id_):
                    deletar_dados = Delete(id_)
                    resposta_requisicao = deletar_dados.excluir()
                else:
                    print("O id que você digitou não existe, ou não é válido!")
        case _:
            print("O valor que você digitou não existe!")
    print(resposta_requisicao)
except ValueError:
    print("Valor inválido!")