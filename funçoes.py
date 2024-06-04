def exibirMensagem(nome, mensagem='seja bem vindo'):
    print(f'{mensagem} {nome}')
    return f'Usuário logado: {nome}'

nome_usuario=input('digite o nome de usuario: ')
msg=input('digite uma mensagem: ')
usuario = exibirMensagem(nome_usuario, msg)
print(usuario)

print(50*'-')

nome_usuario=input('digite o nome de usuario: ')
msg=input('digite uma mensagem: ')
usuario = exibirMensagem(nome_usuario, msg)
print(usuario)
