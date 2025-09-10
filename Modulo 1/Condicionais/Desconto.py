# Cálculo de Desconto em um Produto.
# • Se o usuário informar que o preço original é 100 e o desconto é
# de 20%, o programa deverá calcular que o valor do desconto é 20
# e, consequentemente, o preço final será 80.
# • Exemplo de fórmula:
# valor_desconto = preco_original * (porcentagem_desconto / 100)
# preco_final = preco_original - valor_desconto


produto=input('digite o nome do produto:')
valor_total = float(input('digite o valor total:'))
porcentagem =float(input('digite a porcentagem de produto:'))
desconto = valor_total * (porcentagem /100)
valor_novo = valor_total - desconto
print(f'O {produto} com {porcentagem}% de desconto custará :R${valor_novo}')