
## Operação de Depósito
#Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário,
#dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos
#devem ser armazenados em uma variável e exibidos na operação de extrato.

## Operação de Saque
#O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha
#saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de
#saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

## Operação de Extrato
#Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o
#saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
#Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:1500.45 = R$ 1500.45

menu = "1-Extrato 2-Saque 3-Depósito 4-Sair\n"
opcao=0
saldo=0
historico=""
LIMITE_DIARIO=500
QTD_LIMITE=3



while opcao!=4:        
    entrada=0
    try:
        opcao=int(input(menu))
        if opcao==1:
            if historico=="":
                print("Não foram realizadas movimentações")
            else:
                print(f"{historico}") 
                print(f"Saldo atual:R$ {saldo:.2f}")                                
            
        if opcao==2:
            entrada=float(input("Informe valor do saque\n"))
            if entrada >LIMITE_DIARIO:
                print(f'Valor de R$ {entrada} ultrapassou o limite diário')
            elif QTD_LIMITE==0:
                print("Você excedeu o limite de saques!")
            elif entrada>saldo:
                print(f"Saque inferior ao saldo disponível")    
            else:
                QTD_LIMITE-=1
                saldo-=entrada
                historico+=(f"Saque no valor de R$ {entrada:.2f}\n")   


        if opcao==3:            
            entrada=float(input("Informe o valor\n"))
            saldo+=entrada
            historico+=(f"Depósito no valor de R$ {entrada:.2f}\n")   
            

    except ValueError:
        print('Entrada inválida! Tente novamente\n')
