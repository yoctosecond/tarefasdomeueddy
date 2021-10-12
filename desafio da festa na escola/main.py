# Setando a variável do caixa e a quantidade de fichas como atributo.
current_balance = 1000


# Função que inicializa o sistema.
def main():
    border, space = "═══════════════════════☸☸☸═══════════════════════".center(107), (" " * 32)
    print(f"\n{border}\n{space}Uuuuuh, welcome to the jun-... cash manager!\n{border}\n{space}")
    
# Menu de controle do usuário.
    answer = input("What would you like to do? (𝙎)𝙖𝙡𝙙𝙤, (𝙍)𝙚𝙩𝙞𝙧𝙖𝙙𝙖 e (𝘿)𝙚𝙫𝙤𝙡𝙪𝙘𝙖𝙤 → ").lower()[0:1]
    verify(answer)



# Função que verifica qual opção foi digitada pelo usuário.
def verify(answer):
    global current_balance

    # Se a resposta for para ver o SALDO,
    if answer == "s":

        # Printa o saldo e executa uma função que pergunta se deseja voltar ao menu.
        print(f"Agora o caixa tem {current_balance} fichas disponíveis!")
        return_verification()

    # Se a resposta for para realizar a RETIRADA,
    elif answer == "r":

        # Verifica se o valor do caixa está apto a efetuar a transação.
        if 0 < current_balance <= 1000:

            # Chama uma função que calcula o processo.
            statement()

        # Se o caixa não estiver apto, imprime uma mensagem de que não tem ficha e retorna ao menu.
        else:
            print(" Você não tem ficha, moço!"), main()

    # Se a resposta for para realizar o DEPÓSITO,
    elif answer == "d":

        # Verifica se o total do caixa é apto a receber fichas.
        if 0 <= current_balance < 1000:

            # Chama uma função que calcula o processo.
            check_the_token_amount()

        # Senão, printa uma mensagem de que não há chance de depositar mais, retornando ao menu.
        else:
            print("Você não consegue depositar ficha, moço!"), main()
            
    # Mas se nenhuma resposta der "match", retorna um erro de argumento, voltando ao menu.
    else:
        print("Neca de pitibirida, argumento não suportado. Retry."), main()



# Função responsável pelo "extrato" das fichas.
def statement():
    global current_balance

    # Pergunta quantas fichas o usuário gostaria de receber.
    value = int(input("Quantas fichas gostaria de retirar do caixa? → "))

    # Se a quantidade de fichas está entre 0 e 1000 e o valor se adequa ao total disponível,
    if 0 <= current_balance <= 1000 and 0 <= value <= current_balance:

        # Desconta do total e exibe a mensagem de quantas fichas o caixa tem.
        current_balance = current_balance - value
        verify("s")

    # Senão, é printada uma mensagem de erro e restarta o processo.
    else:
        print("ERROR! QUANTIDADE NÃO-DISPONÍVEL!"), verify("r")



# Função que pergunta se gostaria de retornar ao menu de controle.
def return_verification():
    second_answer = input("Gostaria de retornar? (𝙎)𝙞𝙢 ou (𝙉)𝙖𝙤 → ").lower()[0:1]

# Caso a resposta seja sim, ele retorna ao menu. Senão, encerra o processo com uma mensagem bonita.
    main() if second_answer == "s" else print("Baibai") # Operador ternário

# Função que verifica a quantidade de fichas para depositar.
def check_the_token_amount():
    value = int(input("Quantas fichas gostaria de depositar? → "))
    
    # Se o total de fichas for de 0 até 1000 e se somado ao caixa dá 1000,
    if 0 <= value <= 1000 and value + current_balance <= 1000:
        
        # Executa a função que registra a transação.
        return_token_to_the_balance(value)
    
    # Do contrário, exibe uma mensagem de erro e restarta o sistema de depósito.
    else:
        print("Quantidade não disponível, moço!")
        verify("d")



# Função que retorna o valor de fichas ao caixa.
def return_token_to_the_balance(tokenamount):
    global current_balance
    
    # Adiciona a quantidade de fichas ao caixa e retorna o saldo.
    current_balance = current_balance + tokenamount
    verify("s")


main()
