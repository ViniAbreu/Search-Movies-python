import requests
import json

print("+==================================+")
print("|      Biggs-s34arch-m0v13s        |")
print("+==================================+")
print("|       Coded By: SrBiggs          |")
print("|       Contact: @SrBiggs          |")
print("|       Versao: 1.0                |")
print("+==================================+\n")

def requesicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?t=' + op + '&type=movie')
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print("Erro de conexão!")
        return None

def printar_detalhes(filme):
    print("\n<<< Informações do filme >>>\n")
    print("Titulo: " + filme['Title'])
    print("Ano: " + filme['Year'])
    print("Diretor: " + filme['Director'])
    print("Atores: " + filme['Actors'])
    print("Nota: " + filme['imdbRating'])
    print("Prêmios: " + filme['Awards'])
    print("Poster: " + filme['Poster'])
    print('')


sair = False
while not sair:
    op =str(input("Digite o nome de um filme ou Sair para fechar: "))

    if op == 'Sair':
        sair = True
        print("Saindo......")
    else:
        filme = requesicao(op)
        if filme['Response'] == 'False':
            print('Filme não encontrado!\n')
        else:
            printar_detalhes(filme)
