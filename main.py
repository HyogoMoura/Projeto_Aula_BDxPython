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
  database="db_project_test2"
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

print("###################### Olá, Bem vindo ao SmartList ################################## \n ")
while init == True:
  print("###################### Digite Seus Dados para Iniciar ################################## \n ")
  Nome = input ("Digite seu Nome :  ")
  Cpf = input ("Digite seu CPF :   ")
  Cell = input ("Digite seu Celular:   ")
  Email = input ("Digite seu Email:   ")
  Endereco = input ("Digite seu Endereco:  ")
  comando1 = f'INSERT INTO Users (name, cpf, phone, mail, location) VALUES ("{Nome}", "{Cpf}", "{Cell}", "{Email}", "{Endereco}")'

  print(" ###################### Otimo!!! Ola ", Nome, "Agora preciso que Digite onde esta realizando suas compras? ################################## \n ")

  NomeStore = input ("Digite seu Nome da Loja :  ")
  EnderecoStore = input ("Digite o Endereco da Loja:  ")
  CustoStore = input ("Digite o Custo de Deslocamento:   ")
  comando2 = f'INSERT INTO Store (name, location, comutecost) VALUES ("{Nome}", "{Endereco}", "{CustoStore}")'

  print("###################### Tudo certo!!!", Nome ,"vamos as ompras no ", NomeStore ," ################################## \n ")
  Confirmar = input ("Se seus dados estiverem corretos digite 1 para continuar ou 2 para retornar ou 3 para finalizar \n :")
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
        #Infcart = input ("Digite o numero da sua lista:   ")
        #comando = f'INSERT INTO Cart (Cp_id) VALUES ({Infcart})'
        #cursor.execute(comando)
        #conexao.commit() # Utilizar quando edita (Updade ou Delete) o BD        
        Idlista = input ("Digite o numero da sua lista:   ")
        comando = f'INSERT INTO Cart_Plist (Cp_id) VALUES ({Idlista})'
        cursor.execute(comando)
        conexao.commit() # Utilizar quando edita (Updade ou Delete) o BD

        Linit = True
        print("############################ Vamos inciar ############################# \n ")
        Valor = 0
        cont = 0
        Quantidade = 1
        Mult=0
        i=0
        while Linit == True:
          print("###################################### Sua lista:",Idlista,"###########################################\n ")
          consulta = f'SELECT * FROM Product a JOIN Cart_Plist b ON b.Cp_id = a.P_id'
          #def pesquisarEstabelecimentos():
          #Id = Idlista
          #sql = "Select * Product a JOIN Cart_Plist b ON b.Cp_id = a.P_id WHERE Nome = %d "
          #cursor.execute(sql, (Id))
          cursor.execute(consulta)
          resultado = cursor.fetchall() # utilziar apra leitura do BD
          print(resultado, "\n")
          Total = Quantidade*Valor - Mult
          TotalItens = cont
          print("######################################## Resumo ########################################### \n ")
          print("#################### Total R$:",Total, "Quantidade de Itens:",TotalItens," ################ \n")
          print("############################ Adicione um Produto a sua lista  ############################# \n ")
          Descricao = input ("Digite o Nome do Produto :  ")
          Marca = input ("Digite a Marca se Necessario :   ")
          Codigo = int(input ("Digite o Codigo do Produto caso necessario:   "))
          Valor = float(input ("Digite o valor Unitario do Produto:   "))
          Unidade = input ("Digite a Medida do Produto:  ")
          Quantidade = float(input ("Digite a Quantidade:  "))
          comando4 = f'INSERT INTO Product (description, label, getin, unitvaluer, unit, amount) VALUES ("{Descricao}", "{Marca}", {Codigo}, {Valor}, "{Unidade}", {Quantidade})'
          
          print("############################ Deseja adiconar outro produto?  ############################# \n ")
          Confirmar2 = input ("Digite (1 para adicionar outro produto) (2 para retornar) ou (0 para finalizar)")
          if Confirmar2 == "1":
            Linit = True 
            cont = i+1
            Mult=0
            cursor.execute(comando4)
            conexao.commit() # Utilizar quando edita (Updade ou Delete) o BD
          elif Confirmar2 == "2":
            Linit = True
            i=0
            Mult = Quantidade*Valor
          else:
            Linit = False
            cont = i+1
            cursor.execute(comando4)
            conexao.commit() # Utilizar quando edita (Updade ou Delete) o BD
            Total = Total + Quantidade*Valor
            TotalItens = cont         
            consulta = f'SELECT * FROM Product a JOIN Cart_Plist b ON b.Cp_id = a.P_id'  # DEMOSTRANDO A LISTA!!! VERIFICAR COMO MOSTRA SO A DO ID ESPECIFICO DA COMPRA
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            print(resultado, "\n")
            


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
          print(" Voce selecionou a opcao de consulta \n digite a opcao que deseja consultar")
          copcao = input ("\n 1.Usuario \n 2.Lojas \n 3.Produtos \n 4.Listas \n 5.Comentarios \n :")
          if copcao == "1":
            consulta = f'SELECT * FROM Users'
            cursor.execute(consulta)
            resultado = cursor.fetchall() # utilziar apra leitura do BD
            print(resultado)
          
          elif copcao == "2":
            consulta = f'SELECT * FROM Store'
            cursor.execute(consulta)
            resultado = cursor.fetchall() # utilziar apra leitura do BD
            print(resultado)

          elif copcao == "3":
            consulta = f'SELECT * FROM Product'
            cursor.execute(consulta)
            resultado = cursor.fetchall() # utilziar apra leitura do BD
            print(resultado)

          elif copcao == "4":
            consulta = f'SELECT * FROM Cart'
            cursor.execute(consulta)
            resultado = cursor.fetchall() # utilziar apra leitura do BD
            print(resultado)

          elif copcao == "5":
            consulta = f'SELECT * FROM Comments'
            cursor.execute(consulta)
            resultado = cursor.fetchall() # utilziar apra leitura do BD
            print(resultado)
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