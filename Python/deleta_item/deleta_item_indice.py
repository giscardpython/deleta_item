
nomes_cidades = ['Porto Alegre', 'Curitiba', 'Brasília', 'Águas Claras', 'São Paulo', 'Goiânia']

indice = int(input('Informe a posição do item a ser deletado: '))
# tenta excluir o nome
indice -=1

try:
    del(nomes_cidades[indice])
except:
    print('Índice não pode ser excluído.')

# exibe a nova lista
for nome in nomes_cidades:
    print(nome)
