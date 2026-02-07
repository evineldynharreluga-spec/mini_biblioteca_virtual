import livros

def menu():
    linha()
    print('\tBIBLIOTECA VIRTUAL\t')
    linha()
    print('[1] Ver livros disponiveis')
    print('[2] Adicionar livro ao carrinho')
    print('[3] Ver livros lidos')
    print('[4] Procurar livro por titulo')
    linha()

def linha():
    print('-'*30)

def ver_livros_disponiveis():
    print(livros.livros)

def procurar_livro(livro_desejado):
    return livro_desejado
    



    






