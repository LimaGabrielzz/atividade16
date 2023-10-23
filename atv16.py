# Exercício Python 16: Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou cadeirante. 
# Escreva um programa que pergunta a situação do usuário 
# (se é idoso, se é gestante, se é cadeirante ou nenhum destes) 
# e diga se ele pode ter acesso a fila prioridade ou não.
situacao = str(input("Voce é gestante, idoso, cadeirante ou nenhum? \n Digite 'idoso', 'gestante', 'cadeirante' ou 'nenhum: "))
if situacao == 'idoso' or situacao == 'gestante' or situacao == 'cadeirante':
    print("Voce tem acesso a fila de prioridade")
else:
    print("Voce nao tem acesso a fila de prioridade")