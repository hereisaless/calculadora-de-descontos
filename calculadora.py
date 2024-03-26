#Mensagem de boas-vindas
print('Seja muito bem-vindo(a) ao nosso App - Alessandra de Souza Oliveira')
#Input do produto/quantidade | valor do produto(vp) | quantidade do produto(qp)
vp = float(input('Digite o valor do produto: '))
qp = int(input('Digite a quantidade de produtos: '))
#Definições dos descontos | valor total sem desconto(vtsd)
vtsd = vp * qp
if vtsd < 1000:
  desconto = 0
elif vtsd < 3000:
   desconto = 3
elif vtsd < 5000:
  desconto = 5
else:
  desconto = 8
#Cálculo do desconto e valor total com desconto | valor do desconto(vd) | valor com desconto(vcd)'
vd = (desconto / 100) * vtsd
vcd = vtsd - vd
#Mensagem padrão para compra com desconto
if vtsd > 1000:
  print(f'Você economizou {desconto}% na sua compra e teve um desconto de R${vd:.2f}!')
  print(f'Valor total SEM desconto: R${vtsd:.2f}')
  print(f'Valor total COM desconto: R${vcd:.2f}')
#Mensagem padrão para compra sem desconto
else:
     print(f'Valor total: R${vtsd:.2f}')
#Mensagem de agradecimento final
print('Agradecemos por comprar conosco, até a próxima!')