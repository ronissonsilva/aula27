#cadrasto de usuário e senha
#saldo = 0.0 #variavel que guarda o saldo do usuario 
while True:
    #menu principal
    print("bem vindo! \n digite 1.cadastrar 2.login 3. ecerrar")
    #ler a escolha do usuário
    escolha_menu = int(input()) #lê a escolha como um número

    #se usuário escolher cadastro
    if escolha_menu == 1:
        #crie um usuário e uma senha com tipo string
        usuario = input("crie um nome de usuário")
        senha = input("crie uma senha")
    elif escolha_menu == 2: #se usuário escolher login
        #comparar as inf. cadastradas com uma leitura 
        login_usuario = input("digite seu usuário")
        login_senha = input("digite sua senha")
        if login_usuario == usuario and login_senha == senha:  
            print("LOGIN REALIZADO COM SUCESSO")
            #SE LOGIN CORRETO, ENTRA NO
            #MENU PRINCIPAL DO APP 
            print("bem vindo", usuario)
            while True: #ENQUANTO QUE EXIBIRÁ O MENU PRINCIPAL
                print("1. deposito 2. sacar 3. extrato 4.encerrar")
                escolha_principal = int(input())
                if escolha_principal == 1: #se usuário escolher depositar
                    #LÊ O VALOR A SER DEPOSITADO
                    valor_deposito = float(input())
                    saldo = saldo + valor_deposito #ATUALIZA O VALOR 
                elif escolha_principal == 2: #saque
                    valor_saque == float(input("digite o valor do saque "))
                    print("NOVO SALDO É ", saldo)
        else:
            print("USUÁRIO OU SENHA INCORRETOS")                                                                                                                                                                                                                                                                                                                                                                      '
