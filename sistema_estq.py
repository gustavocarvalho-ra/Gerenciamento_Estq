produtos = []

def menu() :
  print('''
    Menu:
    
    [1] - Adicionar produto
    [2] - Atualizar produto
    [3] - Vizualizar estoque
    [4] - Sair
  ''')
  return str(input('Digite a opição desejada: '))

def master():
  opicao_desejada = menu()
  while opicao_desejada != '4':
    if (opicao_desejada == '1'):
      produto = {}
      nome_produto = str(input('Nome do produto a adicionar: '))
      preco_produto = str(input('Preço do produto: '))
      quantidade_produto = str(input('Quantidade a adicionar: '))
      produto = {'nome':nome_produto, 'preco':preco_produto, 'quantidade':quantidade_produto}
      produtos.append(produto)
      print('Produto adicionado com êxito!')
      opicao_desejada = menu()
    elif (opicao_desejada == '2'):
      nome_Aatualizar = str(input('Informe o nome do produto a atualizar: '))
      atualizar = 0
      for a in produtos:
        if a['nome'] == nome_Aatualizar:
          preco_novo = str(input('Informe o novo Preço a ser alterado: '))
          quantidade_nova = str(input('Informe o nova quantidade em estoque: '))
          a['preco'] = preco_novo
          a['quantidade'] = quantidade_nova
          atualizar = 1
      if atualizar == 1:
        print('Produto atualizado com êxito!')


master()