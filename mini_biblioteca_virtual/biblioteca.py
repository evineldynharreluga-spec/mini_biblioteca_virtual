import functions, livros


functions.menu()

opcao = int(input('Escolha uma opcao: '))
if opcao == 1:
    functions.ver_livros_disponiveis()
if opcao == 4:
    nome_livro = str(input('Digite o nome do livro: '))
    for livro in livros.livros:
        livro.get(functions.procurar_livro(nome_livro))
    print(livro)
    