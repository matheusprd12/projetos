#login

def login():
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

    if usuario == 'Luis' and senha == "12345":
        print("Acesso permitido")
    else:
        print("Acesso negado, usuario ou senha incorreto")

while True:
    if login():
        break