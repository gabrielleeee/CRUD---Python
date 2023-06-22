#Faça um CRUD básico utilizando seus conhecimentos em listas, dicionários, loops de repetição e etc.
#O CRUD é para ajudar um médico a fazer seu controle de pacientes, ele precisa das operações básicas, 
# cadastrar, atualizar, excluir e visualizar os cadastros.
#Os dados que o médico precisa de seus pacientes são: Nome, idade, altura, e se eles são alérgicos
#a algum medicamento, caso sejam, ele anota todos os medicamentos que o paciente tem alergia.
#No programa será necessário que ele sempre volte ao menu quando terminar alguma ação requisitada,
#e caso escolha a opção de sair, o programa é finalizado.

cadastros = []

def cadastrarPaciente():
  print("\n==========CADASTRO DE PACIENTE===========\n")
  nome = input("Nome: ")
  cpf = int(input("CPF: "))
  idade = int(input("Idade: "))
  altura = float(input("Altura: "))
  alergia = input("\nPaciente alergico a algum medicamento? \n Responda com: s ou n\n")

  if alergia == 's':
    medicamentos = input("Medicamentos: ")
    paciente = {"nome" : nome, "cpf" : cpf, "idade" : idade, "altura": altura, "alergia": alergia, "medicamentos": medicamentos} 
  else:
    paciente = {"nome" : nome, "cpf" : cpf, "idade" : idade, "altura" : altura, "alergia" : alergia} 
  
  print("Paciente cadastrado com sucesso!")
  return paciente
  
def mostrarPacientes():
  print("===========PACIENTES CADASTRADOS============\n")
  for paciente in cadastros:
    print(paciente)
  #print(cadastros.items())

def pesquisarPaciente():
  print("============PESQUISA DE PACIENTES===========\n")
  pesquisa = int(input("CPF do paciente: "))
  encontrado = False
  #print(cadastros[pesquisa])

  for paciente in cadastros:
    if paciente.get("cpf") == pesquisa:
        print("Paciente encontrado: \n", paciente)
        encontrado = True
        break

  if not encontrado:
      print("Paciente não encontrado")


def atualizarPaciente():
  print("\n==========ATUALIZAÇÃO DE CADASTRO ============\n")
  pesquisa = int(input("CPF do paciente que deseja atualizar: "))
  encontrado = False
  
  for i in range(len(cadastros)):
    if cadastros[i].get('cpf') == pesquisa:
       cadastros[i] = cadastrarPaciente()
       encontrado = True
       print("\nO paciente foi atualizado com sucesso!\n")
       break
    
    if not encontrado:
      print("Paciente não encontrado")
  

def excluirPaciente():
  pesquisa = int(input("CPF do paciente: "))

  for i in range(len(cadastros)):
    if cadastros[i]['cpf'] == pesquisa:
      del cadastros[i]
      print("Paciente excluído com sucesso!")


opcao = 0
while opcao != 6:
  print("\n===================MENU=================\n")
  print("1 - Cadastar Novo Paciente \n2 - Mostrar Pacientes Cadastrados \n3 - Pesquisar Paciente")
  print("4 - Atualizar dados de um paciente \n5 - Excluir Um Paciente \n6 - Finalizar programa")

  opcao = int(input("\nDigite a opção desejada: \n"))

  if opcao == 1:
    cadastros.append(cadastrarPaciente())
  elif opcao == 2:
    mostrarPacientes()
  elif opcao == 3:
   pesquisarPaciente()
  elif opcao == 4:
    atualizarPaciente()
  elif opcao == 5:
    excluirPaciente()
  else:
    print("\nPrograma finalizado!")