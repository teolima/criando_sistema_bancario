menu = """
digite uma das opcões:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("digite o valor do deposito"))
        
        if valor > 0:
             saldo += valor
             print(f"Depósito efetuado com sucesso.")
        else:
            print("Erro digite um valor valido")
    if opcao == "s":
        valor = float(input("digite o valor para sacar:"))
        if valor > saldo:
            print("Saldo insuficiente para saque ")   
        else:
            
            if valor > limite:
                print("valor do saque é maior do que  o limite ")
            elif numero_saques >= LIMITE_SAQUES:
                print("Erro, número ultrapassou  o limite diario de saques")

            elif valor > 0:
                saldo -= valor
                numero_saques += 1
    if opcao == "e":
        print("\n############ EXTRATO ################")
        print(f"Saldo final R$: {saldo}")         
    if opcao == "q":
         break          
   
  
        