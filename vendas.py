#Loja do Aleksandro Bruno Gouvêa

from datetime import datetime

def obter_limite():
    global idade
    global dono
    ano_atual = datetime.today().year
    dono = 'Aleksandro Bruno Gouvea'
    print('Prezado cliente, bem-vindo à Loja do',dono)
    print('------------------------------------------------------------')
    print('Faremos uma análise de crédito:')
    print('')
    cargo = str(input('Digite o cargo na empresa em que trabalha: '))
    salario = float(input('Digite o seu salário mensal atual: '))
    data_nasc = str(input('Digite a sua data de nascimento (formato dd/mm/aaaa): '))
    ano_nasc = int(data_nasc.split("/")[2])
    while (1880 > ano_nasc) or (ano_nasc > 2021): #validador de idade
        print('Data de nascimento inválida')
        data_nasc = str(input('Digite a sua data de nascimento (formato dd/mm/aaaa): '))
        ano_nasc = int(data_nasc.split("/")[2])
    print('O seu cargo atualmente é',cargo)
    print('O seu salário mensal é R$ %.2f' % salario)
    print('Seu ano de nascimento é',ano_nasc)
    idade = ano_atual-ano_nasc
    print('A sua idade é aproximadamente',idade,'anos')
    limite = salario*(idade/1000)+100
    print('O seu limite disponível para compras na loja é de R$ %.2f' % limite)
    return limite

def verificar_produto(limite):
    global preco_final    
    produto = str(input('Digite o nome do produto que deseja: '))
    preco = float(input('Digite o valor do produto '+produto+': '))
    desconto = float(len(dono.split()[0]))
    bloqueado = 'N'
    if preco <= (0.6*limite):
        print('Liberado')
    elif preco < (0.9*limite):
        print('Liberado ao parcelar em 2 vezes')
    elif preco < limite:
        print('Liberado ao parcelar em 3 ou mais vezes')
    else:
        print('Bloqueado, valor do item é maior que o limite disponível')
        bloqueado = 'S'
        preco_final = 0
    if bloqueado == 'N':
        if (len(dono) > preco > idade) or (len(dono) < preco < idade):
            print('Neste item, você tem direito a um desconto especial do Aleksandro de R$ %.2f' % desconto)
            preco_final = preco - desconto
            print('Com o desconto, o produto %s fica com valor de R$ %.2f' % (produto,preco_final))
        else:
            print('Sem desconto. O produto %s possui valor de R$ %.2f' % (produto,preco))
            preco_final = preco
    return preco_final

limite = obter_limite()
print('------------------------------------------------------------')
print('Carrinho de compras:')
print('')
limite_orig = limite
qntd_produtos = int(input('Digite a quantidade de produtos que deseja cadastrar para compra: ' ))
total = 0
for p in range(qntd_produtos):
    verificar_produto(limite)
    total += preco_final
    limite -= preco_final
    print('Seu limite atualizado é de: R$ %.2f' % limite)
    print('')
print('------------------------------------------------------------')
if total <= 0: #todos bloqueados ou zero produtos
    print('Compra não realizada')
else:
    input('Pressione qualquer tecla para para ir para etapa de pagamento')
    print('Caixa - Finalização da sua compra:')
    print('')
    print('Compra autorizada, valor total ficou em R$ %.2f\nResta um limite de R$ %.2f' % (total,limite))
    if total > (0.6*limite_orig) and total < (0.9*limite_orig):
        print('Lembrando que será necessário parcelar em 2 vezes')
        total_parc = total/2
        print('Serão 2 parcelas de: R$ %.2f' % total_parc)
    elif total > (0.9*limite_orig):
        print('Lembrando que será necessário parcelar em 3 ou mais vezes')
        parcelas = int(input('Digite em quantas vezes deseja parcelar (3 a 12): '))
        while (parcelas < 3) or (parcelas > 12):
            print('Número de parcelas escolhido não é aceito')
            parcelas = int(input('Digite o número de parcelas que deseja (3 a 12): '))
        total_parc = total/parcelas
        print('Serão',parcelas,'parcelas de: R$ %.2f' % total_parc)
    else:
        print('Sua compra foi liberada em pagamento direto')
    print('------------------------------------------------------------')
    input('Pressione qualquer tecla para para concluir a compra')
    input('Compra concluída\nPressione qualquer tecla para sair... e volte sempre!')
    
    
