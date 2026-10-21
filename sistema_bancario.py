# OK -Operações de saque, depósito, extrato e sair
# OK - saque e depósito precisam ser valores positivos
# OK - saque menor ou igual ao limite diário e ao saldo
# OK - limite de 3 saques diários de R$500 cada
# OK - mensagem de erro caso o saque seja maior que o limite diário ou saldo
# OK -Transações registradas no extrato
# OK - Registrar datas das transações
# OK - Voltar ao menu principal após cada operação
# OK - mensagem de erro caso o usuário digite uma opção inválida
# OK - Mensagem de erro caso o usuário não digite um número inteiro para saque ou depoósito

# Permitir o usuário alternar entre as opções usando as setas do teclado

# Perguntar o número da conta
# Pedir para digitar a senha
# Conferir se a senha está correta
# Caso esteja correta, buscar o nome do cliente, saldo, número de saques disponíveis e extrato salvos
# Zerar o limite de saques de todos os clientes ao final do dia
# OK - Se valor de saque ou depósito for inváido, repetir a operação

from datetime import datetime

saldo = 1000
limite_saques = 3
limite_por_saque = 500
historico_de_movimentacoes = [("Horário","Tipo de operação","Valor","Saldo após a movimentação")]
saldo_inicial = saldo

while True:
    opcao = input("Digite a letra correspondente à opção desejada \nS - SAQUE\nD - DEPÓSITO\nE - EXTRATO\nQ - SAIR\n\n" ).upper()
    if opcao == "S":
        if limite_saques >= 1:
            print(f"Seu saldo atual é de R${saldo:.2f}")
            while True:
                try:
                    valor_saque = float(input("Quanto deseja sacar?"))
                    if valor_saque >= 0:
                        if valor_saque <= saldo and valor_saque <= limite_por_saque:                
                            saldo -= valor_saque
                            print(f"Seu novo saldo é R${saldo:.2f}")
                            if valor_saque > 0:
                                limite_saques -= 1
                                horario = datetime.now().strftime("%H:%M:%S")
                                nova_movimentacao = (horario,"Saque",-valor_saque,saldo)  
                                historico_de_movimentacoes.append(nova_movimentacao)                            
                            if limite_saques > 0:
                                print(f"Você ainda tem {limite_saques} saques")
                            else:
                                print("Você não tem mais saques disponíveis")
                            break
                        elif saldo <= limite_por_saque:
                            print(f"Saldo insuficiente. Seu saldo é de R${saldo:.2f}")
                        else:
                            print(f"O limite por saque é R${limite_por_saque:.2f}")    
                    else:
                        print("Digite um valor maior ou igual a que zero")
                except ValueError:
                    print("Valor inválido")
        else:
            print("Você não tem mais saques disponíveis")
    elif opcao == "D":
        while True:
            try:
                valor_deposito = float(input("Quanto deseja depositar?"))
                if valor_deposito > 0:
                    saldo += valor_deposito
                    print(f"Seu novo saldo é R${saldo:.2f}")
                    horario = datetime.now().strftime("%H:%M:%S")
                    nova_movimentacao = (horario,"Depósito",valor_deposito,saldo)
                    historico_de_movimentacoes.append(nova_movimentacao)
                    break
                elif valor_deposito == 0:
                    break
                else:
                    print("Digite um valor maior ou igual a que zero")
            except ValueError:
                print("Valor inválido")
    elif opcao == "E":
        print("\nSeu extrato de movimentações é:")
        print(f"\nSaldo inicial: R${saldo_inicial}\n")
        cabecalho = historico_de_movimentacoes[0]
        print(f"{cabecalho[0]:<10} | {cabecalho[1]:<20} | {cabecalho[2]:<8} | {cabecalho[3]}")
        print("-" * 75)
        for hora, tipo, valor, saldo in historico_de_movimentacoes[1:]:
            saldo_com_moeda = f"R$ {saldo:,.2f}"
            print(f"{hora:<10} | {tipo:<20} | {valor:<+8.2f} | {saldo_com_moeda:<8}")
        print()
    elif opcao == "Q":
        break
    else:
        print("\nOpção inválida")
    print()





