
nomes_cidades = ['Porto Alegre', 'Curitiba', 'Brasília', 'Águas Claras', 'São Paulo', 'Goiânia']

nome_a_excluir = input('Informe o nome que deseja retirar da lista: ')
# tenta excluir o nome

try:
    nomes_cidades.remove(nome_a_excluir)
except:
    print('Nome não pode ser excluído.')

# exibe a nova lista
for nome in nomes_cidades:
    print(nome)
