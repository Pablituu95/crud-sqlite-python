import secrets
from db import criar_db
class Creat:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = secrets.token_hex(16)
    def salvar(self):
        try:
            with criar_db() as db:
                cur = db.cursor()
                cur.execute("INSERT INTO usuarios('nome','email','numero','senha')VALUES (?,?,?,?)",(self.nome,self.email,self.telefone,self.senha))
                db.commit()
                return 'usuario criado com sucesso!'
        except Exception as e:
            if 'usuarios.nome' in str(e):
                return 'O nome que você digitou já está sendo utilizado!'
            elif 'usuarios.email' in str(e):
                return 'O email que você digitou já está sendo utilizado!'
            elif 'usuarios.numero' in str(e):
                return 'O telefone que você digitou já esta sendo utilizado!'
            else:
                return f'não foi possível criar o usuário erro: {e}'
class Read:
    def __init__(self):
        pass
    def pesquisar_unico(self,id_):
        with criar_db() as db:
            cur = db.cursor()
            cur.execute("SELECT * FROM usuarios WHERE id = ?",(id_,))
            usuario = cur.fetchone()
            if usuario:
                return usuario
            else:
                return 'nenhum usuário com esse id!'
    def pesquisar_todos(self):
        with criar_db() as db:
            cur = db.cursor()
            cur.execute("SELECT * FROM usuarios")
            usuarios = cur.fetchall()
            if usuarios:
                return usuarios
            else:
                return 'nenhum usuario criado ainda!'

class Update:
    def __init__(self,id_,nome,email,telefone):
        self.id = id_
        self.nome = nome
        self.email = email
        self.telefone = telefone
    def alterar_info(self,):
        try:
            with criar_db() as db:
                cur = db.cursor()
                cur.execute("UPDATE usuarios SET nome = ?, email = ?, numero = ? WHERE id = ?", (self.nome,self.email,self.telefone,self.id))
                db.commit()
                return 'usuario atualizado com sucesso!'
        except Exception as e:
            if 'usuarios.nome' in str(e):
                return 'O nome que você digitou já existe!'
            elif 'usuarios.email' in str(e):
                return 'O email que você digitou já existe!'
            elif 'usuarios.numero' in str(e):
                return 'O telefone que você digitou já existe!'
            else:
                return f'não foi possível atualizar o usuário, ERRO: {e}'

class Delete:
    def __init__(self,id_):
        self.id = id_
    def excluir(self):
        try:
            with criar_db() as db:
                cur = db.cursor()
                cur.execute("DELETE FROM usuarios WHERE id = ?",(self.id,))
                db.commit()
                return 'usuario excluido com sucesso!'
        except Exception as e:
            return f'não foi possível excluir o usuário, ERRO: {e}'