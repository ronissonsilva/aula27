#Ler entradas do usuario.
cont = 0 #variavel que controla a repetição.
escolha_usuario = int (input())#variavel que guarda quantas vezes o codigo vai rodar.7
alunos = []#lista que armazena a quantidade de alunos cadastrados
while cont < escolha_usuario:
    nome = input() #Armazenar o nome do aluno.
    Nota1 = float(input("Digite a primeira nota:"))#4 notas do aluno.
    Nota2 = float(input("Digite a segunda nota:"))
    Nota3 = float(input("Digite a erceira nota"))
    Nota4 = float(input("Digite a quarta nota:"))

    faltas = int(input("Digite as faltas:"))
    #Calculo da media 
    Media = (Nota1+Nota2+Nota3+Nota4)/4
    print(Media)
    #Logica da Situação.
    if faltas > 31:
        situacao = "Reprovado por falta"
    elif Media >= 8:
        situacao = "aprovado"
    elif Media >= 5: #Recuperação.
        recuperacao = float(input()) # ler a nota da prova de recuperação.
        if recuperacao >= (10-Media):
            situacao = "Aprovado na recuperação"
        else:
            situacao = "Reprovado na recuperação"
    else:
        situacao = "Reprovado por media"
    #enviar os dados do aluno para a lista alunos 
    alunos.append([nome,faltas,Media,situacao,])
    cont =+1
    #relatorio
print(alunos)
