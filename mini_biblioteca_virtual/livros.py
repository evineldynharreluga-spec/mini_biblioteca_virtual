from statistics import mean, median

livros = [
    {
        "titulo": "Sombras do Amanhã",
        "autor": "Carlos Mendes",
        "ano_publicacao": 2015,
        "genero": "Ficção científica",
        "preco": 1800.00,
        "rating": 4.5
    },
    {
        "titulo": "O Código Esquecido",
        "autor": "Ana Ribeiro",
        "ano_publicacao": 2018,
        "genero": "Mistério",
        "preco": 2200.00,
        "rating": 4.2
    },
    {
        "titulo": "Além das Estrelas",
        "autor": "Pedro Alves",
        "ano_publicacao": 2020,
        "genero": "Fantasia",
        "preco": 3500.00,
        "rating": 4.8
    },
    {
        "titulo": "Python para Iniciantes",
        "autor": "Mariana Costa",
        "ano_publicacao": 2022,
        "genero": "Programação",
        "preco": 4800.00,
        "rating": 4.7
    },
    {
        "titulo": "A Última Fronteira",
        "autor": "Rui Martins",
        "ano_publicacao": 2016,
        "genero": "Aventura",
        "preco": 1600.00,
        "rating": 4.1
    },
    {
        "titulo": "Segredos da Mente",
        "autor": "Sofia Rocha",
        "ano_publicacao": 2019,
        "genero": "Psicologia",
        "preco": 2900.00,
        "rating": 4.4
    },
    {
        "titulo": "Ecos do Passado",
        "autor": "João Ferreira",
        "ano_publicacao": 2014,
        "genero": "Drama",
        "preco": 1400.00,
        "rating": 3.9
    },
    {
        "titulo": "Algoritmos Essenciais",
        "autor": "Luís Teixeira",
        "ano_publicacao": 2021,
        "genero": "Tecnologia",
        "preco": 5000.00,
        "rating": 4.9
    },
    {
        "titulo": "Caminhos da História",
        "autor": "Helena Duarte",
        "ano_publicacao": 2013,
        "genero": "História",
        "preco": 2100.00,
        "rating": 4.0
    },
    {
        "titulo": "O Jardim Secreto",
        "autor": "Beatriz Nunes",
        "ano_publicacao": 2017,
        "genero": "Romance",
        "preco": 1750.00,
        "rating": 4.3
    },
    {
        "titulo": "Viagem ao Desconhecido",
        "autor": "Miguel Pires",
        "ano_publicacao": 2015,
        "genero": "Ficção científica",
        "preco": 2600.00,
        "rating": 4.2
    },
    {
        "titulo": "Arte Moderna Explicada",
        "autor": "Carla Batista",
        "ano_publicacao": 2020,
        "genero": "Arte",
        "preco": 3200.00,
        "rating": 4.1
    },
    {
        "titulo": "O Mestre do Jogo",
        "autor": "André Lopes",
        "ano_publicacao": 2018,
        "genero": "Suspense",
        "preco": 3700.00,
        "rating": 4.6
    },
    {
        "titulo": "Sabores do Mundo",
        "autor": "Patrícia Gomes",
        "ano_publicacao": 2021,
        "genero": "Culinária",
        "preco": 2400.00,
        "rating": 4.3
    },
    {
        "titulo": "Fundamentos de Matemática",
        "autor": "Ricardo Sousa",
        "ano_publicacao": 2012,
        "genero": "Educação",
        "preco": 4100.00,
        "rating": 4.5
    },
    {
        "titulo": "A Cidade Perdida",
        "autor": "Daniel Carvalho",
        "ano_publicacao": 2016,
        "genero": "Aventura",
        "preco": 1950.00,
        "rating": 4.0
    },
    {
        "titulo": "Despertar Interior",
        "autor": "Laura Freitas",
        "ano_publicacao": 2019,
        "genero": "Desenvolvimento pessoal",
        "preco": 2800.00,
        "rating": 4.4
    },
    {
        "titulo": "Redes de Computadores Modernas",
        "autor": "Tiago Barros",
        "ano_publicacao": 2023,
        "genero": "Tecnologia",
        "preco": 4700.00,
        "rating": 4.8
    },
    {
        "titulo": "Mistérios do Oceano",
        "autor": "Fernanda Melo",
        "ano_publicacao": 2017,
        "genero": "Ciência",
        "preco": 2300.00,
        "rating": 4.1
    },
    {
        "titulo": "O Guardião das Lendas",
        "autor": "Bruno Azevedo",
        "ano_publicacao": 2020,
        "genero": "Fantasia",
        "preco": 3600.00,
        "rating": 4.7
    }
]

precos = []
rating = []
for livro in livros:
    rating.append(livro.get('rating'))
    precos.append(livro['preco'])

print(livros[precos.index(min(precos))])

print(rating)









