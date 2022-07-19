########################PROJETO DB#########################################

from ast import Return, While
import mysql.connector
from numpy import true_divide
from datetime import date
from datetime import datetime

conexao = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="smartlist"
)


###################  COMANDOS PARA UTILZIACAO  #############################
#cursor = conexao.cursor() #indicador de inicio de conexao
#comando =''
#cursor.execute(comando)
#conexao.commit() # Utilizar quando edita (Updade ou Delete) o BD
# resultado = cursor.fetchall() # utilziar apra leitura do BD
#cursor.close()
#conexao.close() #indicador de finalziacao de conexao


cursor = conexao.cursor() #indicador de inicio de conexao

Appinit = True
init = True




print("\n###################### Ola, Bem vindo ao SmartList ################################## \n ")
while init == True:
  print("###################### Digite Seus Dados para Iniciar ################################## \n\n ")
  Nome = input ("Digite seu Nome :  ")
  Cpf = input ("Digite seu CPF :   ")
  Cell = input ("Digite seu Celular:   ")
  Email = input ("Digite seu Email:   ")
  Endereco = input ("Digite seu Endereco:  ")
  comando1 = f'INSERT INTO Users (name, cpf, phone, mail, location) VALUES ("{Nome}", "{Cpf}", "{Cell}", "{Email}", "{Endereco}")'

  print("\n ###################### Otimo!!! Ola ", Nome, "Agora preciso que Digite onde esta realizando suas compras? ################################## \n\n ")

  NomeStore = input ("Digite seu Nome da Loja :  ")
  EnderecoStore = input ("Digite o Endereco da Loja:  ")
  CustoStore = input ("Digite o Custo de Deslocamento:   ")
  comando2 = f'INSERT INTO Store (name, location, comutecost) VALUES ("{NomeStore}", "{EnderecoStore}", "{CustoStore}")'

  print("###################### Tudo certo!!!", Nome ,"vamos as ompras no ", NomeStore ," ################################## \n\n ")
  Confirmar = input ("Se seus dados estiverem corretos digite:\n 1.Continuar \n 2.Retornar \n 3.Finalizar \n\n :")
  if Confirmar == "1":
    init = False
      #Executando Commit
    cursor.execute(comando1)
    conexao.commit() # Utilizar quando edita (Updade ou Delete) o BD
    cursor.execute(comando2)
    conexao.commit() # Utilizar quando edita (Updade ou Delete) o BD
  
    while Appinit == True: # Dando Prosseguimento a aplicacao
      print("############################ Maos a obra! ############################# \n ")
      print("############## Selecione a opcoes que deseja Executar ################# \n ")
      opcao = input ("\n 1 = Iniciar nova lista \n 2 = Consultar Cadastros \n 3 = Sair da Aplicacao \n : ")

      if opcao == "1": # OPCAO DE INICIO DE LISTA     
        Idlista = input ("Digite o numero da sua lista:   ")
        comando = f'INSERT INTO Cart_Plist (Cp_id) VALUES ({Idlista})'
        cursor.execute(comando)
        conexao.commit() # Utilizar quando edita (Updade ou Delete) o BD
        Valor = 0
        cont = 0
        Mult=0
        Mult2=0
        Ranterior =0
        Qanterior=0
        Linit = True
        
        print("############################ Vamos inciar ############################# \n ")

        while Linit == True:
          print("###################################### Sua lista:",Idlista,"###########################################\n ")
          print("##########################   Descricao   / Valor  /  Quantidade   #####################################\n ")
          consulta = f'SELECT p.description, p.unitvaluer, p.amount, l.Cp_id FROM Product p JOIN Cart_Plist l WHERE l.cp_id = ({Idlista}) order by p.description'
          cursor.execute(consulta)
          resultado = cursor.fetchall() # utilziar apra leitura do BD
          print(resultado, "\n")
          Total = Ranterior - Mult
          TotalItens = Qanterior - Mult2
          print("######################################## Resumo ########################################### \n ")
          print("########################### Total R$:",Total, "Quantidade de Itens:",TotalItens," ########################## \n")
          print("############################ Adicione um Produto a sua lista  ############################# \n ")
          Descricao = input ("Digite o Nome do Produto :  ")
          Marca = input ("Digite a Marca se Necessario :   ")
          Codigo = (input ("Digite o Codigo do Produto caso necessario:   "))
          Valor = float(input ("Digite o valor Unitario do Produto:   "))
          Unidade = input ("Digite a Medida do Produto:  ")
          Quantidade = float(input ("Digite a Quantidade:  "))
          comando4 = f'INSERT INTO Product (description, label, getin, unitvaluer, unit, amount) VALUES ("{Descricao}", "{Marca}", "{Codigo}", {Valor}, "{Unidade}", {Quantidade})'
          
          print("############################ Deseja adiconar outro produto?  ############################# \n ")
          Confirmar2 = input ("Digite (1 para adicionar outro produto) (2 para retornar) ou (0 para finalizar) \n\n :")
          if Confirmar2 == "1":
            Linit = True 
            Mult=0
            Ranterior = Total + Quantidade*Valor
            Qanterior = TotalItens + Quantidade
            cursor.execute(comando4)
            conexao.commit() # Utilizar quando edita (Updade ou Delete) o BD
          elif Confirmar2 == "2":
            Linit = True
            i=0
            Mult = Quantidade*Valor
            Mult2 = Quantidade
          else:
            Linit = False
            cursor.execute(comando4)
            conexao.commit() # Utilizar quando edita (Updade ou Delete) o BD
            Total = Total + Quantidade*Valor
            TotalItens = TotalItens + Quantidade        
            consulta = f'SELECT p.description, p.unitvaluer, p.amount, l.Cp_id FROM Product p JOIN Cart_Plist l WHERE l.cp_id = ({Idlista}) order by p.description'  # DEMOSTRANDO A LISTA!!! VERIFICAR COMO MOSTRA SO A DO ID ESPECIFICO DA COMPRA
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            print(resultado, "\n")
            

            #Atualizando carrinho de comrpas na DB
            data_e_hora_atuais = datetime.now()
            data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
            print("######################################## Resumo da lista:",Idlista," ########################################### \n ")
            print("#################### Total R$:",Total, "Quantidade de Itens:",TotalItens," ################ \n")
            comando = f'INSERT INTO Cart (Cartdate, totalvaluer, totalamount) VALUES ("{data_e_hora_em_texto}",{Total},{TotalItens})'
            cursor.execute(comando)
            conexao.commit() # Utilizar quando edita (Updade ou Delete) o BD
            
            print("#################### Como voce Avalia essa compra? ################ \n")
            Comentario = input ("Comente algo sobre sua lista OU DEIXE EM BRANCO :  ")
            Avaliacao = input ("Avalie sua lista de 1 a 10 OU DEIXE EM BRANCO:  ")
            comandoeva = f'INSERT INTO Evaluation (description, rate) VALUES ("{Comentario}","{Avaliacao}")'
            cursor.execute(comandoeva)
            conexao.commit() # Utilizar quando edita (Updade ou Delete) o BD
      elif opcao == "2": # OPCAO DE  CONSULTA DE BANCO
        Cinit = True
        while Cinit == True:
          print("#################### Voce selecionou a opcao de consulta#################### \n")
          print("\n ##############digite a opcao que deseja consultar#############################")
          copcao = input ("\n 1.Usuario \n 2.Lojas \n 3.Produtos \n 4.Listas \n 5.Avaliacoes \n :")
          if copcao == "1":
            consulta = f'SELECT * FROM Users'
            cursor.execute(consulta)
            resultado = cursor.fetchall() # utilziar apra leitura do BD
            print(resultado)
          
          elif copcao == "2":
            consulta = f'SELECT * FROM Store GROUP BY name ORDER BY name'
            cursor.execute(consulta)
            resultado = cursor.fetchall() # utilziar apra leitura do BD
            print("################################ RESUMO! ################################## \n ")
            print(resultado)
            print("############################ FIM DE CONSULTA! ############################# \n ")

          elif copcao == "3":
            print("################################ RESUMO! ################################## \n ")
            consulta = f'SELECT * FROM Product ORDER BY description'
            cursor.execute(consulta)
            resultado = cursor.fetchall() # utilziar apra leitura do BD
            print(resultado)
            print("############################ FIM DE CONSULTA! ############################# \n ")

          elif copcao == "4":
            consulta = f'SELECT * FROM Cart ORDER BY '
            cursor.execute(consulta)
            resultado = cursor.fetchall() # utilziar apra leitura do BD
            print("################################ RESUMO! ################################## \n ")
            print(resultado)
            print("############################ FIM DE CONSULTA! ############################# \n ")

          elif copcao == "5":
            consulta = f'SELECT * FROM Evaluation'
            cursor.execute(consulta)
            resultado = cursor.fetchall() # utilziar apra leitura do BD
            print("################################ RESUMO! ################################## \n ")
            print(resultado)
            print("############################ FIM DE CONSULTA! ############################# \n ")
          else:
            Cinit = False
      else:
        Appinit = False    
  elif Confirmar == "2":
    initr = True
    print("###################### Ok, Vamos tenrar novamente ################################## \n ")
  else:
    initr = False
    print("###################### Agradecemos pela sua Preferencia ################################## \n ")
    print("############################ Programa Finalizado ################################## \n ")
    break